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



