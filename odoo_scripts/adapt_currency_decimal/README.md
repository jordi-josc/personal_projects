# Adapt Currency Decimal

Description
- Small SQL script to adjust a currency's rounding and decimal precision in an Odoo database (example: USD).
- Updates the `res_currency` table fields `rounding` and `decimal_places`.
- This is a sample, to do it in a production database, it's required a more complex script. In this case, we round the decimals to 2.

Files
- `currency_decimal.sql` — SQL statement to change `rounding` and `decimal_places`.

Example SQL
```sql
UPDATE res_currency
SET rounding = 0.01,
    decimal_places = 2
WHERE name = 'USD';
```

Safety notes
- Test in development or staging first.
- Verify no modules or automated jobs will overwrite these values after the change.
- Prefer writing an Odoo migration or module update if you need a repeatable, integrated change.

Variations
- Target a different currency: change `WHERE name = 'USD'`.
- Apply to multiple currencies: `WHERE name IN ('USD','EUR')`.