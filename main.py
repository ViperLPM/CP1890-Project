from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
import os
import uuid

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

file_save_location = ".static/Images"
allowed_types = [".png", ".jpg", ".webp"]

@app.route("/", methods =["GET"])
def index():
    if "cars" not in session:
        print("Clearing the list")
        session["cars"] = []
    
    print(session.get("cars"))
    return render_template("index.html", cars=session.get("GamingCars"), file_location=file_save_location)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        if "cars" not in session:
            print("Clearing data from the session")
            session["cars"] = []
        car = request.form.get("car", "invalid")
        year = request.form.get("year", "invalid")
        game = request.form.get("game", "invalid")
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            extension = os.path.splitext(uploaded_file.filename)[1]
            if extension in allowed_types:
                car_image = f"{uuid.uuid4().hex}{extension}"
                filename = os.path.join(file_save_location, car_image)
                uploaded_file.save(filename)
                session["cars"].append({"car": car, "year": year, "game": game, "image": car_image})
            else:
                flash("This file is of the wrong type", "error")
                return redirect("./add")
        

        print(session.get("cars"))
        session.modified = True
        flash("Car successfully added to the list.", "message")
        return redirect("/")
    
@app.route('/display')
def display():
    print(session)
    return render_template('display.html', cars=session.get("cars", []), file_location=file_save_location)

@app.route('/remove')
def remove():
    if request.method == "GET":
        return render_template("remove.html")
    elif request.method == "POST":
        if "cars" not in session:
            print("Clearing data from the session")
            session["cars"] = []
        car = request.form.get("car", "invalid")
        if "cars" in session:
            for car in session:
                session["cars"].remove({"car": car})
        else:
            flash("This file is of the wrong type", "error")
            return redirect("./remove")

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")