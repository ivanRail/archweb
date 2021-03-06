import os
# Django settings for archweb project.

## Set the debug values
DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR = False

## Notification admins
ADMINS = ()

# Set managers to admins
MANAGERS = ADMINS

# Package out-of-date emails for orphans
NOTIFICATIONS = ['arch-notifications@archlinux.org']

# Full path to the data directory
DEPLOY_PATH = os.path.dirname(os.path.realpath(__file__))

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'
DEFAULT_CHARSET = 'utf-8'

SITE_ID = 1

# Default date format in templates for 'date' filter
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'

# Login URL configuration
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Set django's User stuff to use our profile model
AUTH_PROFILE_MODULE = 'devel.UserProfile'

# We add a processor to determine if the request is secure or not
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages',
    'main.context_processors.secure',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    '%s/templates' % DEPLOY_PATH,
)

TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

# Send templates matching the following to the Jinja2 engine
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

# Base of the URL hierarchy
ROOT_URLCONF = 'urls'

# URL to serve static files
STATIC_URL = '/static/'

# Location to collect static files
STATIC_ROOT = os.path.join(DEPLOY_PATH, 'collected_static')

# Look for more static files in these locations
STATICFILES_DIRS = (
    os.path.join(DEPLOY_PATH, 'sitestatic'),
)

# Static files backend that allows us to use far future Expires headers
STATICFILES_STORAGE = 'main.storage.MinifiedStaticFilesStorage'

# Configure where messages should reside
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Session configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_HTTPONLY = True

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'

# Use new test runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_countries',
    'django_jinja',

    'main',
    'mirrors',
    'news',
    'packages',
    'todolists',
    'devel',
    'public',
    'releng',
    'visualize',
    'retro',
)

# Logging configuration for not getting overspammed
LOGGING = {
    'version': 1,
    'filters': {
        'ratelimit': {
            '()': 'main.log.RateLimitFilter',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['ratelimit'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        }
    },
}

## Server used for linking to PGP keysearch results
PGP_SERVER = 'pgp.mit.edu'
PGP_SERVER_SECURE = True

# URL to fetch a current list of available ISOs
ISO_LIST_URL = 'https://releng.archlinux.org/isos/'

# URL for SVN access for fetching commit messages (note absence of packages or
# community bit on the end, repo.svn_root is appended)
SVN_BASE_URL = 'svn://svn.archlinux.org/'

# Trackers used for ISO download magnet links
TORRENT_TRACKERS = (
    'udp://tracker.archlinux.org:6969',
    'http://tracker.archlinux.org:6969/announce',
)

# Shorten some names just a bit
COUNTRIES_OVERRIDE = {
    'GB': 'United Kingdom',
    'US': 'United States',
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '00000000000000000000000000000000000000000000000'

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.sqlite3',
        'NAME'    : 'database.db',
    },
}

## Import local settings
try:
    from local_settings import *
except ImportError:
    pass

# Enable caching templates in production environments
if not TEMPLATE_DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    )
    JINJA2_BYTECODE_CACHE_ENABLE = True

# Enable the debug toolbar if requested
if DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES = \
            [ 'debug_toolbar.middleware.DebugToolbarMiddleware' ] + \
            list(MIDDLEWARE_CLASSES)

    INSTALLED_APPS = list(INSTALLED_APPS) + [ 'debug_toolbar' ]

# vim: set ts=4 sw=4 et:
