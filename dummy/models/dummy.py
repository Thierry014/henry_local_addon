import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)


############################################################################################################################################
class Dummy(models.Model):
    _name = 'dummy'
    _description="dummy class is used for testing purposes "

    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
    task_list = fields.Text(string='Task LIST')
#
  

    def dummy_test(self):
        data = self.env['ir.config_parameter'].browse(1).exists()
        if data:
            _logger.warning(data)
            # http://localhost:8069
        else:
            _logger.error(False)

##########################################################################################
# edit email template 
# 1. get it's type
# 2. change it's email temaplate in settings
# 3. add account into manifest

            # ('out_invoice','Customer Invoice'),
            # ('in_invoice','Vendor Bill'),
            # ('out_refund','Customer Credit Note'),
            # ('in_refund','Vendor Credit Note'),

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    subject_type = fields.Char(string='', compute='_get_type')
    

    def _get_type(self):
        for r in self:
            if r.type:
                if r.type == 'out_invoice':
                    r.subject_type = 'Invoice' 
                elif r.type == 'in_invoice':
                    r.subject_type = 'Vendor Bill' 
                elif r.type == 'out_refund':
                    r.subject_type = 'Customer Credit Note' 
                elif r.type == 'in_refund':
                    r.subject_type = 'Credit Note' 

                    

