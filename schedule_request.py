from server_trigger import ServerTrigger
import yaml
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

class ScheduleRequest:

    def __init__(self, yaml_path):
        self.server_trigger = ServerTrigger()
        self.scheduler = BackgroundScheduler()
        with open(yaml_path, "r") as stream:
            try:
                self.requests = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.init_jobs()

    def init_jobs(self):
        for frequency in self.requests.keys():
            for job in self.requests[frequency]:
                self.scheduler.add_job(func=self.server_trigger.trigger_url,
                                       args=(job['url'], job['name']),
                                       trigger="interval",
                                       seconds=int(frequency),
                                       next_run_time=datetime.now())

    def run(self):
        self.scheduler.start()
