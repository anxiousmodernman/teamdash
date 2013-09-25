import unittest
from time import sleep
import sys
from dbworker import worker
from datasource.engines import *
import datetime

# call celery task with a django Report model
# celery task looks up the script's path, an attribute of the model
# # if the attribute exists, look for the file itself
# # # if file exists, run the file as a script
# # # else raise Exception that the file doesn't exist
# # else raise Exception that the Report model doesn't have path attribute