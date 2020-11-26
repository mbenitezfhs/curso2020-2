from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = "helpdesk Ticket"

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    date = fields.Date(string='Fecha')

    #Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection([('new', 'Nuevo'), 
                ('assigned', 'Asignado'),
                ('inprogress', 'En proceso'),
                ('pending', 'Pendiente'),
                ('resolved', 'Resuelto'),
                ('cancel', 'Cancelado')],
                string='State',
                default='new'
                )
    #Tiempo dedicado (en horas)
    dedicated_time = fields.Float(string='Time')
    #Asignado (tipo check)
    assign = fields.Boolean(string='Asignado', readonly="true")
    #Fecha límite
    limit_date = fields.Date(string='Fecha limite')
    #Acción correctiva (html)
    action_corrective = fields.Html(string='Acción correctiva')
    #Acción preventiva (html)
    action_preventive = fields.Html(string='Acción preventiva', help="this is a help")


    user_id = fields.Many2one(comodel_name='res.users', string='Assigned to')

    def set_assigned(self):
        self.ensure_one()
        self.write({
            'assign': True,
            'state': 'assigned',
            'user_id': self.env.uid
        })

    def set_progress(self):
        self.ensure_one()
        self.state = 'inprogress'

    def set_waiting(self):
        self.ensure_one()
        self.state = 'pending'

    def set_done(self):
        self.ensure_one()
        self.state = 'resolved'

    def set_cancel(self):
        self.ensure_one()
        self.state = 'cancel'