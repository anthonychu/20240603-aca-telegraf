from prometheus_client import start_http_server, Summary
import random
import time


# Create a metric to track time spent and requests made.
MY_METRIC = Summary('my_metric', 'Time spent processing request')


# Decorate function with metric.
@MY_METRIC.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.

    print ('Metrics service is up and running !')
    start_http_server(8000)

    # Generate some requests.
    while True:
        process_request(random.random())

