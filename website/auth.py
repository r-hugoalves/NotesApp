from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<h1> Logout </h1>"

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        if len(email) <4:
            flash("E-mail must be greater than 4 characters!", category="error")
        elif len(firstName) <1:
            flash("First Name must be greater than 1 character!", category="error")
        elif password1 != password2:
            flash("Passwords don't match!", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters!", category="error")
        else:
            # Add User to the Database
            flash("Account created!", category="success")
            
    return render_template("signup.html")