import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()


DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL',
        conn_max_age=600
    )
}
INSTALLED_APPS = ['datacenter']
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
