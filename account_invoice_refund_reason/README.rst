=============================
Account Invoice Refund Reason
=============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:c67247626b13cce1861089c7f197c5d18b008dad8785a34e4450f775338913b5
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--invoicing-lightgray.png?logo=github
    :target: https://github.com/OCA/account-invoicing/tree/12.0/account_invoice_refund_reason
    :alt: OCA/account-invoicing
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-invoicing-12-0/account-invoicing-12-0-account_invoice_refund_reason
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-invoicing&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows you to define a list of reasons to create a credit note from
a customer invoice or vendor bill and report on them.

**Table of contents**

.. contents::
   :local:

Configuration
=============

* Go to *Accounting > Configuration > Management > Refund Reasons*
* Review the list of predefined reasons to update them or add new ones

Usage
=====

* Go to *Accounting > Customers > Invoices* (or *Accounting > Vendors > Bills*)
* Select an open invoice
* Click on "Add Credit Note"
* In the wizard, select the reason and add the credit note
* In the pivot view, group customer invoices by Reason

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-invoicing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-invoicing/issues/new?body=module:%20account_invoice_refund_reason%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Open Source Integrators
* Serpent CS

Contributors
~~~~~~~~~~~~

* Open Source Integrators <http://www.opensourceintegrators.com>

  * Maxime Chambreuil <mchambreuil@opensourceintegrators.com>

* Serpent Consulting Services Pvt. Ltd. <support@serpentcs.com>

  * Chanakya Soni <chanakya.soni@serpentcs.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-max3903| image:: https://github.com/max3903.png?size=40px
    :target: https://github.com/max3903
    :alt: max3903

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-max3903| 

This module is part of the `OCA/account-invoicing <https://github.com/OCA/account-invoicing/tree/12.0/account_invoice_refund_reason>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
