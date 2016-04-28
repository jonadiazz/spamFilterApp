import sys
from Tkinter import *
from xml.dom import minidom
from collections import Counter
import re



xmldoc = minidom.parse('/Users/drifter/Desktop/spamFilterApp/emails.xml')
emails = xmldoc.getElementsByTagName('email')

f = open('/Users/drifter/Desktop/spamFilterApp/BOWBad.txt', 'r+')
f2 = open('/Users/drifter/Desktop/spamFilterApp/BOWGood.txt', 'r+')

content = f.readlines()
content2 = f2.readlines()

spamWords = [c.strip() for c in content]
hamWords = [c.strip() for c in content2]

#def getText(nodelist):
#    rc = []
#    for node in nodelist:
#        rc.append(node.childNodes[0].nodeValue)
#    return rc

fromsObjs = []
messageObjs = []
for em in emails:
    fromAddress = em.getElementsByTagName('from')[0]
    msgObjs = em.getElementsByTagName('message')[0]
    fromsObjs.append(fromAddress)
    messageObjs.append(msgObjs)

froms = []
messages = []
for a in range(len(fromsObjs)):
    nodesFroms = fromsObjs[a].childNodes
    nodesMessages = messageObjs[a].childNodes

    for node in nodesFroms:
        froms.append(node.data)
    for node in nodesMessages:
        messages.append(node.data)

#def getwordbins(words, msg):
#    cnt = Counter()
#    for word in words:
#        cnt[word] = cnt[word] + 1
#    return cnt

def MARK(message):
    ham = 0
    spam = 0
    ocurrences = message.split()

    for wurd in spamWords:
        if wurd in ocurrences:
            spam = spam + ocurrences.count(wurd)

    for word in hamWords:
        if word in ocurrences:
            ham = ham + ocurrences.count(word)

    if spam > ham:
        return " :SPAM"
    return " :HAM"


def callback(*event):
    email = mylist.get(mylist.curselection()[0])
    for x in range(len(froms)):
        if froms[x] == email:
            var.set(messages[x] + MARK(messages[x]))

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.title("spamFilterML")
#Button(root, text="Make me a Sandwich").pack()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for f in froms:
    mylist.insert(END, f)

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

var = StringVar()
label = Message( root, textvariable=var, width=900)
label.pack()

mylist.bind("<<ListboxSelect>>", callback)

mainloop()

