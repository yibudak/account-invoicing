# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    pricelist_id = fields.Many2one(
        comodel_name='product.pricelist',
        string='Pricelist',
        readonly=True,
        states={'draft': [('readonly', False)]},
    )

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id_account_invoice_pricelist(self):
        if self.partner_id and self.type in ('out_invoice', 'out_refund')\
                and self.partner_id.property_product_pricelist:
            self.pricelist_id = self.partner_id.property_product_pricelist

    @api.multi
    def button_update_prices_from_pricelist(self):
        for inv in self.filtered(lambda r: r.state == 'draft'):
            inv.invoice_line_ids.filtered('product_id').update_from_pricelist()
        self.filtered(lambda r: r.state == 'draft').compute_taxes()

    @api.model
    def _prepare_refund(self, invoice, date_invoice=None, date=None,
                        description=None, journal_id=None):
        """Pricelist should also be set on refund."""
        values = super(AccountInvoice, self)._prepare_refund(
            invoice, date_invoice=date_invoice, date=date,
            description=description, journal_id=journal_id)
        if invoice.pricelist_id:
            values.update({
                'pricelist_id': invoice.pricelist_id.id,
            })
        return values


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.onchange('product_id', 'quantity')
    def _onchange_product_id_account_invoice_pricelist(self):
        if not self.invoice_id.pricelist_id or not self.invoice_id.partner_id:
            return
        product = self.product_id.with_context(
            lang=self.invoice_id.partner_id.lang,
            partner=self.invoice_id.partner_id.id,
            quantity=self.quantity,
            date=self.invoice_id.date_invoice,
            pricelist=self.invoice_id.pricelist_id.id,
            uom=self.uom_id.id,
            fiscal_position=(
                self.invoice_id.partner_id.property_account_position_id.id)
        )
        self.price_unit = product.price

    @api.onchange('uom_id')
    def _onchange_uom_id(self):
        super(AccountInvoiceLine, self)._onchange_uom_id()
        if self.invoice_id.pricelist_id:
            self._onchange_product_id_account_invoice_pricelist()

    @api.multi
    def update_from_pricelist(self):
        """overwrite current prices from pricelist"""
        for line in self.filtered(lambda r: r.invoice_id.state == 'draft'):
            line._onchange_product_id_account_invoice_pricelist()
