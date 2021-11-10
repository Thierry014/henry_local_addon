# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Library(models.Model):
    _name = 'library.book'
    _description = 'Something about the books'
    _rec_name = 'name'
    # _order = 'order in tree view' 

    @api.model
    def _get_author_name(self):
        print(f'>>>>>>>>>>>>>>>>{self.author_id}<<<<<<<<<<<<<')
        return self.author_id.name

    name = fields.Char(string='Book Name')
    date_release = fields.Date(string='Released date')
    date_updated = fields.Datetime(string='Last update time')
    
    author_id = fields.Many2many(comodel_name='res.partner', string='Authors')
    author_name = fields.Char(string='Author name', default=_get_author_name)
    
    publisher_id = fields.Many2one(comodel_name='res.partner', string='Publisher')
    city = fields.Char(string='City', related='publisher_id.city')
    
    

    state = fields.Selection(
                            selection=[('draft', 'Not available'), 
                            ('available', 'Available'),
                            ('lost', 'Lost')]
                            ,default='draft', string='State')


    
    description = fields.Html(string='Description')
    cover = fields.Binary(string='Book Cover')
    page = fields.Integer(string='Nubmer of Pages')
    rating = fields.Float(string='Rating', digits=(1,1))


    # other model
    category_ids = fields.Many2many(comodel_name='book.category', string='Categories')

   
    
    

    
    
    
    def test(self):
        print('>>>>>>>>>>>>>Function activated')

        for r in self:
            print(f">>>>>>>>>>>{self.env.context.get('avoid_deactivate')}")

    

    @api.constrains('date_updated')
    def _genuine_book(self):
        for r in self:
            if r.date_updated:
                print(f'>>>>>>>>>>>>>>{r.name}<<<<<<<<<<<')

