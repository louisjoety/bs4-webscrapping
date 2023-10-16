import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

html = requests.get(url)
s = BeautifulSoup(html.content, 'html.parser')

results = s.find(id = "ResultsContainer")

job_title = results.find_all('h2', class_= 'title is-5')
human_title = results.find_all('h3', class_= 'subtitle is-6 company')
location_title = results.find_all('p', class_= 'location')
date_title = results.find_all('p', class_= 'is-small has-text-grey')

for job, human, location, date in zip(job_title, human_title, location_title, date_title):
    print(f"Job Title: {job.text.strip()}")
    print(f"Posted by: {human.text.strip()}")
    print(f"Located at: {location.text.strip()}")
    print(f"Date Posted: {date.text.strip()}")
    print()
