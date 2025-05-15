from flask import Flask, request, send_file, render_template
import csv
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")

    if email:
        with open("emails.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([email])

        if os.path.exists("resume.pdf"):
            return send_file("resume.pdf", as_attachment=True)
        else:
            return "Resume file not found!", 404

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
