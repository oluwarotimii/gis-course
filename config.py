import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    JUPYTERHUB_API_TOKEN = os.getenv('JUPYTERHUB_API_TOKEN', 'your_jupyterhub_token')
    JUPYTERHUB_URL = os.getenv('JUPYTERHUB_URL', 'http://localhost:8000')
