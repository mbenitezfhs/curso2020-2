
{
    "name": "Helpdesk Ticket",
    "summary": "Module ticket",
    "version": "13.0.1.0.0",
    "category": "Uncategorized",
    "author": "Manuel Benitez",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/some_model_security.xml",
        "security/ir.model.access.csv",
        'wizards/new_ticket_from_tag_views.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_tag_views.xml',
        'views/helpdesk_action_views.xml',
        'data/helpdesk_data.xml',
    ]
}