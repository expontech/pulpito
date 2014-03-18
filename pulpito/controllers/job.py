from pecan import expose
from pecan import conf
import requests
from util import prettify_job
from pulpito.controllers import error

base_url = conf.paddles_address


class JobController(object):
    def __init__(self, run_name, job_id):
        self.run_name = run_name
        self.job_id = job_id
        resp = requests.get("{base}/runs/{run}/jobs/{job}".format(
            base=base_url, run=run_name, job=job_id))

        if resp.status_code == 400:
            error('/errors/invalid/')
        elif resp.status_code == 404:
            error('/errors/not_found/')
        else:
            self.job = resp.json()
            prettify_job(self.job)

    @expose('job.html')
    def index(self):
        return dict(job=self.job)
