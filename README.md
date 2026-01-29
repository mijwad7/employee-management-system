# Employee Management System (EMS)

A full-stack Employee Management module built with **Python (Django)** and **Django REST Framework (DRF)**. This project features a dynamic form builder, JWT authentication, and a complete AJAX-integrated frontend.

## 🚀 Technical Highlights


**Dynamic Form Builder**: Users can define custom fields (Text, Number, Date) to build and edit employee forms dynamically.


**JWT Authentication**: Secure access using JSON Web Tokens (Access & Refresh tokens).


**AJAX Integration**: All form submissions and record management are handled via **Axios/AJAX**, bypassing standard Django form actions as required.


**Advanced Filtering**: Search functionality that filters records based on both standard fields and dynamic field labels.


**Drag-and-Drop**: Logic implemented to allow the reordering of form sections.



---

## 🛠️ Technology Stack

**Backend**: Python 3.x, Django 5.x.


**API**: Django REST Framework (DRF), SimpleJWT.


**Frontend**: HTML5, CSS3, JavaScript (Axios for API calls).


**Database**: SQLite (default) / PostgreSQL.

---

## 📖 API Documentation

The complete API documentation, including request/response examples and endpoint descriptions, is available at the link below:

👉 **[View Postman Documentation](https://documenter.getpostman.com/view/38847192/2sBXVo8TMD)**

---

## ⚙️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mijwad7/employee-management-system.git
cd employee-management-system

```

### 2. Setup Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py createsuperuser  # Create an admin account
python manage.py runserver

```

The application will be available at `http://127.0.0.1:8000/`.

---

## 🧪 Testing with Postman

1. Import the provided `collection.json` located in the root directory into Postman.
2. Set the `base_url` variable to `http://127.0.0.1:8000`.
3. Use the **Register** and **Login** endpoints to obtain a JWT token.
4. Apply the token in the **Authorization** tab (Bearer Token) to test protected Employee CRUD endpoints.
