from odoo import models,fields

class Pais(models.Model):

    _name = "paises.pais"
    name = fields.Char("Pais")
    capital = fields.Char("Capital")
    continente = fields.Selection(selection=[("africa","Africa"),("asia","Asia"),("europa","Europa"),("america","America")])