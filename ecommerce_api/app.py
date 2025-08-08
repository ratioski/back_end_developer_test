from flask import Flask
from routes.products import products_bp

app = Flask(__name__)

app.register_blueprint(products_bp, url_prefix="/products")

@app.route("/")
def index():
    return "E-commerce Product API (Flask)"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
