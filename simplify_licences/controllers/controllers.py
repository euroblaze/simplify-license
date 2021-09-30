# -*- coding: utf-8 -*-
# from odoo import http


# class SimplifyLicences(http.Controller):
#     @http.route('/simplify_licences/simplify_licences/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simplify_licences/simplify_licences/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simplify_licences.listing', {
#             'root': '/simplify_licences/simplify_licences',
#             'objects': http.request.env['simplify_licences.simplify_licences'].search([]),
#         })

#     @http.route('/simplify_licences/simplify_licences/objects/<model("simplify_licences.simplify_licences"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simplify_licences.object', {
#             'object': obj
#         })
