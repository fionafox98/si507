from flask import Flask, render_template, request, redirect, url_for, abort
from matplotlib.pyplot import title
import requests
from yelpapi import YelpAPI
import numpy
import plotly
import plotly.graph_objs as go

app = Flask(__name__,template_folder='Templates')

yelp_api = YelpAPI('DCwDGvnwsmEqG-WcN3v-bIC_qJmWqm8ain2_6XEbrvXPtJaNLER5tWPIC7rAO_9KsJdWVmBaBgfQzu6ugbkQyyoMrfMZuLmw0GmFm01aiXRgMK0p7bsG8n0mx2s6YnYx')

api_key = 'DCwDGvnwsmEqG-WcN3v-bIC_qJmWqm8ain2_6XEbrvXPtJaNLER5tWPIC7rAO_9KsJdWVmBaBgfQzu6ugbkQyyoMrfMZuLmw0GmFm01aiXRgMK0p7bsG8n0mx2s6YnYx'
headers = {'Authorization': 'Bearer {}'.format(api_key)}
@app.route('/visit/detroitarts')

def find_place():
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'categories': 'arts',
          'location': 'detroit, michigan',
          'limit': 5}
    detroit_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    detroit = detroit_results.json()
    detroit_bus = []
    rating = []
    detroit_arts = (detroit['businesses'])
    for item in detroit_arts:
        detroit_bus.append(item['name'])
        rating.append(item['rating'])

    x_vals = ['Detroit Institute of Arts', 'Motown Museum', 'Comerica Park', "Cliff Bell's", 'Dessert Oasis Coffee Roasters']
    y_vals = [rating[0], rating[1], rating[2], rating[3], rating[4]]
    bars_data = go.Bar(x=x_vals, y=y_vals)
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
     #f"<h1>Here are some more destinations you should visit:<h1>  <p>{detroit1}.<p>"
    return render_template('index.html', name=detroit_bus[0], name1=detroit_bus[1], name2=detroit_bus[2], name3=detroit_bus[3],
    name4=detroit_bus[4], plot_div=div,
    list = detroit_bus)

@app.route('/visit/detroitoutdoor')

def find_outdoor():
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'categories': 'active',
          'location': 'detroit, michigan',
          'limit': 5}
    detroit_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    detroit = detroit_results.json()
    detroit_active = (detroit['businesses'])
    detroit_active_pop = []
    rating = []
    for item in detroit_active:
        detroit_active_pop.append(item['name'])
        rating.append(item['rating'])

    x_vals = ['Comerica Park', 'Campus Martius Park', 'RiverWalk', 'Belle Isle Park', 'Dequindre Cut Greenway']
    y_vals = [rating[0], rating[1], rating[2], rating[3], rating[4]]
    bars_data = go.Bar(x=x_vals, y=y_vals)
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
     #f"<h1>Here are some more destinations you should visit:<h1>  <p>{detroit1}.<p>"
    return render_template('index2.html', name=detroit_active_pop[0], name1=detroit_active_pop[1], name2=detroit_active_pop[2], name3=detroit_active_pop[3],
    name4=detroit_active_pop[4], plot_div=div,
    list = detroit_active_pop)

@app.route('/visit/ruraloutdoor')

def rural_outdoor():
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'categories': 'active',
          'location': 'northern michigan',
          'limit': 50}
    rural_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    rural = rural_results.json()
    rural_active = (rural['businesses'])
    rural_active_pop = []
    rating = []
    for item in rural_active:
        rural_active_pop.append(item['name'])
        rating.append(item['rating'])

    x_vals = ['Sleeping Bear Dunes', 'Hooked SportFishing Charters', 'Crystal River Outfitters', 'Fishtown', 'The River Outfitters']
    y_vals = [rating[0], rating[-1], rating[2], rating[3], rating[5]]
    bars_data = go.Bar(x=x_vals, y=y_vals)
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
     #f"<h1>Here are some more destinations you should visit:<h1>  <p>{detroit1}.<p>"
    return render_template('index3.html', name=rural_active_pop[0], name1=rural_active_pop[-1], name2=rural_active_pop[2], name3=rural_active_pop[3],
    name4=rural_active_pop[5], plot_div=div,
    list = rural_active_pop)

@app.route('/visit/ruralarts')

def rural_arts():
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'categories': 'arts',
          'location': 'northern michigan',
          'limit': 50}
    rural_results = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    rural = rural_results.json()
    rural_active = (rural['businesses'])
    rural_active_pop = []
    rating = []
    for item in rural_active:
        rural_active_pop.append(item['name'])
        rating.append(item['rating'])

    x_vals = ['Cherry Republic', '45 North Vineyard and Winery', 'Cheateau Fontaine', 'Suttons Bay Ciders', 'Fragrant Isle Lavender Farm and Shop']
    y_vals = [rating[0], rating[6], rating[2], rating[3], rating[-4]]
    bars_data = go.Bar(x=x_vals, y=y_vals)
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
     #f"<h1>Here are some more destinations you should visit:<h1>  <p>{detroit1}.<p>"
    return render_template('index4.html', name=rural_active_pop[0], name1=rural_active_pop[6], name2=rural_active_pop[2], name3=rural_active_pop[3],
    name4=rural_active_pop[-4], plot_div=div,
    list = rural_active_pop)



if __name__ == '__main__': 
    app.run(debug=True)

