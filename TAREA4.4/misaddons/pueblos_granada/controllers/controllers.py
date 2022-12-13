# -*- coding: utf-8 -*-
# from odoo import http


# class PueblosGranada(http.Controller):
#     @http.route('/pueblos_granada/pueblos_granada/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pueblos_granada/pueblos_granada/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pueblos_granada.listing', {
#             'root': '/pueblos_granada/pueblos_granada',
#             'objects': http.request.env['pueblos_granada.pueblos_granada'].search([]),
#         })

#     @http.route('/pueblos_granada/pueblos_granada/objects/<model("pueblos_granada.pueblos_granada"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pueblos_granada.object', {
#             'object': obj
#         })
