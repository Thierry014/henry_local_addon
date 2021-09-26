# -*- coding: utf-8 -*-

from odoo.addons import decimal_precision as dp
from odoo import models, fields, api

class Bike(models.Model):
    _inherit = 'product.product'

    is_bike = fields.Boolean(string='Is Bike')
    brand_id = fields.Many2one(comodel_name='bike.brand', string='Brand')
    cate_id = fields.Many2one(comodel_name='bike.category', string='Category')
    part_ids = fields.Many2many(comodel_name='bike.parts', string='Parts')
    offical_link = fields.Char(string="Link")
    second_hand_price = fields.Float(string='2nd Price', digits=dp.get_precision('Product Price'))
    second_hand_link = fields.Char(string="2nd Link")
    year = fields.Char(string='Year')
    weight = fields.Float(string='Weight(kg)',digits=(3,2))

    state = fields.Selection(string='state', selection=[('draft', 'draft'), ('done', 'done'),('cancel', 'cancel')], default="draft")
    
    

    def test(self):
        ...

    
