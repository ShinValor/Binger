from dotenv import load_dotenv
import os

class Config:
    SECRET_KEY = os.urandom(16)
    
