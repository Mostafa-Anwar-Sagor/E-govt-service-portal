from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from os import getcwd, path, makedirs, getenv
from dotenv import load_dotenv
from flask_migrate import Migrate

# Load environment variables
dotenv_path = path.join(path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Ensure the uploads directory exists
cwd = getcwd()
uploads_dir = path.join(cwd, "uploads")
if not path.exists(uploads_dir):
    makedirs(uploads_dir)

# Initialize Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False

# Configuration
app.config["BABEL_DEFAULT_LOCALE"] = "ar"
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "./translations"
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["UPLOAD_DIRECTORY"] = uploads_dir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Ensure all environment variables are properly loaded
# If any variable is missing, log a warning or raise an error for debugging
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
babel = Babel(app)

# Models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(12), primary_key=True)
    password = db.Column(db.String(224))
    name = db.Column(db.String(128))
    phone = db.Column(db.String(16))
    email = db.Column(db.String(48))
    address = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(432))
    readme = db.Column(db.Text)

class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(432))
    readme = db.Column(db.Text)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"),nullable=True)
    department = db.relationship("Department", backref="services")


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(4096))
    file_paths = db.Column(db.String(4096))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    is_done = db.Column(db.Boolean, default=False)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"))
    service = db.relationship("Service", backref="orders")
    user_id = db.Column(db.String(14), db.ForeignKey("users.id"))
    user = db.relationship("User", backref="orders")


# Create tables if running this file directly
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all tables defined in the models
