from odoo import api, fields, models


class HouseCategory(models.Model):
    _name = 'house.category'
    _description = 'type of a property'

    name = fields.Char(string='Name')
    house_ids = fields.One2many(comodel_name='house', inverse_name='property_cat_id', string='House category')
    offer_count = fields.Integer(string='', compute='_get_offer_count')
    
    
    def show_related_offer(self):
        return{
            'name': 'Offers',# name can be anything
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'house.offer',
            'type': 'ir.actions.act_window',
            'domain': [('property_id.property_cat_id','in', [self.id])],
        }
    
    def _get_offer_count(self):
        for r in self:
            all_offers = self.env['house.offer'].search([('property_id.property_cat_id.id','=',r.id)])
            r.offer_count = len(all_offers)

class HouseTag(models.Model):
    _name = 'house.tag'
    _description = 'tag of a property'

    name = fields.Char(string='Name')
    color = fields.Integer(string='')
    
