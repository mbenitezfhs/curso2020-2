
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
        "views/helpdesk_ticket_views.xml",
    ]
}