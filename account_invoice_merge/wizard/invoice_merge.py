<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
>>>>>>> upstream/12.0
# Copyright 2004-2010 Tiny SPRL (http://tiny.be).
# Copyright 2010-2011 Elico Corp.
# Copyright 2016 Acsone (https://www.acsone.eu/)
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
<<<<<<< HEAD
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, exceptions, fields, models
=======
# Copyright 2019 Okia SPRL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.exceptions import UserError
>>>>>>> upstream/12.0
from odoo.tools.translate import _


class InvoiceMerge(models.TransientModel):
    _name = "invoice.merge"
    _description = "Merge Partner Invoice"

    keep_references = fields.Boolean('Keep references from original invoices',
                                     default=True)
    date_invoice = fields.Date('Invoice Date')

    @api.model
<<<<<<< HEAD
=======
    def _get_not_mergeable_invoices_message(self, invoices):
        """Overridable function to custom error message"""
        key_fields = invoices._get_invoice_key_cols()
        error_msg = {}
        if len(invoices) != len(invoices._get_draft_invoices()):
            error_msg['state'] = (
                _('Megeable State (ex : %s)') %
                (invoices and invoices[0].state or _('Draf')))
        for field in key_fields:
            if len(set(invoices.mapped(field))) > 1:
                error_msg[field] = invoices._fields[field].string
        return error_msg

    @api.model
>>>>>>> upstream/12.0
    def _dirty_check(self):
        if self.env.context.get('active_model', '') == 'account.invoice':
            ids = self.env.context['active_ids']
            if len(ids) < 2:
<<<<<<< HEAD
                raise exceptions.Warning(
=======
                raise UserError(
>>>>>>> upstream/12.0
                    _('Please select multiple invoices to merge in the list '
                      'view.'))

            invs = self.env['account.invoice'].browse(ids)
<<<<<<< HEAD
            for d in invs:
                if d['state'] != 'draft':
                    raise exceptions.Warning(
                        _('At least one of the selected invoices is %s!') %
                        d['state'])
                if d['account_id'] != invs[0]['account_id']:
                    raise exceptions.Warning(
                        _('Not all invoices use the same account!'))
                if d['company_id'] != invs[0]['company_id']:
                    raise exceptions.Warning(
                        _('Not all invoices are at the same company!'))
                if d['partner_id'] != invs[0]['partner_id']:
                    raise exceptions.Warning(
                        _('Not all invoices are for the same partner!'))
                if d['type'] != invs[0]['type']:
                    raise exceptions.Warning(
                        _('Not all invoices are of the same type!'))
                if d['currency_id'] != invs[0]['currency_id']:
                    raise exceptions.Warning(
                        _('Not all invoices are at the same currency!'))
                if d['journal_id'] != invs[0]['journal_id']:
                    raise exceptions.Warning(
                        _('Not all invoices are at the same journal!'))
=======
            error_msg = self._get_not_mergeable_invoices_message(invs)
            if error_msg:
                all_msg = _("All invoices must have the same: \n")
                all_msg += '\n'.join([value for value in error_msg.values()])
                raise UserError(all_msg)
>>>>>>> upstream/12.0
        return {}

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False,
                        submenu=False):
        """Changes the view dynamically
         @param self: The object pointer.
         @param cr: A database cursor
         @param uid: ID of the user currently logged in
         @param context: A standard dictionary
         @return: New arch of view.
        """
        res = super(InvoiceMerge, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=False)
        self._dirty_check()
        return res

    @api.multi
    def merge_invoices(self):
        """To merge similar type of account invoices.

             @param self: The object pointer.
             @param cr: A database cursor
             @param uid: ID of the user currently logged in
             @param ids: the ID or list of IDs
             @param context: A standard dictionary

             @return: account invoice action
        """
        inv_obj = self.env['account.invoice']
        aw_obj = self.env['ir.actions.act_window']
        ids = self.env.context.get('active_ids', [])
        invoices = inv_obj.browse(ids)
        allinvoices = invoices.do_merge(keep_references=self.keep_references,
                                        date_invoice=self.date_invoice)
        xid = {
            'out_invoice': 'action_invoice_tree1',
            'out_refund': 'action_invoice_tree1',
            'in_invoice': 'action_invoice_tree2',
            'in_refund': 'action_invoice_tree2',
        }[invoices[0].type]
        action = aw_obj.for_xml_id('account', xid)
        action.update({
            'domain': [('id', 'in', ids + list(allinvoices.keys()))],
        })
        return action
