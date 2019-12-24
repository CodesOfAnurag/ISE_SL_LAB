from flask import Flask, session, redirect, request, url_for, render_template

app=Flask(__name__)
app.secret_key="Secret"

@app.route("/", methods=["GET", "POST"])
def atm():
	if 'balance' not in session and 'count' not in session:
		session['balance']=8000
		session['count']=0

	if request.method=="GET":
		return render_template("atm.html", balance=session['balance'], msg="Enter Amount and Select Transaction Option")

	if request.method=="POST":
		if request.form['action']=="Exit":
			session.clear()
			return redirect(url_for("atm"))

		if request.form['amt']=="":
			return render_template("atm.html", balance=session['balance'], msg="No Amount Entered")
		
		if int(request.form['amt'])<0:
			return render_template("atm.html", balance=session['balance'], msg="Negative Amount Entered")
		
		if session['count']==5:
			return render_template("atm.html", balance=session['balance'], msg="Exceeded maximum nnumber of transaction")	

		if request.form['action']=="Withdraw":
			if int(request.form['amt'])>5000:
				return render_template("atm.html", balance=session['balance'], msg="Withdrawal Limit Exceeded")
			elif int(request.form['amt'])>session['balance']:
				return render_template("atm.html", balance=session['balance'], msg="Insufficient Balance")
			else:
				session['count']+=1
				session['balance']-=int(request.form['amt'])
				return render_template("atm.html", balance=session['balance'], msg=request.form['amt']+" Withdrawn")

		if request.form['action']=="Deposit":
			if int(request.form['amt'])>50000:
				return render_template("atm.html", balance=session['balance'], msg="Deposit Limit Exceeded")
			else:
				session['count']+=1
				session['balance']+=int(request.form['amt'])
				return render_template("atm.html", balance=session['balance'], msg=request.form['amt']+" Deposited")

if __name__=="__main__":
	app.run(debug=True)