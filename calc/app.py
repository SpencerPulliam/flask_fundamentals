import operations
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    return str(operations.add(int(request.args.get('a')), int(request.args.get('b'))))

@app.route('/sub')
def sub():
    return str(operations.sub(int(request.args.get('a')), int(request.args.get('b'))))

@app.route('/mult')
def mult():
    return str(operations.mult(int(request.args.get('a')), int(request.args.get('b'))))

@app.route('/div')
def div():
    return str(operations.div(int(request.args.get('a')), int(request.args.get('b'))))