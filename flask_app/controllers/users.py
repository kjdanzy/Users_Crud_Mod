from flask import Flask, render_template, request, redirect

from flask_app import app  
from flask_app.models.user import User



@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)


@app.route("/<int:id>")
def get_user(id):
    data = {
        'id': id
    }
    user = User.get_user(data)
    return render_template("show.html", user = user)
    
@app.route("/user/new")
def new_user():
    #redirect to create.html
    return render_template("create.html")
            
# relevant code snippet from server.py
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "occupation" : request.form["occupation"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    print("===========")
    print(data)
    print("===========")
    User.create_user(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route("/update_user", methods=["POST"])
def update_user():
    data = {
        "id": int(request.form["id"]),
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "occupation" : request.form["occupation"]
    }
    # We pass the data dictionary into the update method from the User class.
    print("===========")
    print(data)
    print("===========")
    User.update(data)
    return redirect('/')

@app.route("/user/<int:id>/edit")
def edit_user(id):
    data = {
        'id': id
    }
    user = User.get_user(data)
    return render_template("edit.html", user=user)

@app.route("/user/<int:id>/delete")
def delete_user(id):
    data = {
        'id': id
    }
    user = User.delete_user(data)
    return redirect('/')