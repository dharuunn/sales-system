from flask import Flask, request, redirect, url_for, render_template_string
app = Flask(__name__)
sales = []
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sales System - {{ version }}</title>
</head>
<body>
    <h1>Sales System - {{ version }}</h1>

    <form method="POST" action="/add">
        <input name="product" placeholder="Product name" required>
        <input name="quantity" type="number" min="1"
               placeholder="Quantity" required>
        <input name="price" type="number" min="0.01" step="0.01"
               placeholder="Price per item" required>
        <button type="submit">Add Sale</button>
    </form>

    {% if version in ['v2', 'v3'] %}
    <h2>Sales Records</h2>
    {% for sale in sales %}
        <p>{{ sale.product }} | Quantity: {{ sale.quantity }}
        | Price: {{ "%.2f"|format(sale.price) }}</p>
    {% endfor %}
    {% endif %}

    {% if version == 'v3' %}
    <h2>Total Revenue: {{ "%.2f"|format(revenue) }}</h2>
    {% endif %}
</body>
</html>
"""
@app.route("/")
def home():
    version = request.args.get("version", "v1")
    if version not in ("v1", "v2", "v3"):
        version = "v1"

    revenue = sum(s["quantity"] * s["price"] for s in sales)

    return render_template_string(
        HTML, version=version, sales=sales, revenue=revenue
    )
@app.route("/add", methods=["POST"])
def add_sale():
    sales.append({
        "product": request.form["product"],
        "quantity": int(request.form["quantity"]),
        "price": float(request.form["price"])
    })
    version = request.args.get("version", "v1")
    return redirect(url_for("home", version=version))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
