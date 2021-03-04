# -*- coding: utf-8 -*-
# from odoo import http


# class Codeplay(http.Controller):
#     @http.route('/codeplay/codeplay/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/codeplay/codeplay/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('codeplay.listing', {
#             'root': '/codeplay/codeplay',
#             'objects': http.request.env['codeplay.codeplay'].search([]),
#         })

#     @http.route('/codeplay/codeplay/objects/<model("codeplay.codeplay"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('codeplay.object', {
#             'object': obj
#         })
