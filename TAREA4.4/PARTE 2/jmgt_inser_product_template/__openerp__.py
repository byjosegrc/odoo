# -*. coding: utf-8 -*.

{
    'name': 'Nombre del modulo',
    'version': '1.0',
    'author': ['Jose Manuel Garcia Trave'],
    'category': 'Acco',
    'summary': 'Ejemplo de un modulo de Odoo',
    #'website': 'https:/'
    'description': """
    Ejemplo de Hola mundo.
    =======================
    """,
    'depends': ['base'],
    'data': [
        'jmgthelloword_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}