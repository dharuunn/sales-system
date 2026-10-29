
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
sales = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sales System v2</title>
</head>
<body>
    <h1>Sales System - v2</h1>

    <h2>Add Sale</h2>
    <form method="POST" action="/add">
        <input name="product" placeholder="Product name" required>
        <input name="quantity" type="number" min="1"
               placeholder="Quantity" required>
        <input name="price" type="number" min="0.01" step="0.01"
               placeholder="Price per item" required>
        <button type="submit">Add Sale</button>
    </form>

    <h2>View Sales</h2>
    {% if sales %}
    <table border="1" cellpadding="8">
        <tr>
            <th>Product</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Subtotal</th>
        </tr>
        {% for sale in sales %}
        <tr>
            <td>{{ sale.product }}</td>
            <td>{{ sale.quantity }}</td>
            <td>{{ "%.2f"|format(sale.price) }}</td>
            <td>{{ "%.2f"|format(sale.quantity * sale.price) }}</td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p>No sales recorded yet.</p>
    {% endif %}
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, sales=sales)


@app.route("/add", methods=["POST"])
def add_sale():
    sales.append({
        "product": request.form["product"],
        "quantity": int(request.form["quantity"]),
        "price": float(request.form["price"])
    })
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
