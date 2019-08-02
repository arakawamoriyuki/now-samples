from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def root():
    return Response('hello world')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
