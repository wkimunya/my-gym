# app/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gym.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_for_jwt'  # Change this to a random secret key
