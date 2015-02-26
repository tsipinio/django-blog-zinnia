__author__ = 'pasha'

from django.conf import settings
from django.db.utils import ProgrammingError, OperationalError
from zinnia import settings as zinnia_settings


class ConfigurationMiddleware(object):

    def process_request(self, request):
        try:
            PAGINATION = getattr(settings, 'ZINNIA_PAGINATION', 10)
            setattr(zinnia_settings, "PAGINATION", PAGINATION)
        except (ProgrammingError, OperationalError) as e:
            print e
