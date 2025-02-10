from flask import request, jsonify
from app.services.product_service import ProductService

def add_product_handler(product_service: ProductService):
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'price' not in data or 'seller_id' not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    try:
        product_service.add_product(data['title'], data['description'], data['price'], data['seller_id'])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({"message": "Product added successfully"}), 201


def list_products_handler(product_service: ProductService):
    products = product_service.list_products()
    return jsonify([{
        "title": product.title,
        "description": product.description,
        "price": product.price,
        "seller_id": product.seller_id
    } for product in products]), 200


def delete_product_handler(product_service: ProductService, product_id: int):
    if not product_id:
        return jsonify({"error": "Invalid product ID"}), 400
    
    try:
        product_service.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Error deleting product"}), 400
