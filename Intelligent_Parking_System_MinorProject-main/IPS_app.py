from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from Backend.vehicle_count import VehicleCount
import random
import os

app = Flask(__name__)
app.secret_key = "secret key"

# ----------------- Database Configuration -----------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "parking.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ----------------- Models -----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, fname, email, password):
        self.fname = fname
        self.email = email
        self.password = password


# ----------------- Routes -----------------

@app.route('/')
def home_page():
    return render_template('Index.html')


@app.route('/user')
def user():
    return render_template('Customer/login_page/user.html')


@app.route('/user_form', methods=["GET", "POST"])
def user_signup():
    if request.method == 'POST':
        fname = request.form.get('fname')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("User already exists. Please login.", "warning")
            return redirect(url_for('user_login'))

        # Add new user
        new_user = User(fname, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for('home_page'))
    return render_template('Customer/login_page/user.html')


@app.route('/user/login', methods=["GET", "POST"])
def user_login():
    error_message = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            flash("Login successful!", "success")
            return redirect(url_for('home_page'))
        else:
            flash("Invalid email or password.", "danger")
    return render_template('Customer/login_page/user.html')


# ----------------- Initialize DB -----------------
with app.app_context():
    db.create_all()


# ----------------- Run Server -----------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

