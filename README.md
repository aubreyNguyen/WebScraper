# Course Website Scraper
## How to Use
```
pip install requests
chmod +x scraper.py
./scraper.py
```
This program prints out the published homework and reading assignment titles from the course website. It scrapes with 1 worker and then with 4 workers, printing out the time it took.

## Screenshot
<img width="532" height="379" alt="website_scraper_screenshot" src="https://github.com/user-attachments/assets/4caf24c6-caa3-4609-a40d-0ffec7529964" />


## Performance Impact
### Functional Programming
The program uses map() and filter(). Map() was used multiple times, including to form the links of individual assignment pages by adding the base url to each assignment name and to apply scrape_assignment to each assignment link. Filter() is used to create separate lists of readings and homeworks from the list of all assignments. Both functional programming techniques don't have much of an effect on speed, but they keep the code concise by applying a function or condition to a list of items in one line of code.

### Concurrency
With concurrent.futures.ThreadPoolExecutor, the program scrapes the assignment pages with 1 worker and 4 workers and prints out the time each took. Using 4 workers allows multiple pages to be scraped at once. From the output, this results in a time (0.239 s) about 3.4x faster than using 1 worker (0.807 s). 
