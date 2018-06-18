from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "Hello World"
    if request.method =="POST":
        name=request.form['name']
        greet =request.form['greet']
        greeting=f"{greet},{name}"
        return render_template("index.html",greeting=greeting)
    else:
        return render_template("hello_form.html")
if__name__ == "__main__":
    app.run()

