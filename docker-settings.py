# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from .development import *

#########################################
## GENERIC
#########################################

SECRET_KEY = os.environ.get('SECRET_KEY', 'ultraverytopsecret')
DEBUG = os.environ.get('DEBUG') == 'True'

#ADMINS = (
#    ("Admin", "example@example.com"),
#)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE',
                                 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DATABASE_NAME', 'taiga'),
        'USER': os.environ.get('DATABASE_USER', 'taiga'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'changeme'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5234'),
    }
}

EVENTS_PUSH_BACKEND = os.environ.get('EVENTS_PUSH_BACKEND',
                                     "taiga.events.backends.rabbitmq.EventsPushBackend")
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": os.environ.get('EVENTS_PUSH_URL', "amqp://taiga:PASSWORD_FOR_EVENTS@localhost:5672/taiga")
}

SITES = {
    "api": {
       "scheme": os.environ.get('API_SCHEME', 'http'),
       "domain": os.environ.get('API_DOMAIN', 'localhost:8000'),
       "name": "api"
    },
    "front": {
       "scheme": os.environ.get('FRONT_SCHEME', 'http'),
       "domain": os.environ.get('FRONT_DOMAIN', 'localhost:9001'),
       "name": "front"
    },
}

#SITE_ID = "api"

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/home/taiga/media')
STATIC_ROOT = os.environ.get('STATIC_ROOT', '/home/taiga/static')


#########################################
## THROTTLING
#########################################

#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon-write": "20/min",
#    "user-write": None,
#    "anon-read": None,
#    "user-read": None,
#    "import-mode": None,
#    "import-dump-mode": "1/minute",
#    "create-memberships": None,
#    "login-fail": None,
#    "register-success": None,
#    "user-detail": None,
#    "user-update": None,
#}

# This list should containt:
#  - Tiga users IDs
#  - Valid clients IP addresses (X-Forwarded-For header)
#REST_FRAMEWORK["DEFAULT_THROTTLE_WHITELIST"] = []


#########################################
## MAIL SYSTEM SETTINGS
#########################################

if(os.environ.get("EMAIL_SETTINGS") == 'True'):
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', "john@doe.com")
    CHANGE_NOTIFICATIONS_MIN_INTERVAL = int(os.environ.get('CHANGE_NOTIFICATION_MIN_INTERVAL', 300)) #seconds

    EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND',
                                   'django.core.mail.backends.smtp.EmailBackend')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', False) # You cannot use both (TLS and SSL) at the same time!
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
    EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'user')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password')

#########################################
## REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = os.environ.get('PUBLIC_REGISTER_ENABLED') == 'True'

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

# GITHUB SETTINGS
#GITHUB_URL = "https://github.com/"
#GITHUB_API_URL = "https://api.github.com/"
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"


#########################################
## STATS
#########################################

#STATS_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second


#########################################
## CELERY
#########################################
# Set to True to enable celery and work in async mode or False
# to disable it and work in sync mode. You can find the celery
# settings in settings/celery.py and settings/celery-local.py
#CELERY_ENABLED = True


#########################################
## IMPORTERS
#########################################

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
#IMPORTERS["github"] = {
#    "active": True, # Enable or disable the importer
#    "client_id": "XXXXXX_get_a_valid_client_id_from_github_XXXXXX",
#    "client_secret": "XXXXXX_get_a_valid_client_secret_from_github_XXXXXX"
#}

# Configuration for the Trello importer
# Remember to enable it in the front client too.
#IMPORTERS["trello"] = {
#    "active": True, # Enable or disable the importer
#    "api_key": "XXXXXX_get_a_valid_api_key_from_trello_XXXXXX",
#    "secret_key": "XXXXXX_get_a_valid_secret_key_from_trello_XXXXXX"
#}

# Configuration for the Jira importer
# Remember to enable it in the front client too.
#IMPORTERS["jira"] = {
#    "active": True, # Enable or disable the importer
#    "consumer_key": "XXXXXX_get_a_valid_consumer_key_from_jira_XXXXXX",
#    "cert": "XXXXXX_get_a_valid_cert_from_jira_XXXXXX",
#    "pub_cert": "XXXXXX_get_a_valid_pub_cert_from_jira_XXXXXX"
#}

# Configuration for the Asane importer
# Remember to enable it in the front client too.
#IMPORTERS["asana"] = {
#    "active": True, # Enable or disable the importer
#    "callback_url": "{}://{}/project/new/import/asana".format(SITES["front"]["scheme"],
#                                                              SITES["front"]["domain"]),
#    "app_id": "XXXXXX_get_a_valid_app_id_from_asana_XXXXXX",
#    "app_secret": "XXXXXX_get_a_valid_app_secret_from_asana_XXXXXX"
#}
