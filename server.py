from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key="topsecret"


@app.route('/', methods=['GET'])
def pagPrincipal():
    if "random" not in session:
        session["random"] = random.randint(1, 100)

    if "oportunidades" not in session:
        session["oportunidades"] = 0
    else:
        session["oportunidades"] += 1        
    return render_template("index.html")


@app.route('/intento', methods=['POST'])
def intentos():
    session['intentalo'] = int(request.form['intentalo'])
    
    return redirect('/')

#@app.route('/numerodevecesintentando', methods=['POST'])
#def num_intentos():
#    if "oportunidades" not in session:
#        session["oportunidades"] = 0
#    else:
#        session["oportunidades"] += 1        
#    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run( debug=True )


