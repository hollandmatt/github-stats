#!/usr/bin/env python

import requests, csv, json

with open('config.json') as data_file:
    config = json.load(data_file)

headers = {
   'Authorization': 'token ' + config['token']
}

apiRoot = 'https://api.github.com/repos/'

output = csv.writer(open(config['output'], 'wb'))
output.writerow(['Repo', 'ID', 'Description', 'Created By', 'Open Date', 'Merged By', 'Merged Date', 'Comments'])

for repo in config['repos']:
   all = apiRoot + repo + '/pulls?state=all'
   individual = apiRoot + repo + '/pulls/'

   request = requests.request('GET', all, headers=headers)
   parsed = request.json()

   for pull in parsed:
      details = requests.request('GET', individual + str(pull['number']), headers=headers).json()
      comments = requests.request('GET', individual + str(pull['number']) + '/comments', headers=headers).json()
      output.writerow([repo,
                       pull['number'],
                       pull['title'].encode('ascii', 'ignore'),
                       pull['user']['login'],
                       pull['created_at'],
                       details['merged_by']['login'] if details['merged_by'] is not None else None,
                       pull['merged_at'],
                       len(comments)])

print(str(request.headers['X-RateLimit-Remaining']) + ' requests remaining out of ' +
      str(request.headers['X-RateLimit-Limit']))
