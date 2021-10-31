from flask import render_template
from app import app
from .requests import get_sources


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

@app.route('/articles/<int:article_id>')
def articles(article_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('articles.html',id = article_id)
    