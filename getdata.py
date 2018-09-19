import requests, json

# eBird documentation: https://documenter.getpostman.com/view/664302/ebird-api-20/2HTbHW#intro

# get the API key from a safe place
with open('key.txt','r') as myfile:
	key = myfile.readline()
	key = key.rstrip()

# I happen to know, from spying on the eBird site, that Allegheny County
# has an ID of US-PA-003 - see: https://ebird.org/region/US-PA-003
loc_id = 'US-PA-003'
payload = {'key': key}

r = requests.get('https://ebird.org/ws2.0/data/obs/%s/recent/notable'%loc_id, params=payload)
if r.status_code == 200:
	data = json.loads(r.text)
	for item in data: # data is a list of dictionaries, cool
		print('Someone saw a %(comName)s at %(locName)s at %(obsDt)s' %item)