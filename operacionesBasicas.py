from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


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

        
    
#especificar el metodo que va a arrancar la aplicacion 
if __name__=="__main__":
    app.run(debug=True) 