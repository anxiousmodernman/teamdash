# Create your views here.
from reports.models import Report
from rest_framework.generics import ListCreateAPIView

class ReportListAPIView(ListCreateAPIView):
    model = Report
