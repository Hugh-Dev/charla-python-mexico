# """
# ░█▀▀░█▀▀░▀█▀░▀█▀░▀█▀░█▀█░█▀▀░█▀▀
# ░▀▀█░█▀▀░░█░░░█░░░█░░█░█░█░█░▀▀█
# ░▀▀▀░▀▀▀░░▀░░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀
# """

from scripts.libs import *

file_env = '/Users/psf/Projects/pylab/charla-python-mexico/batch-release-etl/environments/.env'
load_dotenv(dotenv_path=file_env)

URL_API = os.getenv('URL_API')
API_KEY = os.getenv('API_GOOGLE_KEY')
AIR_QUALITY_API = os.getenv('AIR_QUALITY_API')