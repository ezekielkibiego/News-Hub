from flask import render_template
from app import app
from .requests import get_articles, get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    popular_source = get_sources()
    # print(source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular_sources = popular_source)

@app.route('/news-sources/articles/<sources_id>')
def articles(sources_id):
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles(sources_id)
    title = f'{sources_id}'

    return render_template('articles.html', title=title, articles=articles)
