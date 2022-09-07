

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeB_Wierysz.settings')

application = get_wsgi_application()
