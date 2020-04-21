#!/usr/bin/env python3

import time
import requests
import threading

def get_single_page(url):
    with requests.Session().get(url) as response:
        print(f"Read {len(response.content)} from {url}")

if __name__ == "__main__":

    websites = [ "https://www.google.de/", ] * 10

    # with Thread
    threads = []
    start_time = time.time()
    for website in websites:
        thread = threading.Thread(target = get_single_page, args=(website,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Downloaded {len(websites)} in {end_time - start_time} seconds - with Thread")
