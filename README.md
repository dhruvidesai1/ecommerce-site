# 🛒 Django eCommerce Website

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Django](https://img.shields.io/badge/django-5.0%2B-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Made with ❤️](https://img.shields.io/badge/Made%20with-Django-092E20.svg)

A web-based eCommerce store built with Django. Features include product listings, detailed views, cart functionality, and a checkout page — all rendered using HTML templates and styled with CSS.

---

## 🚀 Features

- 🛍️ Product listing on the homepage (`index.html`)
- 🔎 Product detail page (`detail.html`)
- 💳 Checkout flow (`checkout.html`)
- 🎨 Custom CSS styling (`static/shop/style.css`)
- 👤 Admin panel to manage products

---

## 🗂️ Project Structure

ecomsite/
├── ecomsite/                 # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/                     # Main app
│   ├── migrations/
│   ├── static/shop/
│   │   └── style.css
│   ├── templates/shop/
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── checkout.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py         
├── db.sqlite3
└── manage.py

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/django-ecommerce-site.git
cd django-ecommerce-site

	2.	Create and activate a virtual environment

python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

	3.	Install dependencies

pip install -r requirements.txt

	4.	Apply migrations

python manage.py migrate

	5.	Create superuser

python manage.py createsuperuser

	6.	Run the server

python manage.py runserver

Visit http://127.0.0.1:8000 to see your site in action.

⸻

🔐 Admin Panel

Visit: http://127.0.0.1:8000/admin/

Manage your product models from here.

⸻

📄 License

This project is licensed under the MIT License.

⸻

👩‍💻 Author

Dhruvi Desai

⸻

🌐 Live Demo (Optional)

Link your Render, Vercel, or Heroku deployment here once live.

---

Let me know if:
- You want to add a `products` model overview
- You want to include screenshots or a GIF demo
- You're planning to add cart logic and need help structuring that

I can also generate your `requirements.txt` from your current env if needed.
