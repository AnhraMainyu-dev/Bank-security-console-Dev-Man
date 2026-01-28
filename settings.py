import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL',
        conn_max_age=600
    )
}
INSTALLED_APPS = ['datacenter']
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
