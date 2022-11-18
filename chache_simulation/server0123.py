import requests
from cachetools import cached, TTLCache
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import time
import random
# creating chache using TTLCache
cache = TTLCache(maxsize=100, ttl=86400)

# initialize cache a the beginning
# in proxy mode the request doesnt have to go the the page but get the request from the chache
@cached(cache)
def proxy_mode_server(url):
    response = requests.get(url)
    content = response.content
    return content

# server access via the direct mode method
def direct_mode_server(url):
    response = requests.get(url)
    content = response.content
    return content


hostName = "localhost"
# you can change the port number to any valid http port
serverPort = 8080


class ServerSimulation(SimpleHTTPRequestHandler):
    # simulate the randomness of the web server
    # like network delays, propagation delays and processing delays
    time.sleep(random.randint(0, 3))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), ServerSimulation)
    print("Server running on  http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
