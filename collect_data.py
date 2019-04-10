#!/usr/local/bin/python3
import requests
import json

user_data = {}
user_data['data'] = []
api = 'https://reqres.in/api/users'

# there are 4 APIs and only the parameter of page changes
for i in range(1,5):
    req = requests.get(url=api,params={'page':i})
    status = req.status_code

    # if the api responses
    if status == 200:
        result = req.json()
        page_count = result['per_page']
        data = result['data']

        for j in range(page_count):
            record = {}
            record['id'] = data[j]['id']
            record['first_name'] = data[j]['first_name']
            record['last_name'] = data[j]['last_name']
            record['avatar'] = data[j]['avatar']
            user_data['data'].append(record)

# save file
output_file = 'user_data.txt'
with open(output_file,'w') as outfile:
    json.dump(user_data, outfile)
    print('Successfully collected the data.')


