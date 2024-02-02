# config/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'your_database_url_here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'
    JWT_EXPIRATION_HOURS = 24  # Set the expiration time for JWT tokens
