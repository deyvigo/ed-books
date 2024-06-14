from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".enviromentvars")

class Config():
  JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class DevelopmentConfig(Config):
  DEBUG = True

config = {
  "development": DevelopmentConfig
}
