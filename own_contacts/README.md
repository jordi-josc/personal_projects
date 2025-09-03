# Private Contacts Access
## How it works
- **Custom Module Category**: `Private Contacts`
- **Security Group**: `Private Contacts User`
- **Record Rule**: Restrict users so they can only:
  - See their own contact (`res.partner` linked to their user account)
  - See the contacts they are explicitly assigned to (via `user_id`)

Another possibility: the right we create can be extended to also allow visibility of **unassigned contacts** by changing the domain to:
```python
['|', ('id', '=', user.partner_id.id), ('user_id', 'in', [user.id, False])]