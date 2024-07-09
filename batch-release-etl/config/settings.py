# """
# ░█▀▀░█▀▀░▀█▀░▀█▀░▀█▀░█▀█░█▀▀░█▀▀
# ░▀▀█░█▀▀░░█░░░█░░░█░░█░█░█░█░▀▀█
# ░▀▀▀░▀▀▀░░▀░░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀
# """

# from scripts.libs import *
import os
from dotenv import load_dotenv

root_path = os.path.dirname(os.getcwd())
file_env = f'{root_path}/batch-release-etl/environments/.env'
load_dotenv(dotenv_path=file_env)

URL_API = os.getenv('URL_API')
API_KEY = os.getenv('API_GOOGLE_KEY')
AIR_QUALITY_API = os.getenv('AIR_QUALITY_API')
URL_OPENWEATHERMAP_API = os.getenv('URL_OPENWEATHERMAP_API')
API_OPENWEATHERMAP_KEY = os.getenv('API_OPENWEATHERMAP_KEY')
