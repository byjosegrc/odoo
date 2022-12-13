# -*- coding: utf-8 -*-
# from odoo import http


# class Pueblos(http.Controller):
#     @http.route('/pueblos/pueblos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pueblos/pueblos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pueblos.listing', {
#             'root': '/pueblos/pueblos',
#             'objects': http.request.env['pueblos.pueblos'].search([]),
#         })

#     @http.route('/pueblos/pueblos/objects/<model("pueblos.pueblos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pueblos.object', {
#             'object': obj
#         })
