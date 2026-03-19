# 🏥 Medical Management System

A web-based **Medical Management System** built using **Django** that helps manage patient records, appointments, and basic healthcare workflows. This project is designed for learning, development, and deployment using modern tools like **Vercel**.

---

## 🚀 Features

* 👤 Patient record management
* 📅 Appointment handling
* 🗂️ Organized medical data storage
* ⚙️ Admin panel (Django Admin)
* 🌐 Ready for deployment (Vercel configuration included)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (default)
* **Frontend:** HTML, CSS (Django Templates)
* **Deployment:** Vercel
* **Server:** Gunicorn
* **Static Files:** WhiteNoise

---

## 📁 Project Structure

```
mediBridge/
│
├── medical_sys/
│   ├── manage.py
│   ├── requirements.txt
│   ├── vercel.json
│   ├── build.sh
│   ├── db.sqlite3
│   ├── medical_sys/        # Main Django project
│   └── staticfiles/
│
└── parser.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Start Development Server

```bash
python manage.py runserver
```

Now open 👉 `http://127.0.0.1:8000/`

---

## 🔐 Admin Panel Access

Create a superuser:

```bash
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin/
```

---

## 🌍 Deployment (Vercel)

This project is configured for Vercel deployment using:

* `vercel.json`
* `build.sh`
* `gunicorn`
* `whitenoise`

### Steps:

1. Install Vercel CLI:

```bash
npm install -g vercel
```

2. Deploy:

```bash
vercel
```

---

## ⚠️ Common Issues

### ❌ requirements.txt parsing error

If you see encoding errors:

* Open `requirements.txt`
* Remove unwanted characters (like `��`)
* Save file in **UTF-8 encoding**

---

## 📌 Future Improvements

* Add authentication system (login/signup)
* Improve UI with modern frameworks (React / Tailwind)
* Add doctor dashboard
* Online prescriptions & reports
* API integration

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a Pull Request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

Developed by **[Samarth Choudhar]**

---

link = https://medibridge-l21t.vercel.app/accounts/login/?next=/
