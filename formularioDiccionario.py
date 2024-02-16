from wtforms import Form
from wtforms import StringField,RadioField
from wtforms import validators

class datos(Form):
    pIngles = StringField('Palabra en ingles', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=2, max=30, message='Ingresa una palabra válida')
    ])
    pEspanol = StringField('Palabra en Español', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=2, max=30, message='Ingresa una palabra válida')
    ])

class datos2(Form):
    palabraB = StringField('Palabra a buscar', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=2, max=30, message='Ingresa una palabra válida')
    ])
    elecionIdioma = RadioField('Seleciona el idioma a buscar', choices=[('Ingles', 'Ingles'), ('Español', 'Español')])
