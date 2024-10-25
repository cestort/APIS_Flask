from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    texto_entrante = ""
    if request.method == 'POST':
        texto_entrante = request.form['texto_entrante']

    return render_template('landing.html', texto_entrante=texto_entrante)


if __name__ == '__main__':
    app.run(debug=True)
