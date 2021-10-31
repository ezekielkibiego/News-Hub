from app import app
import urllib.request,json
from .models import sources
Sources=sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the movie base url
sources_url = app.config["NEWS_API_SOURCES_URL"]

def get_sources():
    '''
    Function that gets the json response to url request
    '''
    get_sources_url= sources_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category=sources_item.get('category')
        language=sources_item.get('en')
        country=sources_item.get('country')
        if id:
            sources_object = Sources(id,name,description,url,category,language,country)
            sources_results.append(sources_object)

    return sources_results




    