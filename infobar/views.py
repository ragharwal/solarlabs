from django.shortcuts import render

import wptools

# Create your views here.


def get_wikipedia_content(request):
    country = request.GET.get('country')
    content = wptools.page(country) # create a page object
    return content

def home(request):
    result = None
    wiki_data = []
    result = dict()

    # attributes of interest contained within the wiki infoboxes
    features = ['image_map', 'capital', 'largest_city', 'official_languages', 'population_estimate', 'GDP_PPP']

    content = get_wikipedia_content(request)    
    page = content 

    try:
        page.get_parse() # call the API and parse the data

        if page.data['infobox'] != None:
            infobox = page.data['infobox']
            data = { feature : infobox[feature] if feature in infobox else '' for feature in features }
        else:
            data = { feature : '' for feature in features }

        wiki_data.append(data)

    except KeyError:
        pass

    result['flag'] = wiki_data[0]['image_map']
    result['capital'] = wiki_data[0]['capital']
    result['largest_city'] = wiki_data[0]['largest_city']
    result['official_languages'] = wiki_data[0]['official_languages']
    result['population_estimate'] = wiki_data[0]['population_estimate']
    result['GDP_PPP'] = wiki_data[0]['GDP_PPP']
    
    return render(request, 'infobar/home.html',  {'result': result})
