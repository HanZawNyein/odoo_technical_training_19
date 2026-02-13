from odoo import api, fields, models


class HmsRoom(models.Model):
    _name = 'hms.room'  # hms_room
    _description = 'HmsRoom'

    name = fields.Char()
    state = fields.Selection([
        ('available', 'Available'),
        ('not_available', 'Not Available')], default='available')
