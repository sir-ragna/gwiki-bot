#!/usr/bin/env python
import irc, HTMLParser
from urllib import urlopen, quote
from urlopen_test import titlefinder


def wikilink(word, chan):
    url = "http://wiki.guildwars2.com/wiki/" + quote( str(word) )
    response = urlopen(str(url))
    rep_code = response.code    #response code
    
    if rep_code == 200:
        # Was a great succes!
        # zoek title
        html = response.read()
        find_title = titlefinder()
        find_title.feed(html)
        title =  find_title.get_title()
        if (' - ' in title):
            title = title.split(' - ', 1)[0]
        MyConn.send_string("PRIVMSG %s :%s %s" % (chan, title, url))
    else:
        MyConn.send_string("PRIVMSG %s :Error: %s" % (chan, str(rep_code)))
        
# Define event listeners.
def handle_state(newstate):
    if newstate==4:
        MyConn.send_string("JOIN %s" % channel)

def handle_raw(line):
    print line

def handle_parsed(prefix, command, params):
    if command=="PRIVMSG":
        if params[1]=="!help":
            MyConn.send_string("PRIVMSG %s :!gw <search> | will search gw2 wiki" % params[0])
            return
        #if(params[0]==channel ):
            #if params[1]=="hi":MyConn.send_string("PRIVMSG %s :Hello World!" % channel)

        if params[1]=="!quit":
            #MyConn.send_string("QUIT :%s" % quit_reason) # heeft geen gracefull shutdown
            return
        
        if not ' ' in params[1]: return
        (command, line) = params[1].split(' ', 1)
        
        if '!gw' == command:
            wikilink(line.strip(), params[0])
        

# Connect as usual.
MyIRC=irc.IRC_Object( )
MyConn=MyIRC.new_connection( )
MyConn.nick="gw2_bot"
MyConn.ident="gwiki_py"
MyConn.server=("irc.chat.be", 6667)
MyConn.realname="GW2 wiki Bot"
channel="#chathere"
quit_reason="Bye Bye was a fun time."

# Before starting the main loop, add the event listeners.
MyConn.events['state'].add_listener(handle_state)
MyConn.events['raw'].add_listener(handle_raw)
MyConn.events['parsed'].add_listener(handle_parsed)

while 1:
    MyIRC.main_loop( )