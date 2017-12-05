"""
Django settings for techblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jtnhx9ccr6&ug&q0&y_1v&g9a%q$&b^j6+_09n1##+kg!1+dj@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.syndication',
    'django.contrib.sitemaps',
    'libs.django-disqus.disqus', # for comments
    'libs.ckeditor', # for managing text,images and formulas
    'libs.ckeditor_uploader',
)
SITE_ID = 1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'blog.middleware.MobileTemplatesMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    "django.core.context_processors.media",
    "django.core.context_processors.static",
)

ROOT_URLCONF = 'techblog.urls'

WSGI_APPLICATION = 'techblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'img')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/img/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog','static'),
)

# Template directory
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog', 'templates'),
)
MOBILE_TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog', 'templates', 'mobile'),
)
DESKTOP_TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog', 'templates', 'desktop'),
)


# Disqus configuration (for managing comments)
# To install disqus http://django-disqus.readthedocs.org/en/latest/index.html
DISQUS_API_KEY = 'DISQUS_API_KEY'
DISQUS_WEBSITE_SHORTNAME = 'rktechiblog'

# Http protocol with (https://) or without SSL (http://)
# NOTE: You need to have a SSL certificate installed before setting this flag to True
HTTPS = False

# Social Networks
FACEBOOK_ID = 'keyurr2' #for Facebook tracking
FACEBOOK_URL = 'https://www.facebook.com/keyurr2'
TWITTER_URL = 'https://twitter.com/keyurr2'
TWITTER_HANDLE = 'keyurr2'
LINKEDIN_URL = 'https://in.linkedin.com/'
GOOGLE_PLUS_URL = 'https://plus.google.com/'
PINTEREST_URL = ''
INSTAGRAM_URL = ''
RSS_URL = 'http://feeds.feedburner.com/keyurr2'

# Google Analytics
GA_TRACKING_ID = 'GA_TRACKING_ID'

# Ckeditor
CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_IMAGE_BACKEND = "pillow"

