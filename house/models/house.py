# -*- coding: utf-8 -*-

from odoo import models, fields, api



class House(models.Model):
    _name = 'house'
    _description = 'Model about properties'

    # sql constraints 
    # ['constraint name','CHECK(field value >< ?)',
    # 'error message'
    # ]
    _sql_constraints = [
         ('check_price', 'CHECK(expected_price >= 0)',
         'The price of the house should >= 0 .')
    ]

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
    best_offer = fields.Float(string='Best Offer', compute='_get_best_offer')
    
    living_area = fields.Float(string='Living area(sqm)')
    total_area = fields.Float(string='Total area(sqm)')

    # property_cat = fields.Selection(string='House Category', selection=[('townhouse', 'Townhouse'), ('apartment', 'Apartment'),])
    property_cat_id = fields.Many2one(comodel_name='house.category', string='House Category')
    
    property_type = fields.Selection(string='House Type', selection=[('new', 'New house'), ('second', '2nd hand')], default='new')
    property_selling_status = fields.Selection(string='', selection=[('listed', 'Listed'),
                                                                     ('received', 'Offer Received'),
                                                                     ('confirmed', 'Offer Confirmed'),
                                                                     ('sold', 'Sold'),
                                                                     ('cancelled', 'Cancelled')], default='listed')

    link = fields.Char(string='Url')
    
    # iframe = fields.Char(string='Iframe link')
    
    house_map = fields.Html(string='house_map')

    seller = fields.Many2one(comodel_name='res.users', string='Sales Person', default=lambda self: self.env.user)
    buyer = fields.Many2one(comodel_name='res.partner', string='Buyer')

    tag_ids = fields.Many2many(comodel_name='house.tag', string='')

    offer_ids = fields.One2many(comodel_name='house.offer', inverse_name='property_id', string='')
    
    
    
    
    
# google map field => can be a binary or iframe or something else

    def mark_as_sold(self):
        # todo only can be sold when offer confirmed 
        for rec in self:
            # if rec.property_selling_status in ['confirmed']:
            rec.property_selling_status = 'sold'

    def mark_as_cancelled(self):
         for rec in self:
            # if rec.property_selling_status in ['sold','listed','reveived']:
            rec.property_selling_status = 'cancelled'

    
# computed function 

    @api.depends('offer_ids')    
    def _get_best_offer(self):
        for record in self:
            if len(record.offer_ids)>0:
                best_order = max(record.offer_ids.mapped('price'))
                self.best_offer = best_order
                
    

    
    
    
    