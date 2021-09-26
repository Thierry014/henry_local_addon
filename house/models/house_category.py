from odoo import api, fields, models


class HouseCategory(models.Model):
    _name = 'house.category'
    _description = 'type of a property'

    name = fields.Char(string='Name')


class HouseTag(models.Model):
    _name = 'house.tag'
    _description = 'tag of a property'

    name = fields.Char(string='Name')
