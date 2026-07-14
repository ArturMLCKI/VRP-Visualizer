from flask import Flask, request, render_template

app = Flask(__name__, template_folder="../frontend")


@app.route("/", methods=["GET", "POST"])
def home():

    start_x = 53.342686
    start_y = -6.267118
    start_address = "Dublin Castle"

    destination_x = 53.349805
    destination_y = -6.260310
    destination_address = "Trinity College Dublin"

    if request.method == "POST":

        try:
            start_address = request.form["start_address"]
            start_x = round(float(request.form["start_x"]), 3)
            start_y = round(float(request.form["start_y"]), 3)

            destination_address = request.form["destination_address"]
            destination_x = round(float(request.form["destination_x"]), 3)
            destination_y = round(float(request.form["destination_y"]), 3)

        except ValueError:
            return "Invalid input values", 400

    return render_template(
        "home.html",
        start_x=start_x,
        start_y=start_y,
        start_address=start_address,
        destination_x=destination_x,
        destination_y=destination_y,
        destination_address=destination_address
    )


if __name__ == "__main__":
    app.run(debug=True)