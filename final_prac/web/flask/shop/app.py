from flask import Flask, redirect, request, url_for, session, render_template

app=Flask(__name__)
app.secret_key="secret"

items = ['Eggs', "Milk", 'Bread']
cost = dict(zip(items, [12,15,10]))
@app.route("/", methods=["POST", "GET"])
def add():

	if request.method=="GET":
		return render_template("add.html", items=items)

	if request.method=="POST":
		for item in items:
			if item in session:
				session[item]+=int(request.form[item])
			else:
				session[item]=int(request.form[item])

		return redirect(url_for('cart'))
@app.route("/cart", methods=["POST", "GET"])
def cart():
	cartContent=[[item, session[item]] for item in items]
	print(cartContent)
	return render_template("cart.html", cart=cartContent)

@app.route("/bill", methods=["POST", "GET"])
def bill():
	billContent = [[item, session[item], cost[item]] for item in items]
	return render_template("bill.html", bill=billContent)	

@app.route("/", methods=["POST", "GET"])
def logout():
	session.clear()
	return redirect(url_for('add'))

if __name__=='__main__':
	app.run(debug=True)
