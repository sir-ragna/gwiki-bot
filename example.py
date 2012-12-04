import irc

def handle_hi(destination):
	MyIRC.active.send_hi(destination)

MyIRC=irc.IRC_Object()
MyIRC.load_extension("extensions/helloworld")
MyConn=MyIRC.new_connection()

MyConn.nick="MauBot"
MyConn.ident="maubot"
MyConn.server=("irc.oftc.net", 6667)
MyConn.realname="Hoi"

MyConn.events['hi'].add_listener(handle_hi)

while 1:
	MyIRC.main_loop()

