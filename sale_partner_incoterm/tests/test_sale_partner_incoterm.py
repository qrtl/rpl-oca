# Copyright 2015 Opener B.V. (<https://opener.am>)
# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestSalePartnerIncoterm(TransactionCase):
    def test_sale_partner_incoterm(self):
        """
        Check that the customer's default incoterm is retrieved in the
        sales order's onchange
        """
        res_partner = self.env["res.partner"]
        incoterm_exw = self.env.ref("account.incoterm_EXW")
        incoterm_fca = self.env.ref("account.incoterm_FCA")
        customer_1 = res_partner.create({"name": "customer 1"})
        customer_2 = res_partner.create(
            {
                "name": "customer 2",
                "sale_incoterm_id": incoterm_exw.id
            }
        )
        customer_3 = res_partner.create(
            {
                "name": "customer 3",
                "sale_incoterm_id": incoterm_fca.id
            }
        )
        # No incoterm on either partner
        sale_order = self.env["sale.order"].create({"partner_id": customer_1.id})
        sale_order.onchange_partner_id_incoterm()
        self.assertFalse(sale_order.incoterm)
        # Incoterm set only on delivery address
        sale_order.partner_shipping_id = customer_2
        sale_order.onchange_partner_id_incoterm()
        self.assertEqual(sale_order.incoterm, incoterm_exw)
        # Incoterm set only on customer
        sale_order.partner_id = customer_2
        sale_order.partner_shipping_id = customer_1
        sale_order.onchange_partner_id_incoterm()
        self.assertEqual(sale_order.incoterm, incoterm_exw)
        # Incoterm set on both partners
        sale_order.partner_shipping_id = customer_3
        sale_order.onchange_partner_id_incoterm()
        self.assertEqual(sale_order.incoterm, incoterm_fca)
