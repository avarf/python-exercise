import urllib.parse
import requests
import json

main_api = 'https://www.google.com/finance/info?q='
query_type = 'CURRENCY'
query_subject = 'GBPUSD'

# url = main_api+query_type+':'+query_subject

url = 'https://www.google.com/finance/info?q=CURRENCY:GBPUSD'

print(url)

# json_data = requests.get(url).json()
json_data = requests.get(url)

print(type(json_data))

"print raw data"
print(json_data.text)
# print(type(json_data.text))
text_data = json_data.text
text_data2 = str(text_data).strip("'<>() ").replace('\'', '\"')

# print (text_data2)

print (json_data.encoding)
# print (json_data.content)
print (json_data.status_code == requests.codes.ok)

"We can view the server's response headers using a Python dictionary:"
print (json_data.headers)


print('***************************************')
m = json.dumps(text_data)
o = json.loads(m)

print(o)
# print (o)

print('***************************************')
new_str = text_data[4:]
print (new_str)

print(json.loads(new_str))
print('***************************************')


"the proper way to work with json and data"
valid_json_data = json.loads(new_str)
json_dict = valid_json_data[0]
print (json_dict['e'])
print (json_dict['t'])
print (json_dict['l'])


"There's also a builtin JSON decoder, in case you're dealing with JSON data:"
# print (json.loads(json_data.text))
# print (json.loads(text_data2))

