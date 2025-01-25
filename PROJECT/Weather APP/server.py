from flask import Flask,render_template,request
from app import Get_Weather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "First Flask app"
@app.route

if __name__ == "__main__":
    #app.run(host= "0.0.0.0",port = 8000)
    serve(app, host = "0.0.0.0",port = 8000)