from prometheus_client.core import REGISTRY,GaugeMetricFamily
from prometheus_client import start_http_server
from time import sleep
from datetime import datetime, timedelta
'''
  Simple demo on how to use Prometheus client Library using Python
'''
class simple_exporter(object):
    def __init__(self):
        pass

    def collect (self):
        # initialise record/match count
        records    = {"application_error":0, "user_activity":0, "application_event":0  }
        
        # activities to track
        activities =  ["application_error", "user_activity", "application_event"]

        # we are only interested in activities which happened exactly a minute ago
        aMinuteAgo = datetime.now() - timedelta (minutes=1)
        timestamp =  aMinuteAgo.strftime("%Y-%m-%d %H:%M")
    
        #Open the log file to parse
        file_content = open('app.log','r')
        
        # loop over each record of the file
        for content in file_content.readlines():
            if timestamp in content: # filter only events which happened a minute ago
              for activity in activities:
                  if activity in content: # see if there is a match for an activity
                      records[activity] = records[activity]  + 1

        metric = GaugeMetricFamily("techbleat","this is just a demo", labels=["activities"])
        for activity in activities:
            print ("%s has %s matches" % (activity,records [activity]))
            metric.add_metric ([activity],records [activity])

        yield metric  #make metric available to Prometheus


if __name__ == '__main__':
    REGISTRY.register (simple_exporter())
    # start the http server 
    start_http_server(9000)
    while True: sleep(10)
    