from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    max_discount = fields.Float(
        string="Maximum Allowed Discount (%)",
        help="Maximum discount allowed for this customer on sale order lines.",
        default=0.0,
    )
