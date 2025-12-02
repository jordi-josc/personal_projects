from odoo import models, fields, api


class SaleCancelWizard(models.TransientModel):
    _name = 'sale.cancel.wizard'
    _description = 'Sale Cancellation Wizard'

    order_id = fields.Many2one('sale.order', string="Order", required=True)

    note = fields.Text(string="Reason / Note", required=True)

    def action_confirm_cancel(self):
        self.ensure_one()

        self.order_id.write({
            'cancel_note': self.note
        })

        return self.order_id.with_context(bypass_cancel_wizard=True).action_cancel()
