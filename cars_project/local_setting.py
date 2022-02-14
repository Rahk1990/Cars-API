#  SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%lelgu$+cqlh8xgo(ln%@gvm^sybde+ugfp&f$x--dp+!y5@ih'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '199028aA'

    }
}


