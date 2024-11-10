# Import
from flask import Flask, render_template, request 



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


#FORMULARIO
@app.route('/submit', methods=['POST'])
def submit_form():
    
    email = request.form['email']
    comment = request.form['comment']

    with open('form.txt', 'a',) as f:
        f.write(f"Correo electrónico: {email} \n")
        f.write(f"Fecha: {comment} \n")
            
    
    return render_template('form_result.html', 
                           
                           email=email,
                           comment=comment,
                           )

if __name__ == "__main__":
    app.run(debug=True)
