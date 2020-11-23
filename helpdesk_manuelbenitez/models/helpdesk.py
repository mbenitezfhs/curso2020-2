from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = "helpdesk Ticket"

    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
    date = fields.Date(string='Fecha')