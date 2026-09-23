import requests
import json

# Fireball Data API shows every fireball or bright meteor that has been detected by Jet Propusion Laboratory
# Sorted for events after January 1st, 2026 with an associated location

response = requests.get("https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2026-01-01&req-loc=true") 
print(response.status_code)

# print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())