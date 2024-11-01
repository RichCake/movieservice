import psycopg2 

DATEBASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movieservice',
        'USER': 'postgres',
        'PASSWORD': '1029',
        'IP': '195.2.73.250',
        'PORT': '5432'
    }
}