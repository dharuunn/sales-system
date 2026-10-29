
from flask import Flask, request, render_template_string

app = Flask(__name__)
sales = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sales System v1</title>
</head>
<body>
    <h1>Sales System - v1</h1>
    <h2>Add Sale</h2>

    <form method="POST">
        <input name="product" placeholder="Product name" required>
        <input name="quantity" type="number" min="1"
               placeholder="Quantity" required>
        <input name="price" type="number" min="0.01" step="0.01"
               placeholder="Price per item" required>
        <button type="submit">Add Sale</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        sales.append({
            "product": request.form["product"],
            "quantity": int(request.form["quantity"]),
            "price": float(request.form["price"])
        })
        message = "Sale recorded successfully!"

    return render_template_string(HTML, message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
