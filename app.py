from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    app.logger.info(f'Entramos al path {request.path}')
    return 'Hello World desde Flask!'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Hola como estas {nombre}?'

if __name__ == '__main__':
    app.run()
