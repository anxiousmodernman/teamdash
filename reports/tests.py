"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from reports.models import Report


class ReportsTest(TestCase):

    def create_report(self, name="pandastest", language="python", author="coleman",
                      path="/scripts/tests/pandastest.py", schema=None):
        test_report = Report(self, name=name, language=language, author=author,
                                            path=path, schema=schema)
        return test_report

    def testGetPath(self):
        report = self.create_report()
        hard_coded_path = '/home/coleman/Code/teamdash/reports/scripts/tests/pandastest.py'
        self.assertEquals(report.getPath(), hard_coded_path)


