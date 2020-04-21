#!/usr/bin/env python3

import time
import requests
import multiprocessing

def get_single_page(url):
    with requests.Session().get(url) as response:
        print(f"Read {len(response.content)} from {url}")

if __name__ == "__main__":

    websites = [ "https://www.google.de/", ] * 10

    # with Pool
    process_pool = multiprocessing.Pool(multiprocessing.cpu_count())
    start_time = time.time()
    process_pool.map(get_single_page, websites)
    end_time = time.time()
    duration = end_time - start_time
    process_pool.close()
    print(f"Downloaded {len(websites)} in {duration} seconds - with Pool")

    # with Process
    processes = []
    start_time = time.time()
    for website in websites:
        process = multiprocessing.Process(target = get_single_page, args=(website,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    print(f"Downloaded {len(websites)} in {end_time - start_time} seconds - with Process")
