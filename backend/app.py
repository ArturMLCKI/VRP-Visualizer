from flask import Flask, request, render_template

app = Flask(__name__, template_folder="../frontend")


@app.route("/", methods=["GET", "POST"])
def home():

    x = 53.342686
    y = -6.267118
    address = "Dublin Castle"


    if request.method == "POST":
    
        try:
            address = request.form["address"]
            x = float(f"{float(request.form['x']):.3f}")
            y = float(f"{float(request.form['y']):.3f}")
        except ValueError:
            return "Invalid input values", 400


    return render_template(
        "home.html",
        x=x,
        y=y,
        address=address
    )


if __name__ == "__main__":
    app.run(debug=True)