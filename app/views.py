from flask import render_template
from app import app
from .requests import get_sources,get_articles


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_source = get_sources()
    # print("sources" ,popular_sources)
    business_news = get_sources()
    sport_news = get_sources()
    

    title = 'Home - Welcome to Online News Website'
    return render_template('index.html', title = title, popular_sources = popular_source,business = business_news,sport = sport_news )

@app.route('/articles/<source_id>')
def articles(source_id):
    articles = get_articles(source_id)
    print(articles)

    return render_template('articles.html',articles = articles)