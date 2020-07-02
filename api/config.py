import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.urandom(16)
    
