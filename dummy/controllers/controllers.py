# -*- coding: utf-8 -*-
from odoo import http

# class Scaffold-template(http.Controller):
#     @http.route('/scaffold-template/scaffold-template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaffold-template/scaffold-template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaffold-template.listing', {
#             'root': '/scaffold-template/scaffold-template',
#             'objects': http.request.env['scaffold-template.scaffold-template'].search([]),
#         })

#     @http.route('/scaffold-template/scaffold-template/objects/<model("scaffold-template.scaffold-template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaffold-template.object', {
#             'object': obj
#         })