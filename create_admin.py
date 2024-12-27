from models import db, User
from werkzeug.security import generate_password_hash

def create_admin():
    # Define admin user details
    admin_id = "123456789012"  # 12-digit ID
    admin_password = "admin123"  # Replace with your desired password
    hashed_password = generate_password_hash(admin_password)
    admin_user = User(
        id=admin_id,
        password=hashed_password,
        name="Admin",
        phone="1234567890",
        email="admin@gmail.com",
        address="Admin Address",
        is_admin=True,  # Mark this user as an admin
    )

    # Add and commit the admin user
    db.session.add(admin_user)
    db.session.commit()
    print("Admin user created successfully!")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        create_admin()
