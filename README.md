📄 README.md — E-commerce Product API (Flask)
📌 Tech Stack
Language: Python 3.x

Framework: Flask

Storage: JSON file (data/products.json)

🚀 Installation & Run
Clone or download the project with the following structure:


ecommerce_api/
│
├── app.py
├── routes/
│   └── products.py
├── data/
│   └── products.json
├── requirements.txt
└── README.md
Install dependencies

pip install -r requirements.txt
Start the server

bash
Copiar
Editar
python app.py
Access the API
By default, it will be available at:

http://localhost:5000
📂 API Endpoints
1️⃣ GET /products/
Returns all products.

PowerShell Example

Invoke-RestMethod -Uri "http://localhost:5000/products/" -Method Get
2️⃣ GET /products/?category=Apparel
Filters products by category (case-insensitive).

PowerShell Example

Invoke-RestMethod -Uri "http://localhost:5000/products/?category=Apparel" -Method Get
3️⃣ GET /products/<id>
Returns a single product by ID.

PowerShell Example

Invoke-RestMethod -Uri "http://localhost:5000/products/1" -Method Get
4️⃣ POST /products/
Creates a new product (requires valid JSON body).

Required fields:

name (string, non-empty)

price (number > 0)

category (string)

description (string, optional)

PowerShell Example

Invoke-RestMethod -Uri "http://localhost:5000/products/" `
  -Method Post `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"name":"New Hat","price":12.5,"category":"Apparel","description":"Nice hat"}'
Expected Response (201 Created):

{
  "id": 4,
  "name": "New Hat",
  "price": 12.5,
  "category": "Apparel",
  "description": "Nice hat"
}
🛠 Notes
Data is stored in data/products.json.

Each POST request appends the new product to the JSON file.

In production, replace JSON file storage with a real database.

Server runs in debug mode for development purposes.
