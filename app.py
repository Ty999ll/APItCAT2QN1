from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ['name', 'description', 'price']):
        return jsonify({"error": "Invalid data"}), 400

    # Add product to the list
    product = {
        "id": len(products) + 1,
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    products.append(product)
    return jsonify({"message": "Product created successfully", "product": product}), 201


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200


if __name__ == '__main__':
    app.run(debug=True)
