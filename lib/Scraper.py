
from bs4 import BeautifulSoup 
import requests
import ipdb
import Course
import json

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'html.parser')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3', class_="joblist-comp-name").text.strip()
    skills = job.find('span', class_="srp-skills").text.replace(' ','')
    published_date = job.find('span', class_ = 'sim-posted').span.text
    print(f'''
    Company Name: {company_name}
    Required Skills: {skills}
    Published Date: {published_date}''')
    print('')
    



