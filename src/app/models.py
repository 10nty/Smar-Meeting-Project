from app.auth import hash_password

fake_users_db = {
    "user@example.com": {
        "username": "user@example.com",
        "hashed_password": hash_password("password123")
    }
}
