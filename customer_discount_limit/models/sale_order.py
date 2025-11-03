from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.constrains("discount")
    def _check_customer_discount_limit(self):
        for line in self:
            if (
                line.order_id.partner_id
                and line.order_id.partner_id.max_discount > 0
                and line.discount > line.order_id.partner_id.max_discount
            ):
                raise UserError(
                    _(
                        "Discount %.2f%% exceeds the maximum allowed (%.2f%%) "
                        "for customer %s."
                    )
                    % (
                        line.discount,
                        line.order_id.partner_id.max_discount,
                        line.order_id.partner_id.name,
                    )
                )
