
import feedparser
from flask import Flask
import helloworld

app = Flask(__name__)


RSS_FEEDS = {'cisco' : 'http://newsroom.cisco.com/data/syndication/rss2/enterprise_networking_20.xml',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss'}


@app.route("/")

@app.route("/cisco")
def get_cisco():
    return get_news('cisco')

@app.route("/cnn")
def get_ccn():
    return get_news('cnn')
@app.route("/hello")
def get_hello():
    return helloworld.sayhello()

def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
        <h1>News</h1>
        <b>{0}</b> <br />
        <i>[1]</1> <br />
        <p>[2]</p> <br />
        </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))
    





if __name__ == '__main__':
    app.run(port=5000, debug=True)

