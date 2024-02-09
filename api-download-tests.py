# create a test for the download API, call download API 10 times in parallel and check the response time, response is a zip file
import requests
import time
import threading
import os

# download API
url = "http://localhost:8080/download"

# create a function to call the download API
def download_api_call():
    # call the download API a post request with request body

    response = requests.post(url, json=[])
    # check the response status code
    if response.status_code == 200:
        print("Download API call successful")
    else:
        print("Download API call failed")

# create a function to call the download API 10 times in parallel
def parallel_download_api_calls():
    # create a list to store the threads
    threads = []
    # loop to call the download API 10 times in parallel
    for i in range(10):
        # create a thread for each download API call
        t = threading.Thread(target=download_api_call)
        # start the thread
        t.start()
        # add the thread to the list
        threads.append(t)
    # loop to join the threads
    for t in threads:
        t.join()

# call the function to call the download API 10 times in parallel
parallel_download_api_calls()
