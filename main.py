from flask import Flask,render_template,request
import formularioDistancia as forms 
import claseResistencia as f
from math import sqrt

app=Flask(__name__)

@app.route("/operaciones")
def formulario():
    return render_template("formulario.html")

@app.route("/cine")
def cine():
    return render_template("cine.html")

@app.route("/respuestas",methods=["GET","POST"])
def r():
    if request.method=="POST":
        n=request.form.get("nombre")
        CB=int(request.form.get("cantidadBoletos"))
        TC=request.form.get("tarjetaCine")
        TP=CB*12
        TPD=0
        p=int(request.form.get("cantidadCompradores"))
        limiteB=7
        limiteBT=limiteB*p
       
        if CB<= limiteBT:
            if CB >5:
                TPD=TP-(TP*0.15)
            elif CB <= 5 and CB >= 3:
                 TPD=TP-(TP*0.10)
            else:
                TPD=TP    
            if TC == "si":
                TPD=TPD-(TPD*0.10)
            return  render_template('cine.html', valor_a_pagar=TPD,nombre=n,cantidad=CB)
        else:
            return  render_template('cine.html', alerta="No puedes comprar {}, solo {}".format(CB,limiteBT))


@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        operacion=request.form.get("op")
        if operacion=="s":
            return  f'<h1>La suma es: {str(int(num1) + int(num2))} </h1>'
        elif operacion=="r":
            return  f'<h1>La resta es: {str(int(num1) - int(num2))} </h1>'
        elif operacion=="m":
            return  f'<h1>La multiplicacion es: {str(int(num1) * int(num2))} </h1>'
        else:
            return  f'<h1>La divicion es: {str(int(num1) / int(num2))} </h1>'

@app.route("/distancia",methods=["GET","POST"])
def distancia():
    puntos_form=forms.Puntos(request.form)
    res=0
    if request.method=='POST':
        X1=puntos_form.X1.data
        Y1=puntos_form.Y1.data
        X2=puntos_form.X2.data
        Y2=puntos_form.Y2.data
        res=int(sqrt(pow((X2-X1),2)+pow((Y2-Y1),2)))
    return render_template("vistaDistancia.html",form=puntos_form,R=res)   

@app.route("/resistencia",methods=["GET","POST"])
def formularioResistencia():
    resistencia_datos=f.Res(request.form)
    c1=''
    c2=''
    c3=''
    t=''
    c=''
    cc=0
    tma=0.0
    tmi=0.0
    n1=''
    n2=''
    n3=''
    col1=''
    col2=''
    col3=""
    col4=""
    if request.method=='POST':
        c1=resistencia_datos.color1.data
        n1,col1 = nombreColor(c1)
        c2=resistencia_datos.color2.data
        n2,col2=nombreColor(c2)
        c3=resistencia_datos.color3.data
        n3,col3=nombreColor2(c3)
        c3=int(c3)
        t=resistencia_datos.tolerancia.data
        c=int(str(c1) + str(c2))
        cc=c*int(c3)
        if t== '5%':
           tma=cc+(cc*0.05)
           tmi=cc-(cc*0.05)
           t="Dorado 5%"
           col4="#F7DC6F"
        else:
            tma=cc+(cc*0.10)
            tmi=cc-(cc*0.10)
            t="Plata 10%" 
            col4="#ABB2B9"
        
    return render_template("vistaResistencia.html",form=resistencia_datos,c1=n1,c2=n2,c3=n3,t=t,v=cc,tma=tma,tmi=tmi,color=col1,color2=col2,color3=col3,color4=col4)



def nombreColor(opcion):
    if opcion == '0':
        nombre_color_seleccionado = "Negro"
        color="#000000"
    elif opcion == '1':
        nombre_color_seleccionado = "Café"
        color="#EB984E"
    elif opcion == '2':
        nombre_color_seleccionado = 'Rojo'
        color="#E52916"
    elif opcion == '3':
        nombre_color_seleccionado = 'Naranja'
        color="#F37F12"
    elif opcion == '4':
        nombre_color_seleccionado = 'Amarillo'
        color="#F3F012"
    elif opcion == '5':
        nombre_color_seleccionado = 'Verde'
        color="#94F312"
    elif opcion == '6':
        nombre_color_seleccionado = 'Azul  '
        color="#12C3F3"
    elif opcion == '7':
        nombre_color_seleccionado ='Violeta'
        color="#E212F3"
    elif opcion == '8':
        nombre_color_seleccionado = 'Gris'
        color="#B5AEB6"
    else:
        nombre_color_seleccionado = 'Blanco'
        color="#FDFEFE"
    return nombre_color_seleccionado,color

def nombreColor2(opcion):
    if opcion == '1':
        nombre_color_seleccionado = "Negro"
        color="#000000"
    elif opcion == '10':
        nombre_color_seleccionado = "Café"
        color="#EB984E"
    elif opcion == '100':
        nombre_color_seleccionado = 'Rojo'
        color="#E52916"
    elif opcion == '1000':
        nombre_color_seleccionado = 'Naranja'
        color="#F37F12"
    elif opcion == '1000':
        nombre_color_seleccionado = 'Amarillo'
        color="#F3F012"
    elif opcion == '100000':
        nombre_color_seleccionado = 'Verde'
        color="#94F312"
    elif opcion == '1000000':
        nombre_color_seleccionado = 'Azul  '
        color="#12C3F3"
    elif opcion == '10000000':
        nombre_color_seleccionado ='Violeta'
        color="#E212F3"
    elif opcion == '100000000':
        nombre_color_seleccionado = 'Gris'
        color="#B5AEB6"
    else:
        nombre_color_seleccionado = 'Blanco'
        color="#FDFEFE"
    return nombre_color_seleccionado,color

    
#especificar el metodo que va a arrancar la aplicacion 
if __name__=="__main__":
    app.run(debug=True) 