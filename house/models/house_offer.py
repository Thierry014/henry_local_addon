from odoo import api, fields, models


class HouseOffer(models.Model):
    _name = 'house.offer'
    _description = 'offers of a proerty'

    # name = fields.Char(string='Name')

    property_id = fields.Many2one(comodel_name='house' ,string='Property')
    # buyer???
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    
    price = fields.Float(string='Offer Price')
    offer_state = fields.Selection(string='State', selection=[('applied', 'Draft'),('accepted', 'Accepted'), ('refuesd', 'Refuesd'),], default='applied')
    
    
    def show_ctx(self):
        print(self.env.context)