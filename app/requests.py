import urllib.request
import json
from .models import Sources, Articles


api_key = ''

sources_url_sources = None

sources_url_articles = None


def configure_requests(app):
    global api_key, sources_url_sources, sources_url_articles
    sources_url_sources = app.config['NEWS_API_SOURCES_URL']
    sources_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']


def get_sources():
    '''
    Function that gets the json response to url request
    '''
    get_sources_url= 'https://newsapi.org/v2/sources?apiKey=d90f1979a57b49d681affbc8c311ccca'
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


def process_results_articles(articles_list):
    '''
    Function that processes the articles list result and transform them to a list of Objects
    '''
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')


        if urlToImage:
            articles_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(articles_object)

    return articles_results


def get_articles(sources_id):
    '''
        Function that gets the json response to our url request using the source id
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=d90f1979a57b49d681affbc8c311ccca'.format(
        sources_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None
        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)

        print(articles_results_list)
        
    return articles_results












    