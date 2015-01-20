import sqlite3
from scrapy import log


# Adds scraped data to Sqlite3 scrapedata.db
class Sqlite3Pipeline(object):
    # Connect to DB and creates if necessary.
    def __init__(self):
        self.connection = sqlite3.connect('./data.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS scrapedata '
                    '(id INTEGER PRIMARY KEY, module VARCHAR(120), url VARCHAR(120), available INTEGER)')

    # Take the item and put it in database - do not allow duplicates
    def process_item(self, item, spider):
        self.cursor.execute("select * from scrapedata where url=?", (item['url'],))
        result = self.cursor.fetchone()
        if result:
            log.msg("{0} already in database.".format(item['module']), level=log.DEBUG)
        else:
            self.cursor.execute(
                "insert into scrapedata (module, url, available) values (?, ?, 1)", (item['module'], item['url']))
            self.connection.commit()
            log.msg("{0} stored successfully!".format(item['module']), level=log.DEBUG)
        return item




