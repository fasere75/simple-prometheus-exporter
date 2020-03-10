from prometheus_client import start_http_server, Summary, Counter , Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
c = Counter('my_failures', 'Description of counter')
d = Gauge('data_objects', 'Number of objects')




# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)
    c.inc()     # Increment by 
    c.inc(1.6)  # Increment by given value
    my_dict = {"ruleengine_sftr_gsl":1, "ruleengine_sftr_ml":2}
    d.set_function(lambda: len(my_dict))


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
