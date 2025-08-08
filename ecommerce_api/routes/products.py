import json
import os
from flask import Blueprint, request, jsonify

products_bp = Blueprint("products", __name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")

def read_products():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_products(products):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2)

# GET /products (optional ?category=)
@products_bp.route("/", methods=["GET"])
def get_products():
    products = read_products()
    category = request.args.get("category")
    if category:
        products = [p for p in products if p["category"].lower() == category.lower()]
    return jsonify(products)

# GET /products/<id>
@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    products = read_products()
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

# POST /products
@products_bp.route("/", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data or "name" not in data or not isinstance(data["name"], str) or not data["name"].strip():
        return jsonify({"error": "name is required and must be a non-empty string"}), 400

    if "price" not in data or not isinstance(data["price"], (int, float)) or data["price"] <= 0:
        return jsonify({"error": "price is required and must be a number > 0"}), 400

    if "category" not in data or not isinstance(data["category"], str):
        return jsonify({"error": "category is required and must be a string"}), 400

    products = read_products()
    new_id = max(p["id"] for p in products) + 1 if products else 1

    new_product = {
        "id": new_id,
        "name": data["name"].strip(),
        "price": data["price"],
        "category": data["category"].strip(),
        "description": data.get("description", "")
    }
    products.append(new_product)
    write_products(products)

    return jsonify(new_product), 201
