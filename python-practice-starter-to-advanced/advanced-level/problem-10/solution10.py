from dotenv import load_dotenv
import os

def load_env_file(path=".env"):
    """
    Loads environment variables from a .env file using python-dotenv.
    """
    load_dotenv(dotenv_path=path)
    print("Environment variables loaded.")