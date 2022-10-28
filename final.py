
import requests
import json
import time
import requests_cache
import webbrowser
from yelpapi import YelpAPI

requests_cache.install_cache("yelp_cache", backend="sqlite", expire_after=86400)



yelp_api = YelpAPI('DCwDGvnwsmEqG-WcN3v-bIC_qJmWqm8ain2_6XEbrvXPtJaNLER5tWPIC7rAO_9KsJdWVmBaBgfQzu6ugbkQyyoMrfMZuLmw0GmFm01aiXRgMK0p7bsG8n0mx2s6YnYx')

api_key = 'DCwDGvnwsmEqG-WcN3v-bIC_qJmWqm8ain2_6XEbrvXPtJaNLER5tWPIC7rAO_9KsJdWVmBaBgfQzu6ugbkQyyoMrfMZuLmw0GmFm01aiXRgMK0p7bsG8n0mx2s6YnYx'
headers = {'Authorization': 'Bearer {}'.format(api_key)}

#Arts Detroit
search_api_url = 'https://api.yelp.com/v3/businesses/search'
params = {'categories': 'arts',
          'location': 'detroit, michigan',
          'limit': 50}
detroit_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
detroit = detroit_results.json()
detroit_arts = (detroit['businesses'])
detroit_arts_pop = []
detroit_arts_unpop = []
for item in detroit_arts:
    if item['review_count'] > 50:
        detroit_arts_pop.append(item)
    elif item['review_count'] < 50:
        detroit_arts_unpop.append(item)


#Active/Outoor Detroit
params = {'categories': 'active',
          'location': 'detroit, michigan',
          'limit': 50}
detroit_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
detroit = detroit_results.json()
detroit_active = (detroit['businesses'])
detroit_active_pop = []
detroit_active_unpop = []
for item in detroit_active:
    if item['review_count'] > 50:
        detroit_active_pop.append(item)
    elif item['review_count'] < 50:
        detroit_active_unpop.append(item)


#Local flavor Detroit
params = {'categories': 'localflavor',
          'location': 'detroit, michigan',
          'limit': 50}
detroit_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
detroit = detroit_results.json()
detroit_local = (detroit['businesses'])
for item in detroit_local:
    if item['review_count'] > 50:
        detroit_arts_pop.append(item)
    elif item['review_count'] < 50:
        detroit_arts_unpop.append(item)

#Arts Rural
params = {'categories': 'arts',
          'location': 'northern michigan',
          'limit': 50}
rural_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
rural = rural_results.json()
rural_arts = (rural['businesses'])
rural_arts_pop = []
rural_arts_unpop = []
for item in rural_arts:
    if item['review_count'] > 50:
        rural_arts_pop.append(item)
    elif item['review_count'] < 50:
        rural_arts_unpop.append(item)

#Local flavor rural
params = {'categories': 'localflavor',
          'location': 'northern michigan',
          'limit': 50}
rural_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
rural = rural_results.json()
rural_local = (rural['businesses'])

for item in rural_local:
    if item['review_count'] > 50:
        rural_arts_pop.append(item)
    elif item['review_count'] < 50:
        rural_arts_unpop.append(item)


#Outdoor Rural
params = {'categories': 'active',
          'location': 'northern michigan',
          'limit': 50}
rural_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
rural = rural_results.json()
rural_active = (rural['businesses'])
rural_active_pop = []
rural_active_unpop = []
for item in rural_active:
    if item['review_count'] > 40:
        rural_active_pop.append(item)
    elif item['review_count'] < 40:
        rural_active_unpop.append(item)




tree = ('Would you like to visit somewhere urban or rural? Type yes for urban and no for rural',
('Would you like to experience the arts or the outdoors? Type yes for arts and no for outdoor', 
('Would you like popular or unpopular? Type yes for popular and no for unpopular', 
(detroit_arts_pop[0]['name'], None, None), (detroit_arts_unpop[2]['name'], None, None)),
('Would you like popular or unpopular? Type yes for popular and no for unpopular', 
(detroit_active_pop[0]['name'], None, None), (detroit_active_unpop[0]['name'], None, None))),
('Would you like to experience the arts or the outdoors? Type yes for arts and no for outdoor', 
('Would you like popular or unpopular? Type yes for popular and no for unpopular', 
(rural_arts_pop[0]['name'], None, None), (rural_arts_unpop[1]['name'], None, None)),
('Would you like popular or unpopular? Type yes for popular and no for unpopular?', 
(rural_active_pop[0]['name'], None, None), (rural_active_unpop[4]['name'], None, None))))


json_string = json.dumps(tree)
with open('json_data.json', 'w') as outfile:
    json.dump(json_string, outfile)


def playLeaf(tree):
    return tree[0]

def yes(prompt):
    response = input(prompt)
    yes_words = ['yes', 'y', 'yup', 'sure']
    if response in yes_words:
        return True
    else:
        return False

def isleaf(tree):
    if type(tree[0]) == str and tree[1] == None and tree[2] == None:
        return True
    else:
        return False

def simplePlay(tree):
    if isleaf(tree) == True:
        rec = playLeaf(tree)
        return rec
    else:
        question = tree[0]
        if yes(question) == True:
            x = simplePlay(tree[1])
            return x
        else:
            x = simplePlay(tree[2])
            return x



y = simplePlay(tree)
print(f"You should visit {y}!")


#how to use scrapy?

#use flask to show other places within 10 miles to visit