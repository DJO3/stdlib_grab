import os
import sys
import random
import sqlite3
import webbrowser

# For scrapy spider to work within script
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from stdlib_grab.spiders.stdlib_grab_spider import StdlibGrabSpider
from scrapy.utils.project import get_project_settings


# Locates new module on PYMOTW
class GrabModule:

    def __init__(self):
        self.connection = sqlite3.connect('./data.db')
        self.cursor = self.connection.cursor()
        self.rows = None
        self.row = None

    def set_rows(self):
        self.cursor.execute("SELECT * FROM scrapedata WHERE available=1")
        self.connection.commit()
        self.rows = self.cursor.fetchall()

    def get_row(self):
        self.row = random.choice(self.rows)

    def remove_availability(self):
        self.cursor.execute("UPDATE scrapedata SET available=? WHERE Id=?", (0, self.row[0]))
        self.connection.commit()

    def open_url(self):
        webbrowser.open(self.row[2])

    def find_and_load(self):
        self.set_rows()
        self.get_row()
        self.remove_availability()
        self.open_url()
        sys.exit()


def main():
    if not os.path.exists("data.db"):
        spider = StdlibGrabSpider(domain='pymotw.com')
        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start()
        reactor.run()
    link = GrabModule()
    link.find_and_load()


if __name__ == '__main__':
    main()