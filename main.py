from schedule_request import ScheduleRequest
if __name__ == '__main__':
    executor = ScheduleRequest("requests.yml")
    executor.run()
    while True:
        continue
