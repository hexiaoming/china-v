# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zuvp4036q9zpc!)0sac=qhk!%udh^5dcavrr@lc6c)m41f3nz%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['wx.jdb.cn'] 

from base.common import *
from base.loggers import LOGGING

