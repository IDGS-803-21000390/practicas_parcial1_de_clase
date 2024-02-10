from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField


class Res(Form):
    opcionesColor=[
        ('0','Negro'),
        ('1','Café'),
        ('2','Rojo'),
        ('3','Naranja'),
        ('4','Amarillo'),
        ('5','Verde'),
        ('6','Azul'),
        ('7','Violeta'),
        ('8','Gris'),
        ('9','Blanco')

    ]
    opcionesColor2=[
        ('1','Negro'),
        ('10','Café'),
        ('100','Rojo'),
        ('1000','Naranja'),
        ('10000','Amarillo'),
        ('100000','Verde'),
        ('1000000','Azul'),
        ('10000000','Violeta'),
        ('100000000','Gris'),
        ('1000000000','Blanco')

    ]
    toleraciaValores=[
        ('5%','Dorado'),
        ('10%','Plata')
    ]
    color1=SelectField('Color1',choices=opcionesColor)
    color2=SelectField('Color2',choices=opcionesColor)
    color3=SelectField('Color3',choices=opcionesColor2)
    tolerancia=RadioField('Tolerancia',choices=toleraciaValores)