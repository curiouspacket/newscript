
import feedparser
from flask import Flask

app = Flask(__name__)

PP_FEED = "https://feeds.packetpushers.net/packetpushersfullfeed/"

RSS_FEEDS = {'pp' : 'https://feeds.packetpushers.net/packetpushersfullfeed/',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss'}


@app.route("/")

@app.route("/pp")
def get_pp():
    return get_news('pp')

@app.route("/cnn")
def get_ccn():
    return get_news('cnn')



def get_news(publication):
    feed = feedparser.parse(PP_FEED)
    first_article = feed['entries'][0]
    return """<html>
        <body>
        <h1>Packet Pushers News</h1>
        <b>{0}</b> <br />
        <i>[1]</1> <br />
        <p>[2]</p> <br />
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))
    





if __name__ == '__main__':
    app.run(port=5000, debug=True)

