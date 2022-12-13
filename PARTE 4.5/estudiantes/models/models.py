# -*- coding: utf-8 -*-

from odoo import models, fields, api


#class estudiantes(models.Model):
#     _name = 'estudiantes.estudiantes'
#     _description = 'estudiantes.estudiantes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# ---------------------------------------------------------------------

# PRIMERA CLASE:

class asignaturas(models.Model):
     _name = 'estudiantes.asignaturas'
     _description = 'estudiantes.asignaturas'


     #NOMBRE ASIGNATURA:

     nombreAsign = fields.Selection(selection=[("1dam","1DAM"),("2dam","2DAM"),("1daw","1DAW"),("2daw","2DAW")])

     #CODIGO: 

     codigoAsig = fields.Integer(requiered=True,string="Codigo Asignatura",size=4)
     

     #GENTE EN LA ASIGNATURA:

     genteClase = fields.Integer(default=23)

     #HORAS DE CLASE A LA SEMANA:

     horasclase = fields.Integer(default=10)

     #NOMBRE DEL PROFESOR QUE DA LA ASIGNATURA:

     nombreProfesor = fields.Char(help="Codigo Asignatura")



 




# ---------------------------------------------------------------------


# SEGUNDA CLASE:

class sobreti(models.Model):
     _name = 'estudiantes.sobreti'
     _description = 'estudiantes.sobreti'

     #TU NOMBRE: 

     tuNombre = fields.Char(requiered=True,string="Tu nombre es?")

     tuApellido = fields.Char(requiered=True,string="Tu apellido es?")


     #AFICIONES:

     aficion = fields.Char(requiered=True,string="Aficiones que te gusta",size=25)

     #TU EDAD:

     tuEdad = fields.Integer(string="Tu edad")

     #ERES INFORMATICO:

     eresInformatico = fields.Char(help="Si estudio en DAM")

     #EDAD MINIMA:

     edadMinima = fields.Integer(default=18)


     # ---------------------------------------------------------------------


     # TERCERA CLASE:

class mascotas(models.Model):
     _name = 'estudiantes.mascotas'
     _description = 'estudiantes.mascotas'

     #TU NOMBRE:
     
     tuNombre = fields.Char(requiered=True,string="Tu nombre es?")
     

     tuApellido = fields.Char(requiered=True,string="Tu apellido es?")

     #TIENES ANIMALES:

     mascota = fields.Char(help="Si tengo")

     #NOMBRE DE TU MASCOTA

     mascotaNombre = fields.Char(string="Nombre de tu mascota",size=15)

     #NUMERO DE MASCOTAS:

     numeroMascotas = fields.Integer(default=1)

     #QUE ANIMAL ES TU FAVORITO

     favorito = fields.Char(string="Tu mascota favorita")


         # ---------------------------------------------------------------------