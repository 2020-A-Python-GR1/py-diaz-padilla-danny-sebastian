from flask import Flask, redirect, url_for, request, json, session
from flask import render_template  # cargar html


app = Flask(__name__)


@app.route("/")
def index():
    return "Página principal"


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/home")
def show_home():
    user_data = json.loads(session['user_data'])
    return render_template("home.html", name=user_data["name"])


"""API"""


@app.route('/api/save_user', methods=['POST'])
def parse_request():
    data = request.form
    # TODO: GUARDAR DATOS
    session['user_data'] = json.dumps({"name": data['name']})  # cookie de sesión
    return redirect(url_for('.show_home'))


# valida que corre por primera vez
if __name__ == "__main__":
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.debug = True  # detecta cambios
    app.run()






"""

@app.route("/Hola/")
@app.route("/Hola/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)  # mandar html
    # la variable que se manda responde a lo que esta en codigo
    # jinja en el html que recibe un nombre
    
    
@app.route("/post/<int:post_id>")  # http://127.0.0.1:5000/post/888
def mostrar_post(post_id):
    return "Post %d" % post_id



@app.route("/usuario/<username>")  # redirecciones!,multiples dir
@app.route("/user/<username>")
def mostrar_nombre_perfil(username):
    return "User %s" % username
    
return redirect("http://www.example.com", code=302)

return redirect(url_for('foo'))



def do_baz():
    messages = json.dumps({"main":"Condition failed on page baz"})
    session['messages'] = messages
    return redirect(url_for('.do_foo', messages=messages))

@app.route('/foo')
def do_foo():
    messages = request.args['messages']  # counterpart for url_for()
    messages = session['messages']       # counterpart for session
    return render_template("foo.html", messages=json.loads(messages))
"""
