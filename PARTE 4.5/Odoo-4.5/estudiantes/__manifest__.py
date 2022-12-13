# -*- coding: utf-8 -*-
{
    'name': "estudiantes",

    'summary': """
        Este modulo contiene la imformacion de  los estudiantes del IES AL-ALANDALUS""",

    'description': """
        El proposito de este modulo es contener tanto el nombre de los estudiantes y el curso que estan cursando en el IES AL-ALANDALUS
    """,

    'author': "Jose Manuel Garcia Trave",
    'website': "http://www.josemanuelgt.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/asignaturas.xml',
        'views/sobreti.xml',
        'views/mascotas.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
