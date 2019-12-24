from flask import Flask, url_for, redirect, render_template, request
from time import strptime
from re import match

app=Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def registration():
	if request.method == "GET":
		return render_template("student.html", msg="Enter All Registration Information")

	if request.method == "POST":
		
		if request.form["usn"]=="" or request.form["dob"]=="":
			return render_template("student.html", msg="You didn't fill all the info, enter again")
		
		try:
			strptime(request.form["dob"], "%d/%m/%Y")
		except ValueError:
			return render_template("student.html", msg="Invalid DOB")

		pattern = "^[1][M][S][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
		if not match(pattern, request.form["usn"]):
			return render_template("student.html", msg="Invalid USN")

		return render_template("success.html", data=[request.form["usn"], request.form["dob"]])

if __name__=="__main__":
	app.run(host="127.0.0.1", port="8080", debug=True)
