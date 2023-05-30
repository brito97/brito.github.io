from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = 'John Doe'
    return render_template('index.html', nome=nome)

if __name__ == '__main__':
    app.run()
