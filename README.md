# Shortly - A Simple URL Shortener with Django
Shortly is a minimalist URL shortener built using **Django**, allowing users to input long URLs and receive unique, shortened links they can share easily.

## Features
- Unique short codes generated for each URL
- Shortened URLs redirect to the original destination
- Clean UI using TailwindCSS

## Setup Instructions (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/shortly.git
cd shortly
```

### 2. Create a Virtual Environment (recommended)

```bash
python -m venv env
```

### 3. Activate it:

- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

- On Windows:
  ```bash
  env\Scripts\activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
cd urlproject
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and visit: http://localhost:8000