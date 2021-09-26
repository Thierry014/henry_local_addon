from odoo import api, fields, models


class BikeBrand(models.Model):
    _name = 'bike.brand'
    _description = 'Brand'

    name = fields.Char(string='Name')
    logo = fields.Binary(string='')
    description = fields.Text(string='About Brand')
    size_chart = fields.Binary(string='Size chart')
    


class BikeCategory(models.Model):
    _name = 'bike.category'
    _description = 'Category'

    name = fields.Char(string='Name')


class BikePart(models.Model):
    _name = 'bike.parts'
    _description = 'parts'

    name = fields.Char(string='Name')
    level = fields.Selection(string='Level', selection=[('low', 'Leisure'),('entry', 'Entry'), ('mid', 'Mid'),('top', 'Top')])
    
    