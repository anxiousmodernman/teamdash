from django.conf import settings

# TODO handle paths to scripts better
REPORTS_PATH = getattr(settings, 'REPORTS_PATH', '/home/coleman/Code/teamdash/reports')

