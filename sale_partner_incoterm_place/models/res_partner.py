# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    sale_incoterm_place = fields.Char(
        "Default Sales Incoterm Place",
        help="The default incoterm place for new sales orders for this partner."
    )
