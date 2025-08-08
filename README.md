# 📄 E-commerce Product API (Flask)

A simple e-commerce product API built with Flask, using a JSON file for storage.

---

## 📌 Tech Stack

- **Language:** Python 3.x
- **Framework:** Flask
- **Storage:** JSON file (`data/products.json`)

---

## 🚀 Installation & Running

### 1. Clone or Download the Project

Project structure:
```
ecommerce_api/
│
├── app.py
├── routes/
│   └── products.py
├── data/
│   └── products.json
├── requirements.txt
└── README.md
```

### 2. Install Dependencies


pip install -r requirements.txt


### 3. Start the Server


python app.py


By default, the API will be available at:  
`http://localhost:5000`

---

## 📂 API Endpoints

### 1️⃣ Get All Products

**GET** `/products/`  
Returns all products.

**Example (PowerShell):**

Invoke-RestMethod -Uri "http://localhost:5000/products/" -Method Get


---

### 2️⃣ Filter Products by Category

**GET** `/products/?category=Apparel`  
Filters products by category (case-insensitive).

**Example (PowerShell):**

Invoke-RestMethod -Uri "http://localhost:5000/products/?category=Apparel" -Method Get


---

### 3️⃣ Get Product by ID

**GET** `/products/<id>`  
Returns a single product by ID.

**Example (PowerShell):**

Invoke-RestMethod -Uri "http://localhost:5000/products/1" -Method Get


---

### 4️⃣ Create a New Product

**POST** `/products/`  
Creates a new product (requires valid JSON body).

**Required Fields:**
- `name` (string, non-empty)
- `price` (number > 0)
- `category` (string)
- `description` (string, optional)

**Example (PowerShell):**

Invoke-RestMethod -Uri "http://localhost:5000/products/" `
  -Method Post `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"name":"New Hat","price":12.5,"category":"Apparel","description":"Nice hat"}'


**Expected Response (`201 Created`):**

{
  "id": 4,
  "name": "New Hat",
  "price": 12.5,
  "category": "Apparel",
  "description": "Nice hat"
}


---

## 🛠 Notes

- Data is stored in `data/products.json`.
- Each POST request appends a new product to the JSON file.
- For production, replace JSON file storage with a real database.
- Server runs in debug mode for development.

---

```

Let me know if you want any additional sections or formatting!
