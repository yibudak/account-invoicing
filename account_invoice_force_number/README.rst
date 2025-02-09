====================
Force Invoice Number
====================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:cb0638b481e725c13ca8926fe74215a24addc38dd572103c06529673698ca4d9
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--invoicing-lightgray.png?logo=github
    :target: https://github.com/OCA/account-invoicing/tree/12.0/account_invoice_force_number
    :alt: OCA/account-invoicing
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-invoicing-12-0/account-invoicing-12-0-account_invoice_force_number
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-invoicing&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows to force the invoice numbering. It displays the move_name field. If user fills that field, the typed value will be used as invoice (and move) number. Otherwise, the next sequence number will be retrieved and saved. So, the new field has to be used when user doesn't want to use the default invoice numbering for a specific invoice.

**Table of contents**

.. contents::
   :local:

Configuration
=============

The user has to belong to the *Allow "Invoice Force Number"* group.
This can be done as follows:

* checking the corresponding setting on the Access Rights (Technical Settings) of the user
* manually adding it to the corresponding group

Usage
=====

Once installed, you'll find the Force Number field on all the invoices in draft state. You can then fill in this field with the invoice number you want to assign. The invoice will get this number when confirmed.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-invoicing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-invoicing/issues/new?body=module:%20account_invoice_force_number%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Agile Business Group

Contributors
~~~~~~~~~~~~

* Alex Comba <alex.comba@agilebg.com> (https://www.agilebg.com/)
* Francesco Apruzzese <f.apruzzese@apuliasoftware.it>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/account-invoicing <https://github.com/OCA/account-invoicing/tree/12.0/account_invoice_force_number>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
