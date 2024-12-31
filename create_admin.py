from models import db, User
from werkzeug.security import generate_password_hash

def create_admin():
    # Prompt for admin user details
    admin_id = input("Enter Admin ID (12-digit): ")
    admin_email = input("Enter Admin Email: ")
    admin_password = input("Enter Admin Password: ")
    admin_name = input("Enter Admin Name: ")
    admin_phone = input("Enter Admin Phone Number: ")
    admin_address = input("Enter Admin Address: ")

    # Check if the admin already exists
    existing_admin = User.query.filter_by(email=admin_email).first()
    if existing_admin:
        print(f"Admin with email {admin_email} already exists!")
        return

    # Hash the password for security
    hashed_password = generate_password_hash(admin_password)

    # Create the admin user
    admin_user = User(
        id=admin_id,
        password=hashed_password,
        name=admin_name,
        phone=admin_phone,
        email=admin_email,
        address=admin_address,
        is_admin=True  # Mark this user as an admin
    )

    # Add and commit the admin user
    db.session.add(admin_user)
    db.session.commit()
    print("New admin user created successfully!")
    print(f"Admin Email: {admin_email}")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        create_admin()
