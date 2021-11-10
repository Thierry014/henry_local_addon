# -*- coding: utf-8 -*-

from . import controllers
from . import models

from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    print(f'>>>>>>>>>>> post_init_hook run <<<<<<<<<<<<<<')
    # select m2o.name 
    records = env['library.book'].search([])
    print(f'>>>>record:{records}<<<><<')
    for record in records:
        record.author_name = record.author_id.name
        print(f'set {record.author_id.name} to {record.author_name}')