from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cancel_note = fields.Text(
        string="Cancellation Reason",
        readonly=True,
    )

    def action_cancel(self):
        if self.env.context.get('bypass_cancel_wizard'):
            return super(SaleOrder, self).action_cancel()

        return {
            'name': 'Reason for Cancellation',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.cancel.wizard',
            'target': 'new',
            'context': {'default_order_id': self.id},
        }
