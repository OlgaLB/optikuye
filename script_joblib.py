#!/usr/bin/env python3

# pip(3) install joblib

import time
import requests
import multiprocessing
from joblib import Parallel, delayed

def get_single_page(url):
    with requests.Session().get(url) as response:
        print(f"Read {len(response.content)} from {url}")

if __name__ == "__main__":

    websites = [ "https://www.google.de/", ] * 10

    # with JobLib
    threads = []
    start_time = time.time()
    Parallel(n_jobs=multiprocessing.cpu_count())(delayed(get_single_page)(website) for website in websites)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Downloaded {len(websites)} in {duration} seconds - with JobLib")

