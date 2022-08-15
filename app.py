from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def inicio():
    return Response("Hola", status=200)    

if __name__ == '__main__':
    app.run()