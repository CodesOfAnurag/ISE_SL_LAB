from flask import Flask, redirect, url_for, render_template, session, request

app=Flask(__name__)
app.secret_key="secret"

@app.route("/", methods=["POST", "GET"])
def total():
	items=["egg", "milk", "bread"]
	total=0

	if request.method=="GET":
		return render_template("calc.html", data=items, cost="Total: "+str(total))

	if request.method=="POST":
		for item in items:
			total+=int(request.form[item+"Cost"])*int(request.form[item+"Qty"])
		return render_template("calc.html", data=items, cost="Total: Rs."+str(total))			


if __name__=="__main__":
	app.run(debug=True)