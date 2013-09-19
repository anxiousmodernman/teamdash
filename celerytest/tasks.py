from celery import task

@task()
def runJob(runConfig):
    print 'Wow I got celery working'
    pass
