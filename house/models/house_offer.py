
from datetime import datetime, timedelta, date

from odoo import api, fields, models
from odoo.tools import date_utils


class HouseOffer(models.Model):
    _name = 'house.offer'
    _description = 'offers of a proerty'

    # name = fields.Char(string='Name')

    property_id = fields.Many2one(comodel_name='house' ,string='Property')
    # buyer???
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    
    price = fields.Float(string='Offer Price')
    validity = fields.Integer(string='Day(s)')
    offer_deadline = fields.Date(string='Deadline', compute='_get_deadline', inverse='_inverse_deadline')
    
    
    offer_state = fields.Selection(string='State', selection=[('applied', 'Draft'),('accepted', 'Accepted'), ('refused', 'Refuesd'),], default='applied')
    
    # odoo function
    def show_ctx(self):
        print(self.env.context)
    
    def accept_offer(self):
        # find all accept record(s) use filter 
        for rec in self:
            accepted_rec = rec.property_id.offer_ids.filtered(lambda offer: offer.offer_state == 'accepted')
            for record in accepted_rec:
                record.offer_state = 'refused'
            rec.offer_state = 'accepted'
    
        
    
    def refuse_offer(self):
        for rec in self:
            rec.offer_state = 'refused'
    
    # computed function 

    @api.depends('validity')
    def _get_deadline(self):
        for rec in self:
            now = date.today()
            rec.offer_deadline = now + timedelta(days=rec.validity)

    def _inverse_deadline(self):
        ...