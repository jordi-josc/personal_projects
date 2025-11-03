# Customer Discount Limit
## How it works
- **Custom Module Category**: `Sales`
- **New Field**: `max_discount` on `res.partner`  
  Defines the maximum allowed discount per customer.
- **Constraint**: On `sale.order.line`, prevents applying discounts above that limit.

Example:
```python
if line.discount > line.order_id.partner_id.max_discount:
    raise UserError(_("Discount %.2f%% exceeds the maximum allowed (%.2f%%) for customer %s.") % (...))