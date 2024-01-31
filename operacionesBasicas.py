from flask import Flask,render_template,request
import formularioDistancia as forms 
from math import sqrt

app=Flask(__name__)

@app.route("/formulario")
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
    
#especificar el metodo que va a arrancar la aplicacion 
if __name__=="__main__":
    app.run(debug=True) 