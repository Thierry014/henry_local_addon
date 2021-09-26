from odoo import api, fields, models


class BikeSoWizard(models.TransientModel):
    _name = 'bike.bikeso.wizard'
    _description = 'create a sale order based on current bike'


    # get default

    bike_id = fields.Many2one(comodel_name='product.product', string='Bike', readonly=True)
    
    
    def create_bike_sale_order(self):
        val = {}
        print(val)

        # get SO object, create a sale order 