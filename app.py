from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

UNIT_CONVERSIONS = {
    "length": {
        "meters": {"feet": 3.28084, "inches": 39.3701, "centimeters": 100},
        "feet": {"meters": 0.3048, "inches": 12, "centimeters": 30.48},
        "inches": {"meters": 0.0254, "feet": 0.08333, "centimeters": 2.54},
        "centimeters": {"meters": 0.01, "feet": 0.0328084, "inches": 0.393701},
    },
    "weight": {
        "kilograms": {"grams": 1000, "pounds": 2.20462},
        "grams": {"kilograms": 0.001, "pounds": 0.00220462},
        "pounds": {"kilograms": 0.453592, "grams": 453.592},
    },
    "temperature": {
        "celsius": {"fahrenheit": lambda c: c * 9/5 + 32, "kelvin": lambda c: c + 273.15},
        "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9, "kelvin": lambda f: (f + 459.67) * 5/9},
        "kelvin": {"celsius": lambda k: k - 273.15, "fahrenheit": lambda k: k * 9/5 - 459.67},
    },
}

@app.route("/")
def index():
    return render_template("index.html")

def convert_unit(category, value, from_unit, to_unit):
    try:
        value = float(value)
        if from_unit == to_unit:
            return value  # No conversion needed if units are the same
        conversion = UNIT_CONVERSIONS[category][from_unit][to_unit]
        if callable(conversion):
            result = conversion(value)
        else:
            result = value * conversion
        return round(result, 4)
    except (ValueError, KeyError):
        return None

@app.route("/<category>", methods=["GET", "POST"])
def converter(category):
    if category not in UNIT_CONVERSIONS:
        flash("Invalid conversion category", "error")
        return redirect(url_for('index'))

    if request.method == "POST":
        value = request.form.get('value')
        from_unit = request.form.get('from')
        to_unit = request.form.get('to')
        
        result = convert_unit(category, value, from_unit, to_unit)
        
        if result is None:
            flash("Invalid conversion. Please check your input.", "error")
            return redirect(url_for('converter', category=category))
        
        return render_template("result.html", value=value, from_unit=from_unit, to_unit=to_unit, result=result)
    
    return render_template(f"{category}.html", units=UNIT_CONVERSIONS[category].keys())

if __name__ == "__main__":
    app.run(debug=True)