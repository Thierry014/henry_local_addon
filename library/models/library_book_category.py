from odoo import api, fields, models


class BookCategory(models.Model):
    _name = 'book.category'
    _description = 'Category of the book'

    name = fields.Char(string='Name')
    description = fields.Text(string='About this Category')
    over18 = fields.Boolean(string='18+')


    def make_it(self):
        print('>>>>>>>>>>>>>>>>>>Make it<<<<<<<<<<<<<<<')
        self.ensure_one()
        book = self.env['library.book'].search([('id','=',2)])
        book.with_context(avoid_deactivate=True)
