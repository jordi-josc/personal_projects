{
    'name': "Sale Cancellation Reason",
    "version": "19.0.1.0.0",
    "author": "Jordi-josc",
    "license": "AGPL-3",
    "website": "https://github.com/jordi-josc/personal_projects",
    'category': 'Sales',
    "depends": ["sale"],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_cancel_wizard_view.xml',
        'views/sale_cancel_reason_view.xml',
    ],
}
