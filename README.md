# Flask Introduction

A Day 54 project from the 100 Days of Code challenge, demonstrating fundamental concepts of **Flask** web framework and **Python decorators**.

## 📚 Project Overview

This project introduces the basics of building web applications using Flask, a lightweight and flexible web framework for Python. It also includes examples of Python decorators, showcasing how they can be used to modify function behavior.

## 🚀 Features

- **Flask Routes**: Simple HTTP endpoints demonstrating Flask's routing system
  - `/` - Returns a "Hello, World!" message
  - `/bye` - Returns a "Bye, World!" message

- **Python Decorators**: Example implementation of custom decorators
  - `delay_fun` - A decorator that adds a 2-second delay before function execution
  - Demonstrates decorator syntax with `@` notation

## 📁 Project Structure

```
.
├── main.py              # Flask application with basic routes
├── decorator_file.py    # Python decorator examples
├── pyproject.toml       # Project configuration and dependencies
└── README.md           # This file
```

## 🛠️ Requirements

- Python >= 3.12
- Flask >= 3.1.3
- IPython >= 9.15.0
- Markdown >= 3.10.2
- Display >= 1.0.0

## 📦 Installation

This project uses `uv` as the package manager. To install dependencies:

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

### Flask Web Server

To start the Flask development server:

```bash
python main.py
```

The application will be accessible at `http://localhost:5000`

### Decorator Examples

To run the decorator examples:

```bash
python decorator_file.py
```

This will print "hello world" after a 2-second delay.

## 📖 How It Works

### Flask Routes (main.py)

The Flask application creates a simple web server with two endpoints:
- `@app.route("/")` - Maps the root URL to the `hello_world()` function
- `@app.route("/bye")` - Maps `/bye` URL to the `bye_world()` function

### Decorators (decorator_file.py)

The `delay_fun` decorator wraps the `hello_world()` function, adding a 2-second sleep before execution. This demonstrates:
- Decorator syntax using `@`
- How decorators modify function behavior
- Using `*args` and `**kwargs` for flexible argument passing

## 💡 Learning Objectives

- Understand Flask's basic routing and request handling
- Learn how Python decorators work
- Build simple HTTP endpoints
- Explore the relationship between Flask and Python language features

## 📝 License

This is a learning project from the 100 Days of Code challenge.

---

Happy Coding! 🎉
