# -*- coding: utf-8 -*-
# from odoo import http


# class Lra(http.Controller):
#     @http.route('/lra/lra', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lra/lra/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lra.listing', {
#             'root': '/lra/lra',
#             'objects': http.request.env['lra.lra'].search([]),
#         })

#     @http.route('/lra/lra/objects/<model("lra.lra"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lra.object', {
#             'object': obj
#         })
