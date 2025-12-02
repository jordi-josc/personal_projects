# Sale Cancellation Reason

## How it works
- **Action Interception**: The module overrides the standard `action_cancel` method on Sales Orders.
- **Mandatory Wizard**: instead of cancelling immediately, it triggers a popup window (`TransientModel`) requiring the user to input a text explanation.
- **Data Storage**: The input is saved into a new field `cancel_note` on the `sale.order` model.
- **UI Logic**: The cancellation note is displayed on the Quotation/Order form view **only** when the state is 'Cancelled'.

## Technical details
To allow the cancellation to proceed after the wizard is confirmed, the module uses a specific context key to bypass the interception logic:

```python
# The wizard confirms the action and calls the cancel method again with this context
return self.order_id.with_context(bypass_cancel_wizard=True).action_cancel()