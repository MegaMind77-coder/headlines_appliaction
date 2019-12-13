import feedparser

from flask import Flask
from flask import render_template

app = Flask(__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'}


def get_news(website):
    feed = feedparser.parse(RSS_FEEDS[website])
    return render_template('home.html', articles=feed['entries'])


@app.route("/")
@app.route("/bbc")
def bbc_news():
    return get_news('bbc')


@app.route("/cnn")
def cnn_news():
    return get_news('cnn')


@app.route("/fox")
def fox_news():
    return get_news('fox')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
