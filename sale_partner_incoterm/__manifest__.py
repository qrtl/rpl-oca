# Copyright 2015 Opener B.V. (<https://opener.am>)
# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Default sales incoterm per partner',
    'version': '12.0.1.1.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'summary': "Set the customer preferred incoterm on each sales order",
    'author': "Opener B.V.,Odoo Community Association (OCA)",
    'website': 'https://github.com/oca/sale-workflow',
    'depends': [
        'sale_stock'
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
}
