#!/usr/bin/env python

import HTMLParser
from urllib import urlopen, quote

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class titlefinder(HTMLParser):
    #self.start_title=0
    #self.title = ''
    #self.stop_title=0    
    def __init__(self):        
        HTMLParser.__init__(self) # http://stackoverflow.com/a/9698750
        self.start_title=0
        self.title = ''
        self.stop_title=0
        
    def get_title(self):
        return self.title
    def handle_starttag(self, tag, attrs):
        if tag == 'title': self.start_title = 1
    def handle_endtag(self, tag):
        if tag == 'title': self.stop_title = 1
    def handle_data(self, data):
        if (self.start_title and not self.stop_title):
            self.title = data

def wikilink(word):
    url = "http://wiki.guildwars2.com/wiki/" + quote(str(word))
    print url
    response = urlopen(str(url))
    html = response.read()
    #print html
    find_title = titlefinder()
    find_title.feed(html)
    print find_title.get_title()
    rep_code = response.code
    #rep_code = urlopen(str(url)).code

    if rep_code == 200:
        # Was a great succes!
        print "Succes"
    else:
        print "failed errorcode: " + str(rep_code)
        
wikilink("charr")




# instantiate the parser and fed it some HTML
parser = titlefinder()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
print "what"
print parser.get_title()
print "that"