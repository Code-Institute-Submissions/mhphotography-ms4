{"changed":true,"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","value":"\"\"\"\nDjango settings for ecommerce project.\n\nGenerated by 'django-admin startproject' using Django 1.11.24.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\n#import env\nimport dj_database_url\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = os.environ.get('SECRET_KEY')\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = [\"0b1e701fdf9c47b1afd3ad420befad00.vfs.cloud9.us-east-1.amazonaws.com\"]\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'django_forms_bootstrap',\n    'accounts',\n    'products',\n    'cart',\n    'checkout',\n    'storages',\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'ecommerce.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [os.path.join(BASE_DIR, 'templates')],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n                'django.template.context_processors.media',\n                'cart.contexts.cart_contents',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'ecommerce.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\n\nif \"DATABASE_URL\" in os.environ: \n    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}\nelse:\n    print(\"Database URL not found.  Using SQLite instead\")\n    DATABASES = {\n        'default': {\n            'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n        }\n    }\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\nAUTHENTICATION_BACKENDS = [\n    'django.contrib.auth.backends.ModelBackend',\n    'accounts.backends.CaseInsensitiveAuth']\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nAWS_S3_OBJECT_PARAMETERS = {\n    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',\n    'CacheControl': 'max-age=94608000',\n}\n\nAWS_STORAGE_BUCKET_NAME = 'mhphotography-ms4'\nAWS_S3_REGION_NAME = 'eu-west-1'\nAWS_ACCESS_KEY_ID = os.environ.get(\"AWS_ACCESS_KEY_ID\")\nAWS_SECRET_ACCESS_KEY = os.environ.get(\"AWS_SECRET_ACCESS_KEY\")\n\nAWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME\n\nSTATICFILES_LOCATION = 'static'\nSTATICFILES_STORAGE = 'custom_storages.StaticStorage'\n\nSTATIC_URL = '/static/'\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, \"static\"),\n)\n\nMEDIAFILES_LOCATION = 'media'\nDEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)\n\nSTRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')\nSTRIPE_SECRET = os.getenv('STRIPE_SECRET')\n\nMESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'\n","undoManager":{"mark":99,"position":100,"stack":[[{"start":{"row":144,"column":23},"end":{"row":144,"column":70},"action":"insert","lines":["'%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME"],"id":226}],[{"start":{"row":144,"column":70},"end":{"row":145,"column":0},"action":"insert","lines":["",""],"id":227},{"start":{"row":145,"column":0},"end":{"row":146,"column":0},"action":"insert","lines":["",""]},{"start":{"row":146,"column":0},"end":{"row":146,"column":1},"action":"insert","lines":["S"]},{"start":{"row":146,"column":1},"end":{"row":146,"column":2},"action":"insert","lines":["T"]},{"start":{"row":146,"column":2},"end":{"row":146,"column":3},"action":"insert","lines":["A"]}],[{"start":{"row":146,"column":3},"end":{"row":146,"column":4},"action":"insert","lines":["T"],"id":228}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":4},"action":"remove","lines":["STAT"],"id":229},{"start":{"row":146,"column":0},"end":{"row":146,"column":16},"action":"insert","lines":["STATICFILES_DIRS"]}],[{"start":{"row":146,"column":15},"end":{"row":146,"column":16},"action":"remove","lines":["S"],"id":230},{"start":{"row":146,"column":14},"end":{"row":146,"column":15},"action":"remove","lines":["R"]},{"start":{"row":146,"column":13},"end":{"row":146,"column":14},"action":"remove","lines":["I"]},{"start":{"row":146,"column":12},"end":{"row":146,"column":13},"action":"remove","lines":["D"]}],[{"start":{"row":146,"column":12},"end":{"row":146,"column":13},"action":"insert","lines":["S"],"id":231},{"start":{"row":146,"column":13},"end":{"row":146,"column":14},"action":"insert","lines":["T"]},{"start":{"row":146,"column":14},"end":{"row":146,"column":15},"action":"insert","lines":["O"]},{"start":{"row":146,"column":15},"end":{"row":146,"column":16},"action":"insert","lines":["R"]},{"start":{"row":146,"column":16},"end":{"row":146,"column":17},"action":"insert","lines":["A"]},{"start":{"row":146,"column":17},"end":{"row":146,"column":18},"action":"insert","lines":["G"]},{"start":{"row":146,"column":18},"end":{"row":146,"column":19},"action":"insert","lines":["E"]}],[{"start":{"row":146,"column":19},"end":{"row":146,"column":20},"action":"insert","lines":[" "],"id":232},{"start":{"row":146,"column":20},"end":{"row":146,"column":21},"action":"insert","lines":["="]}],[{"start":{"row":146,"column":21},"end":{"row":146,"column":22},"action":"insert","lines":[" "],"id":233}],[{"start":{"row":146,"column":22},"end":{"row":146,"column":64},"action":"insert","lines":["'storages.backends.s3boto3.S3Boto3Storage'"],"id":234}],[{"start":{"row":145,"column":0},"end":{"row":146,"column":0},"action":"insert","lines":["",""],"id":235}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":1},"action":"insert","lines":["S"],"id":236},{"start":{"row":146,"column":1},"end":{"row":146,"column":2},"action":"insert","lines":["T"]},{"start":{"row":146,"column":2},"end":{"row":146,"column":3},"action":"insert","lines":["A"]},{"start":{"row":146,"column":3},"end":{"row":146,"column":4},"action":"insert","lines":["T"]}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":4},"action":"remove","lines":["STAT"],"id":237},{"start":{"row":146,"column":0},"end":{"row":146,"column":20},"action":"insert","lines":["STATICFILES_LOCATION"]}],[{"start":{"row":146,"column":20},"end":{"row":146,"column":21},"action":"insert","lines":[" "],"id":238},{"start":{"row":146,"column":21},"end":{"row":146,"column":22},"action":"insert","lines":["="]}],[{"start":{"row":146,"column":22},"end":{"row":146,"column":23},"action":"insert","lines":[" "],"id":239}],[{"start":{"row":146,"column":23},"end":{"row":146,"column":25},"action":"insert","lines":["''"],"id":240}],[{"start":{"row":146,"column":24},"end":{"row":146,"column":25},"action":"insert","lines":["S"],"id":241},{"start":{"row":146,"column":25},"end":{"row":146,"column":26},"action":"insert","lines":["T"]},{"start":{"row":146,"column":26},"end":{"row":146,"column":27},"action":"insert","lines":["A"]},{"start":{"row":146,"column":27},"end":{"row":146,"column":28},"action":"insert","lines":["T"]},{"start":{"row":146,"column":28},"end":{"row":146,"column":29},"action":"insert","lines":["I"]},{"start":{"row":146,"column":29},"end":{"row":146,"column":30},"action":"insert","lines":["C"]}],[{"start":{"row":146,"column":29},"end":{"row":146,"column":30},"action":"remove","lines":["C"],"id":242},{"start":{"row":146,"column":28},"end":{"row":146,"column":29},"action":"remove","lines":["I"]},{"start":{"row":146,"column":27},"end":{"row":146,"column":28},"action":"remove","lines":["T"]},{"start":{"row":146,"column":26},"end":{"row":146,"column":27},"action":"remove","lines":["A"]},{"start":{"row":146,"column":25},"end":{"row":146,"column":26},"action":"remove","lines":["T"]},{"start":{"row":146,"column":24},"end":{"row":146,"column":25},"action":"remove","lines":["S"]}],[{"start":{"row":146,"column":24},"end":{"row":146,"column":25},"action":"insert","lines":["s"],"id":243},{"start":{"row":146,"column":25},"end":{"row":146,"column":26},"action":"insert","lines":["t"]},{"start":{"row":146,"column":26},"end":{"row":146,"column":27},"action":"insert","lines":["a"]},{"start":{"row":146,"column":27},"end":{"row":146,"column":28},"action":"insert","lines":["t"]},{"start":{"row":146,"column":28},"end":{"row":146,"column":29},"action":"insert","lines":["i"]},{"start":{"row":146,"column":29},"end":{"row":146,"column":30},"action":"insert","lines":["c"]}],[{"start":{"row":147,"column":23},"end":{"row":147,"column":63},"action":"remove","lines":["storages.backends.s3boto3.S3Boto3Storage"],"id":244},{"start":{"row":147,"column":23},"end":{"row":147,"column":24},"action":"insert","lines":["c"]},{"start":{"row":147,"column":24},"end":{"row":147,"column":25},"action":"insert","lines":["u"]},{"start":{"row":147,"column":25},"end":{"row":147,"column":26},"action":"insert","lines":["s"]},{"start":{"row":147,"column":26},"end":{"row":147,"column":27},"action":"insert","lines":["t"]},{"start":{"row":147,"column":27},"end":{"row":147,"column":28},"action":"insert","lines":["o"]},{"start":{"row":147,"column":28},"end":{"row":147,"column":29},"action":"insert","lines":["m"]},{"start":{"row":147,"column":29},"end":{"row":147,"column":30},"action":"insert","lines":["_"]}],[{"start":{"row":147,"column":30},"end":{"row":147,"column":31},"action":"insert","lines":["s"],"id":245},{"start":{"row":147,"column":31},"end":{"row":147,"column":32},"action":"insert","lines":["t"]},{"start":{"row":147,"column":32},"end":{"row":147,"column":33},"action":"insert","lines":["o"]},{"start":{"row":147,"column":33},"end":{"row":147,"column":34},"action":"insert","lines":["a"]}],[{"start":{"row":147,"column":33},"end":{"row":147,"column":34},"action":"remove","lines":["a"],"id":246}],[{"start":{"row":147,"column":33},"end":{"row":147,"column":34},"action":"insert","lines":["r"],"id":247},{"start":{"row":147,"column":34},"end":{"row":147,"column":35},"action":"insert","lines":["a"]},{"start":{"row":147,"column":35},"end":{"row":147,"column":36},"action":"insert","lines":["g"]},{"start":{"row":147,"column":36},"end":{"row":147,"column":37},"action":"insert","lines":["e"]},{"start":{"row":147,"column":37},"end":{"row":147,"column":38},"action":"insert","lines":["s"]},{"start":{"row":147,"column":38},"end":{"row":147,"column":39},"action":"insert","lines":["."]}],[{"start":{"row":147,"column":39},"end":{"row":147,"column":40},"action":"insert","lines":["S"],"id":248},{"start":{"row":147,"column":40},"end":{"row":147,"column":41},"action":"insert","lines":["t"]},{"start":{"row":147,"column":41},"end":{"row":147,"column":42},"action":"insert","lines":["a"]},{"start":{"row":147,"column":42},"end":{"row":147,"column":43},"action":"insert","lines":["t"]}],[{"start":{"row":147,"column":39},"end":{"row":147,"column":43},"action":"remove","lines":["Stat"],"id":249},{"start":{"row":147,"column":39},"end":{"row":147,"column":52},"action":"insert","lines":["StaticStorage"]}],[{"start":{"row":152,"column":5},"end":{"row":153,"column":0},"action":"insert","lines":["",""],"id":250},{"start":{"row":153,"column":0},"end":{"row":153,"column":4},"action":"insert","lines":["    "]},{"start":{"row":153,"column":4},"end":{"row":154,"column":0},"action":"insert","lines":["",""]},{"start":{"row":154,"column":0},"end":{"row":154,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":154,"column":0},"end":{"row":154,"column":4},"action":"remove","lines":["    "],"id":251}],[{"start":{"row":154,"column":0},"end":{"row":154,"column":1},"action":"insert","lines":["M"],"id":252},{"start":{"row":154,"column":1},"end":{"row":154,"column":2},"action":"insert","lines":["E"]},{"start":{"row":154,"column":2},"end":{"row":154,"column":3},"action":"insert","lines":["D"]},{"start":{"row":154,"column":3},"end":{"row":154,"column":4},"action":"insert","lines":["I"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":5},"action":"insert","lines":["A"]}],[{"start":{"row":154,"column":0},"end":{"row":154,"column":5},"action":"remove","lines":["MEDIA"],"id":253},{"start":{"row":154,"column":0},"end":{"row":154,"column":19},"action":"insert","lines":["MEDIAFILES_LOCATION"]}],[{"start":{"row":154,"column":19},"end":{"row":154,"column":20},"action":"insert","lines":[" "],"id":254},{"start":{"row":154,"column":20},"end":{"row":154,"column":21},"action":"insert","lines":["="]}],[{"start":{"row":154,"column":21},"end":{"row":154,"column":22},"action":"insert","lines":[" "],"id":255}],[{"start":{"row":154,"column":22},"end":{"row":154,"column":24},"action":"insert","lines":["''"],"id":256}],[{"start":{"row":154,"column":23},"end":{"row":154,"column":24},"action":"insert","lines":["M"],"id":257},{"start":{"row":154,"column":24},"end":{"row":154,"column":25},"action":"insert","lines":["E"]},{"start":{"row":154,"column":25},"end":{"row":154,"column":26},"action":"insert","lines":["D"]},{"start":{"row":154,"column":26},"end":{"row":154,"column":27},"action":"insert","lines":["I"]},{"start":{"row":154,"column":27},"end":{"row":154,"column":28},"action":"insert","lines":["A"]}],[{"start":{"row":154,"column":27},"end":{"row":154,"column":28},"action":"remove","lines":["A"],"id":258},{"start":{"row":154,"column":26},"end":{"row":154,"column":27},"action":"remove","lines":["I"]},{"start":{"row":154,"column":25},"end":{"row":154,"column":26},"action":"remove","lines":["D"]},{"start":{"row":154,"column":24},"end":{"row":154,"column":25},"action":"remove","lines":["E"]},{"start":{"row":154,"column":23},"end":{"row":154,"column":24},"action":"remove","lines":["M"]}],[{"start":{"row":154,"column":23},"end":{"row":154,"column":24},"action":"insert","lines":["m"],"id":259},{"start":{"row":154,"column":24},"end":{"row":154,"column":25},"action":"insert","lines":["e"]},{"start":{"row":154,"column":25},"end":{"row":154,"column":26},"action":"insert","lines":["d"]},{"start":{"row":154,"column":26},"end":{"row":154,"column":27},"action":"insert","lines":["i"]},{"start":{"row":154,"column":27},"end":{"row":154,"column":28},"action":"insert","lines":["a"]}],[{"start":{"row":154,"column":29},"end":{"row":155,"column":0},"action":"insert","lines":["",""],"id":260},{"start":{"row":155,"column":0},"end":{"row":155,"column":1},"action":"insert","lines":["D"]},{"start":{"row":155,"column":1},"end":{"row":155,"column":2},"action":"insert","lines":["E"]},{"start":{"row":155,"column":2},"end":{"row":155,"column":3},"action":"insert","lines":["F"]},{"start":{"row":155,"column":3},"end":{"row":155,"column":4},"action":"insert","lines":["A"]}],[{"start":{"row":155,"column":4},"end":{"row":155,"column":5},"action":"insert","lines":["U"],"id":261},{"start":{"row":155,"column":5},"end":{"row":155,"column":6},"action":"insert","lines":["L"]},{"start":{"row":155,"column":6},"end":{"row":155,"column":7},"action":"insert","lines":["Y"]}],[{"start":{"row":155,"column":6},"end":{"row":155,"column":7},"action":"remove","lines":["Y"],"id":262}],[{"start":{"row":155,"column":6},"end":{"row":155,"column":7},"action":"insert","lines":["T"],"id":263},{"start":{"row":155,"column":7},"end":{"row":155,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":155,"column":8},"end":{"row":155,"column":9},"action":"insert","lines":["F"],"id":264},{"start":{"row":155,"column":9},"end":{"row":155,"column":10},"action":"insert","lines":["I"]},{"start":{"row":155,"column":10},"end":{"row":155,"column":11},"action":"insert","lines":["L"]},{"start":{"row":155,"column":11},"end":{"row":155,"column":12},"action":"insert","lines":["E"]},{"start":{"row":155,"column":12},"end":{"row":155,"column":13},"action":"insert","lines":["_"]},{"start":{"row":155,"column":13},"end":{"row":155,"column":14},"action":"insert","lines":["S"]},{"start":{"row":155,"column":14},"end":{"row":155,"column":15},"action":"insert","lines":["T"]},{"start":{"row":155,"column":15},"end":{"row":155,"column":16},"action":"insert","lines":["O"]}],[{"start":{"row":155,"column":16},"end":{"row":155,"column":17},"action":"insert","lines":["R"],"id":265},{"start":{"row":155,"column":17},"end":{"row":155,"column":18},"action":"insert","lines":["A"]},{"start":{"row":155,"column":18},"end":{"row":155,"column":19},"action":"insert","lines":["G"]},{"start":{"row":155,"column":19},"end":{"row":155,"column":20},"action":"insert","lines":["E"]}],[{"start":{"row":155,"column":20},"end":{"row":155,"column":21},"action":"insert","lines":[" "],"id":266},{"start":{"row":155,"column":21},"end":{"row":155,"column":22},"action":"insert","lines":["="]}],[{"start":{"row":155,"column":22},"end":{"row":155,"column":23},"action":"insert","lines":[" "],"id":267}],[{"start":{"row":155,"column":23},"end":{"row":155,"column":25},"action":"insert","lines":["''"],"id":268}],[{"start":{"row":155,"column":24},"end":{"row":155,"column":25},"action":"insert","lines":["C"],"id":269},{"start":{"row":155,"column":25},"end":{"row":155,"column":26},"action":"insert","lines":["U"]},{"start":{"row":155,"column":26},"end":{"row":155,"column":27},"action":"insert","lines":["S"]}],[{"start":{"row":155,"column":26},"end":{"row":155,"column":27},"action":"remove","lines":["S"],"id":270},{"start":{"row":155,"column":25},"end":{"row":155,"column":26},"action":"remove","lines":["U"]},{"start":{"row":155,"column":24},"end":{"row":155,"column":25},"action":"remove","lines":["C"]}],[{"start":{"row":155,"column":24},"end":{"row":155,"column":25},"action":"insert","lines":["c"],"id":271},{"start":{"row":155,"column":25},"end":{"row":155,"column":26},"action":"insert","lines":["u"]},{"start":{"row":155,"column":26},"end":{"row":155,"column":27},"action":"insert","lines":["t"]},{"start":{"row":155,"column":27},"end":{"row":155,"column":28},"action":"insert","lines":["o"]},{"start":{"row":155,"column":28},"end":{"row":155,"column":29},"action":"insert","lines":["m"]}],[{"start":{"row":155,"column":28},"end":{"row":155,"column":29},"action":"remove","lines":["m"],"id":272},{"start":{"row":155,"column":27},"end":{"row":155,"column":28},"action":"remove","lines":["o"]},{"start":{"row":155,"column":26},"end":{"row":155,"column":27},"action":"remove","lines":["t"]}],[{"start":{"row":155,"column":26},"end":{"row":155,"column":27},"action":"insert","lines":["s"],"id":273}],[{"start":{"row":155,"column":24},"end":{"row":155,"column":27},"action":"remove","lines":["cus"],"id":274},{"start":{"row":155,"column":24},"end":{"row":155,"column":39},"action":"insert","lines":["custom_storages"]}],[{"start":{"row":155,"column":39},"end":{"row":155,"column":40},"action":"insert","lines":["."],"id":275},{"start":{"row":155,"column":40},"end":{"row":155,"column":41},"action":"insert","lines":["M"]},{"start":{"row":155,"column":41},"end":{"row":155,"column":42},"action":"insert","lines":["e"]},{"start":{"row":155,"column":42},"end":{"row":155,"column":43},"action":"insert","lines":["d"]}],[{"start":{"row":155,"column":40},"end":{"row":155,"column":43},"action":"remove","lines":["Med"],"id":276},{"start":{"row":155,"column":40},"end":{"row":155,"column":52},"action":"insert","lines":["MediaStorage"]}],[{"start":{"row":146,"column":0},"end":{"row":158,"column":21},"action":"remove","lines":["STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","","STATIC_URL = '/static/'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),","    )","    ","MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"],"id":277}],[{"start":{"row":146,"column":0},"end":{"row":158,"column":74},"action":"insert","lines":["STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","","STATIC_URL = '/static/'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")","","MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"],"id":278}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":279}],[{"start":{"row":91,"column":0},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":280}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["i"],"id":281},{"start":{"row":92,"column":1},"end":{"row":92,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":92,"column":2},"end":{"row":92,"column":3},"action":"insert","lines":[" "],"id":282}],[{"start":{"row":92,"column":3},"end":{"row":92,"column":4},"action":"insert","lines":["D"],"id":283},{"start":{"row":92,"column":4},"end":{"row":92,"column":5},"action":"insert","lines":["A"]},{"start":{"row":92,"column":5},"end":{"row":92,"column":6},"action":"insert","lines":["D"]}],[{"start":{"row":92,"column":5},"end":{"row":92,"column":6},"action":"remove","lines":["D"],"id":284}],[{"start":{"row":92,"column":3},"end":{"row":92,"column":5},"action":"remove","lines":["DA"],"id":285},{"start":{"row":92,"column":3},"end":{"row":92,"column":15},"action":"insert","lines":["DATABASE_URL"]}],[{"start":{"row":92,"column":15},"end":{"row":92,"column":16},"action":"insert","lines":[" "],"id":286},{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["I"]},{"start":{"row":92,"column":17},"end":{"row":92,"column":18},"action":"insert","lines":["N"]}],[{"start":{"row":92,"column":18},"end":{"row":92,"column":19},"action":"insert","lines":[" "],"id":287}],[{"start":{"row":92,"column":18},"end":{"row":92,"column":19},"action":"remove","lines":[" "],"id":288},{"start":{"row":92,"column":17},"end":{"row":92,"column":18},"action":"remove","lines":["N"]},{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"remove","lines":["I"]}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["i"],"id":289},{"start":{"row":92,"column":17},"end":{"row":92,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":92,"column":18},"end":{"row":92,"column":19},"action":"insert","lines":[" "],"id":290}],[{"start":{"row":92,"column":3},"end":{"row":92,"column":4},"action":"insert","lines":["\""],"id":291}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["\""],"id":292}],[{"start":{"row":92,"column":20},"end":{"row":92,"column":21},"action":"insert","lines":[" "],"id":293},{"start":{"row":92,"column":21},"end":{"row":92,"column":22},"action":"insert","lines":["o"]},{"start":{"row":92,"column":22},"end":{"row":92,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":92,"column":23},"end":{"row":92,"column":24},"action":"insert","lines":["."],"id":294},{"start":{"row":92,"column":24},"end":{"row":92,"column":25},"action":"insert","lines":["e"]},{"start":{"row":92,"column":25},"end":{"row":92,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":92,"column":26},"end":{"row":92,"column":27},"action":"insert","lines":["v"],"id":295}],[{"start":{"row":92,"column":24},"end":{"row":92,"column":27},"action":"remove","lines":["env"],"id":296},{"start":{"row":92,"column":24},"end":{"row":92,"column":31},"action":"insert","lines":["environ"]}],[{"start":{"row":92,"column":31},"end":{"row":92,"column":32},"action":"insert","lines":[":"],"id":297}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "],"id":298}],[{"start":{"row":93,"column":82},"end":{"row":94,"column":0},"action":"insert","lines":["",""],"id":299},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"remove","lines":["    "],"id":300}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"insert","lines":["e"],"id":301},{"start":{"row":94,"column":1},"end":{"row":94,"column":2},"action":"insert","lines":["l"]},{"start":{"row":94,"column":2},"end":{"row":94,"column":3},"action":"insert","lines":["s"]},{"start":{"row":94,"column":3},"end":{"row":94,"column":4},"action":"insert","lines":["e"]}],[{"start":{"row":94,"column":4},"end":{"row":94,"column":5},"action":"insert","lines":[":"],"id":302}],[{"start":{"row":94,"column":5},"end":{"row":95,"column":0},"action":"insert","lines":["",""],"id":303},{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":5},"action":"insert","lines":["p"],"id":304},{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"insert","lines":["t"]},{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"insert","lines":["i"]},{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"remove","lines":["n"],"id":305},{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"remove","lines":["i"]},{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"remove","lines":["t"]}],[{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"insert","lines":["r"],"id":306},{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"insert","lines":["i"]},{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"insert","lines":["n"]},{"start":{"row":95,"column":8},"end":{"row":95,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":9},"action":"remove","lines":["print"],"id":307},{"start":{"row":95,"column":4},"end":{"row":95,"column":11},"action":"insert","lines":["print()"]}],[{"start":{"row":95,"column":10},"end":{"row":95,"column":12},"action":"insert","lines":["\"\""],"id":308}],[{"start":{"row":95,"column":11},"end":{"row":95,"column":12},"action":"insert","lines":["D"],"id":309},{"start":{"row":95,"column":12},"end":{"row":95,"column":13},"action":"insert","lines":["a"]},{"start":{"row":95,"column":13},"end":{"row":95,"column":14},"action":"insert","lines":["t"]},{"start":{"row":95,"column":14},"end":{"row":95,"column":15},"action":"insert","lines":["a"]},{"start":{"row":95,"column":15},"end":{"row":95,"column":16},"action":"insert","lines":["b"]},{"start":{"row":95,"column":16},"end":{"row":95,"column":17},"action":"insert","lines":["a"]},{"start":{"row":95,"column":17},"end":{"row":95,"column":18},"action":"insert","lines":["s"]},{"start":{"row":95,"column":18},"end":{"row":95,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":95,"column":19},"end":{"row":95,"column":20},"action":"insert","lines":[" "],"id":310},{"start":{"row":95,"column":20},"end":{"row":95,"column":21},"action":"insert","lines":["U"]},{"start":{"row":95,"column":21},"end":{"row":95,"column":22},"action":"insert","lines":["R"]}],[{"start":{"row":95,"column":22},"end":{"row":95,"column":23},"action":"insert","lines":["L"],"id":311}],[{"start":{"row":95,"column":23},"end":{"row":95,"column":24},"action":"insert","lines":[" "],"id":312},{"start":{"row":95,"column":24},"end":{"row":95,"column":25},"action":"insert","lines":["n"]},{"start":{"row":95,"column":25},"end":{"row":95,"column":26},"action":"insert","lines":["o"]},{"start":{"row":95,"column":26},"end":{"row":95,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":95,"column":27},"end":{"row":95,"column":28},"action":"insert","lines":[" "],"id":313},{"start":{"row":95,"column":28},"end":{"row":95,"column":29},"action":"insert","lines":["f"]},{"start":{"row":95,"column":29},"end":{"row":95,"column":30},"action":"insert","lines":["o"]},{"start":{"row":95,"column":30},"end":{"row":95,"column":31},"action":"insert","lines":["u"]},{"start":{"row":95,"column":31},"end":{"row":95,"column":32},"action":"insert","lines":["n"]},{"start":{"row":95,"column":32},"end":{"row":95,"column":33},"action":"insert","lines":["d"]}],[{"start":{"row":95,"column":33},"end":{"row":95,"column":34},"action":"insert","lines":["."],"id":314}],[{"start":{"row":95,"column":34},"end":{"row":95,"column":35},"action":"insert","lines":[" "],"id":315},{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"insert","lines":[" "]},{"start":{"row":95,"column":36},"end":{"row":95,"column":37},"action":"insert","lines":["U"]},{"start":{"row":95,"column":37},"end":{"row":95,"column":38},"action":"insert","lines":["s"]},{"start":{"row":95,"column":38},"end":{"row":95,"column":39},"action":"insert","lines":["i"]},{"start":{"row":95,"column":39},"end":{"row":95,"column":40},"action":"insert","lines":["n"]},{"start":{"row":95,"column":40},"end":{"row":95,"column":41},"action":"insert","lines":["g"]}],[{"start":{"row":95,"column":41},"end":{"row":95,"column":42},"action":"insert","lines":[" "],"id":316},{"start":{"row":95,"column":42},"end":{"row":95,"column":43},"action":"insert","lines":["S"]},{"start":{"row":95,"column":43},"end":{"row":95,"column":44},"action":"insert","lines":["Q"]},{"start":{"row":95,"column":44},"end":{"row":95,"column":45},"action":"insert","lines":["L"]}],[{"start":{"row":95,"column":45},"end":{"row":95,"column":46},"action":"insert","lines":["i"],"id":317},{"start":{"row":95,"column":46},"end":{"row":95,"column":47},"action":"insert","lines":["t"]},{"start":{"row":95,"column":47},"end":{"row":95,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":95,"column":48},"end":{"row":95,"column":49},"action":"insert","lines":[" "],"id":318},{"start":{"row":95,"column":49},"end":{"row":95,"column":50},"action":"insert","lines":["i"]},{"start":{"row":95,"column":50},"end":{"row":95,"column":51},"action":"insert","lines":["n"]},{"start":{"row":95,"column":51},"end":{"row":95,"column":52},"action":"insert","lines":["s"]},{"start":{"row":95,"column":52},"end":{"row":95,"column":53},"action":"insert","lines":["t"]},{"start":{"row":95,"column":53},"end":{"row":95,"column":54},"action":"insert","lines":["e"]},{"start":{"row":95,"column":54},"end":{"row":95,"column":55},"action":"insert","lines":["a"]},{"start":{"row":95,"column":55},"end":{"row":95,"column":56},"action":"insert","lines":["d"]}],[{"start":{"row":85,"column":0},"end":{"row":90,"column":3},"action":"remove","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }"],"id":319}],[{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"remove","lines":["",""],"id":320}],[{"start":{"row":89,"column":58},"end":{"row":90,"column":0},"action":"insert","lines":["",""],"id":321},{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":90,"column":4},"end":{"row":95,"column":3},"action":"insert","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }"],"id":322}],[{"start":{"row":90,"column":4},"end":{"row":90,"column":6},"action":"remove","lines":["# "],"id":323},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"remove","lines":["# "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"remove","lines":["# "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":2},"action":"remove","lines":["# "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"remove","lines":["# "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "],"id":324},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["#"],"id":325}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":326}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":1},"end":{"row":13,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584463506489}