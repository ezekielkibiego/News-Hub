from flask import render_template
from . import main

from ..requests import get_sources,get_articles


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_source = get_sources()
    # print("sources" ,popular_sources)
    
    

    title = 'Home - Welcome to Online News Website'
    return render_template('index.html', title = title, popular_sources = popular_source )

@main.route('/articles/<sources_id>')
def articles(sources_id):
    articles = get_articles(sources_id)
    print(articles)

    return render_template('articles.html',articles = articles)