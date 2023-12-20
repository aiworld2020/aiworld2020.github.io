# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.codin.app/internships"  # Replace with the URL of the webpage you want to scrape
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the relevant elements using BeautifulSoup's selectors
event_elements = soup.select('div.collection-item.w-dyn-item')

# Create a list to store event details
events_list = []


'''
<div role="listitem" class="collection-item w-dyn-item">
<div class="card-3 events"><div class="card-content events"><a href="https://www.tuftstubers.com/" target="_blank" class="card-title-link w-inline-block">
<h2 fs-cmsfilter-field="names" class="title card-event">Tufts University Biomedical Engineering Research Scholars (TUBERS)</h2></a><p>​The Tufts University Biomedical Engineering Research Scholars (TUBERS) 
Program is dedicated to providing unique and rewarding research experiences at Tufts for dedicated, academically-talented high school students. </p><div class="divider-2 card-events"></div>
<div class="card-event-details-wrapper"><div class="event-date-wrapper">
<div class="event-date"><div class="event-details-text category-text">Field: </div>
<div fs-cmsfilter-field="field" class="event-details-text">Engineering</div></div>
<div class="event-date"><div class="event-details-text category-text">Type: </div>
<div fs-cmsfilter-field="type" class="event-details-text">Research</div></div>
<div class="event-date"><div class="event-details-text category-text">Mode: </div><div fs-cmsfilter-field="mode" class="event-details-text">In-person</div></div></div><div class="event-date-wrapper"><div class="event-date"><div class="event-details-text category-text">Location:</div><div class="event-details-text">Massachusetts</div></div><div class="event-date"><div class="event-details-text category-text">Season:</div><div fs-cmsfilter-field="season" class="event-details-text">Summer</div></div><div class="event-date"><div class="event-details-text category-text">Grade:</div><div class="event-details-text">Junior, Senior</div></div></div><div class="event-date-wrapper"><div class="event-date"><div class="event-details-text category-text">Organization:</div><div class="event-details-text">Tufts University</div></div><div class="event-date"><div class="event-details-text category-text">Selectivity:</div><div fs-cmsfilter-field="selectivity" class="event-details-text">Very Selective</div></div><div class="event-date"><div class="event-details-text category-text">Cost:</div><div fs-cmsfilter-field="cost" class="event-details-text">Free Summer Program</div></div></div></div></div></div></div>
'''
# Iterate through each event element and extract information
for event_element in event_elements:
    event_details = {
        "title": event_element.select_one('h2.title.card-event').text.strip(),
        "description": event_element.select_one('p').text.strip(),
        "url":event_element.select_one('a.card-title-link').get('href'),
        "field": event_element.select_one('div.event-details-text:contains("Field:") + div').text.strip(),
        "type": event_element.select_one('div.event-details-text:contains("Type:") + div').text.strip(),
        "mode": event_element.select_one('div.event-details-text:contains("Mode:") + div').text.strip(),
        "location": event_element.select_one('div.event-details-text:contains("Location:") + div').text.strip(),
        "season": event_element.select_one('div.event-details-text:contains("Season:") + div').text.strip(),
        "grade": event_element.select_one('div.event-details-text:contains("Grade:") + div').text.strip(),
        "organization": event_element.select_one('div.event-details-text:contains("Organization:") + div').text.strip(),
        "selectivity": event_element.select_one('div.event-details-text:contains("Selectivity:") + div').text.strip(),
        "cost": event_element.select_one('div.event-details-text:contains("Cost:") + div').text.strip(),
    }
    event_details["title"] = event_details["title"].encode('ascii', 'ignore').decode('utf-8')
    event_details["description"] = event_details["description"].encode('ascii', 'ignore').decode('utf-8')
    
    # Create a 'tags' array and append selected fields
    event_details['tags'] = [
        event_details['field'],
        event_details['type'],
        event_details['mode'],
        event_details['location'],
        event_details['season'],
        event_details['grade'],
        event_details['organization'],
        event_details['selectivity'],
        event_details['cost']
        
        
        # Add more fields if needed
    ]
    
    # Remove the individual fields from the dictionary
    del event_details['field'],
    del event_details['type'],
    del event_details['mode'],
    del event_details['location'],
    del event_details['season'],
    del event_details['grade']
    del event_details['organization']
    del event_details['selectivity']
    del event_details['cost']
    
    
    
    
    events_list.append(event_details)

# Convert the list of events to a JSON string
json_data = json.dumps(events_list, indent=2)

print(json_data)
# Save the JSON data to a file named 'events.json'
with open('./envision.json', 'w') as json_file:
    json_file.write(json_data)
