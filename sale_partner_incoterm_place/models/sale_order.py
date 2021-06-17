# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("partner_shipping_id", "partner_shipping_id")
    def onchange_partner_id_incoterm(self):
        super().onchange_partner_id_incoterm()
        if not self.partner_shipping_id:
            self.incoterm_place = False
            return
        if self.partner_shipping_id.sale_incoterm_id:
            self.incoterm_place = self.partner_shipping_id.sale_incoterm_place
        else:
            if not self.partner_id:
                self.incoterm_place = False
                return
            self.incoterm_place = self.partner_id.sale_incoterm_place
