# import statistics to help in calculating median in python
import statistics
# both files should reside in one directory for easy call up of one another, the onlineTestsPy
# is the folder where the two files reside
from onlineTestsPy.server0123 import proxy_mode_server, direct_mode_server
import time


def direct_method(url):
    # a list to store time taken for each request
    response_time = []
    # printing the output headings
    print('Direct Mode')
    print('#Requests | Avg. Response Time | Median Response Time')
    # looping through per a hundred requests from 100 to 1000 as directed in the assignment
    for re in range(1, 11, 1):
        # an inside loop to handle each request in range of 100
        for t in range(100):
            start = time.time()
            direct_mode_server(url)
            end = time.time()
            response_time.append(end - start)
            # output for the response time and the median
        print(re * 100, '      ', round(sum(response_time), 5), '\t\t\t', round(statistics.median(response_time), 10))


def proxy_method(url):
    # printing the output headings
    response_time = []
    # printing the output headings
    print('Proxy Mode')
    print('#Requests | Avg. Response Time | Median Response Time')
    # looping through per a hundred requests from 100 to 1000 as directed in the assignment
    for re in range(1, 11, 1):
        # an inside loop to handle each request in range of 100
        for t in range(100):
            start = time.time()
            proxy_mode_server(url)
            end = time.time()
            response_time.append(end - start)
            # output for the response time and the median
        print(re * 100, '      ', round(sum(response_time), 5), '\t\t\t', round(statistics.median(response_time), 8))


# function calls..NB uncomment one function call whenever you are calling the other one
# after running the server, copy the url and paste here
# proxy_method('http://localhost:8080/')
direct_method('http://localhost:8080/')  # function on call with running url