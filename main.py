from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
import os
import uuid

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

file_save_location = "static/images"
allowed_types = [".png", ".jpg"]

@app.route("/", methods =["GET"])
def index():
    if "GamingCars" not in session:
        print("Clearing the list")
        session["GamingCars"] = []
    
    print(session.get("GamingCars"))
    return render_template("index.html", cars=session.get("GamingCars"), file_location=file_save_location)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        if "GamingCars" not in session:
            print("Clearing data from the session")
            session["GamingCars"] = []
        brand = request.form.get("brand", "invalid")
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
                session["GamingCars"].append({"brand": brand, "car": car, "year": year, "image": car_image})
            else:
                flash("This file is of the wrong type", "error")
                return redirect("./add")
        

        print(session.get("GamingCars"))
        session.modified = True
        flash("Car successfully added to the list.", "message")
        return redirect("/")

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")