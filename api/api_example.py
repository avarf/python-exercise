import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = 'lhr'
# while  True:
	# address = input('address: ')
print(address)
# if address == 'q':
# 	break
final_url = main_api + urllib.parse.urlencode({'address': address})

api_answer = requests.get(final_url).json()
# print(api_answer)
print(final_url)

answer_status = api_answer['status']

if answer_status == 'OK':
	formatted_address = api_answer['results'][0]['formatted_address']
	print(formatted_address)
	place_type = api_answer['results'][0]['types'][0]
	print(place_type)

print('Finished')