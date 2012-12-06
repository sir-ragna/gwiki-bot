#!/usr/bin/env python

from math import floor
from urllib import urlopen
import json

## Haal Gold, Silver & Copper uit de verkregen integer
def seperate_coins(x):
    Gold   = int(floor(x/10000))
    Silver = int(floor((x-(Gold*10000))/100))
    Copper = int(floor(x-(Gold*10000)-(Silver*100)))
    print str(x) + "=X || " + str(Gold) + "Gold " + str(Silver) + "Silver " + str(Copper) + "Copper"
    return (Gold, Silver, Copper)

##
## START MAIN PROGRAM
##

## gem from: http://www.gw2spidy.com/gem | http://goo.gl/sW0FB
url = 'http://www.gw2spidy.com/api/v0.9/json/gem-price' # gem price url
source = 'http://goo.gl/sW0FB' #http://www.gw2spidy.com/gem

result = urlopen(url) # haal de JSON op
if result.code != 200:
    print "Error while loading gem course: " + str(result.code)
    exit(1) # <- moet maar een return statement worden later

print "results are in"
jayson = result.read() # print resultaat af
print jayson

## nu de json
decoded = json.loads(jayson) # decode
gem_to_gold = int(decoded['result']['gem_to_gold'])
gold_to_gem = int(decoded['result']['gold_to_gem']) 

message = "100 Gems sell for %dG %dS %dC, " % seperate_coins(gem_to_gold)   # add gems to coins
message += "%sG %sS %sC buy 100 Gems" % seperate_coins(gold_to_gem)         # add coins to gems
message += "| %s" % source                                                  # add source
print message, 'length:', len(message) , 'maxlen:', len('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


## Gem koers naar string omzetten
#x = int('13400') # int(gem_to_gold
#while x > 5:
#    Gold = int(floor(x/10000))
#    Silver = int(floor((x-(Gold*10000))/100))
#    Copper = int(floor(x-(Gold*10000)-(Silver*100)))
#    print str(x) + "=X || " + str(Gold) + "Gold " + str(Silver) + "Silver " + str(Copper) + "Copper"
#    x = x - 3
#exit(0)
#print "gold %dG%dS%dC" % (floor(int(gem_to_gold)/10000), floor(int(gem_to_gold)/100), floor(int(gem_to_gold)/10))

