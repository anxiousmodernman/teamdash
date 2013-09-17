# Create your app's views here.
from reports.models import Report
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

class ReportListAPIView(ListCreateAPIView):
    model = Report

class ReportRetrieveAPIView(RetrieveUpdateAPIView):
    model = Report


