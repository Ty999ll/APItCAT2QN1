import requests

BASE_URL = "http://127.0.0.1:5000"

def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(f"{BASE_URL}/products", json=payload)

    if response.status_code == 201:
        print("Product added successfully!")
        print(response.json())
    else:
        print("Failed to add product.")
        print(response.json())


def get_products():
    response = requests.get(f"{BASE_URL}/products")

    if response.status_code == 200:
        print("Products retrieved successfully:")
        for product in response.json():
            print(product)
    else:
        print("Failed to retrieve products.")
        print(response.json())


if __name__ == "__main__":
    print("Adding a new product...")
    add_product("Laptop", "A high-performance laptop", 1500.00)

    print("\nRetrieving all products...")
    get_products()
