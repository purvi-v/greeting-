from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ammupuri"
@app.route("/hello")
def index():
	flash("what's your Name")
	return render_template("index.html")

@app.route("/greet",methods=["GET","POST"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
 
if __name__=='__main__':
	app.run(debug=True)

