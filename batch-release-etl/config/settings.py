# """
# ░█▀▀░█▀▀░▀█▀░▀█▀░▀█▀░█▀█░█▀▀░█▀▀
# ░▀▀█░█▀▀░░█░░░█░░░█░░█░█░█░█░▀▀█
# ░▀▀▀░▀▀▀░░▀░░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀
# """

from scripts.libs import *

root_path = os.getcwd()
file_env = f'{root_path}/environments/.env'
load_dotenv(dotenv_path=file_env)

URL_API = os.getenv('URL_API')
API_KEY = os.getenv('API_GOOGLE_KEY')
AIR_QUALITY_API = os.getenv('AIR_QUALITY_API')