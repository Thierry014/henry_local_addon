# -*- coding: utf-8 -*-

from odoo import models, fields, api



class House(models.Model):
    _name = 'house'
    _description = 'Model about properties'

    name = fields.Char(string='Title')
    description = fields.Text(string='Descripyion')

    
    postcode = fields.Char(string='Postcode')
    # computed field 
    suburb = fields.Char(string='Suburb')
    
    currency_id = fields.Many2one('res.currency', string='Currency')
    expected_price = fields.Monetary('Expected Price')
    bedroom = fields.Integer(string='Bedrooms')
    bathroom = fields.Integer(string='Bathrooms')
    garage = fields.Integer(string='Garage')

    garden = fields.Boolean(string='Garden')
    active = fields.Boolean(string='Active', default=True)

    available_from = fields.Date(string='Available date', default=fields.date.today())
    selling_price = fields.Monetary('Selling Price', readonly=True)
    living_area = fields.Float(string='Living area(sqm)')
    total_area = fields.Float(string='Total area(sqm)')

    # property_cat = fields.Selection(string='House Category', selection=[('townhouse', 'Townhouse'), ('apartment', 'Apartment'),])
    property_cat_id = fields.Many2one(comodel_name='house.category', string='House Category')
    
    property_type = fields.Selection(string='House Type', selection=[('new', 'New house'), ('second', '2nd hand')], default='new')
    property_selling_status = fields.Selection(string='', selection=[('listed', 'Listed'), ('sold', 'Sold'),])

    link = fields.Char(string='Url')
    
    # iframe = fields.Char(string='Iframe link')
    
    house_map = fields.Html(string='house_map')

    seller = fields.Many2one(comodel_name='res.users', string='Sales Person', default=lambda self: self.env.user)
    buyer = fields.Many2one(comodel_name='res.partner', string='Buyer')

    tag_ids = fields.Many2many(comodel_name='house.tag', string='')
    
    
    
    
    # google map field => can be a binary or iframe or something else

    def test(self):
        ...

    

    

    
    
    
    