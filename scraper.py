#!/usr/bin/env python3

import requests
import sys
import re
import concurrent.futures
import time

COURSE_URL = 'https://pnutz.h4x0r.space/courses/cse.20589.fa26/'

def fetch_url(url: str) -> str | None:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def assignment_links(page: str) -> list[str]:
    reading = re.findall(r'(reading\d+\.html)', page)
    homework = re.findall(r'(homework\d+\.html)', page)
    names = reading + homework

    return list(map(lambda name: COURSE_URL + name, names))

def scrape_assignment(url: str):
    try:
        page = fetch_url(url)
    except requests.HTTPError:
        return (url.split('/')[-1] + ' | Not published yet')

    title = re.search(r'<h1>(.*?)</h1>', page)
    title = re.sub(r'<[^>]+>', '', title.group())
    return title
    
def main():
    workers = [1,4]

    url_text = fetch_url(COURSE_URL + 'index.html')
    links = assignment_links(url_text)
    
    for num in workers:
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor(num) as executor:
            assignments = list(executor.map(scrape_assignment, links))
        elapsed = time.perf_counter() - start
        print(f'Time ({num} workers): {elapsed: 0.3f} seconds')
    print()

    readings = list(filter(lambda title: title.startswith('Reading'), assignments))
    homeworks = list(filter(lambda title: title.startswith('Homework'), assignments))

    print('READING ASSIGNMENTS')
    for title in readings:
        print(title)

    print('\nHOMEWORK ASSIGNMENTS')
    for title in homeworks:
        print(title)

if __name__ == "__main__":
    main()
