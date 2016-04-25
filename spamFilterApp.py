import sys
from Tkinter import *
from xml.dom import minidom

xmldoc = minidom.parse('/Users/drifter/Desktop/spamFilterApp/emails.xml')
emails = xmldoc.getElementsByTagName('email')
#print(len(emails))
#print s.childNodes[0].nodeValue
#print(emails[0].attributes['message'].value)

def getElement(self, element):
    return self.getText(element.childNodes)

#def getText(list):
#    froms = []
#    messages = []
#    for node in list:
#        fromTitle = node.getElementsByTagName('from')[0]
#        froms.append(fromTitle)
#
#    for node in list:
#        msg = node.getElementsByTagName('message')[0]
#        messages.append(msg)
#
#    rc = []
#    for s in len(froms):
#        rc.append([])
#        for m in messages:
#            rc[s].append(m)
#        for

def getText(nodelist):
    rc = []
    for node in nodelist:
        rc.append(node.childNodes[0].nodeValue)

    return rc

#froms = emails.getElementsByTagName('from')

#print getText(froms)
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
#    nodes = fromObj.childNodes
    for node in nodesFroms:
        froms.append(node.data)
    for node in nodesMessages:
        messages.append(node.data)

#def getText(nodelist):
#    rc = []
#    for node in nodelist:
##        print node.childNodes[0].nodeValue
#        if node.childNodes[0].nodeValue != ' ':
#            rc.append(node.childNodes[0].nodeValue)
##        if node.nodeType == node.TEXT_NODE:
##            rc.append(node.data)
##    return ''.join(rc)
#    return rc
#
#messages = getText(emails)
#
#print messages[0]

#for s in emails:
#    print s.childNodes[0].nodeValue
#    print(s.attributes['message'].value)

def callback(*event):
#    print mylist.get(mylist.curselection()[0])
#    mylist.get(mylist.curselection()[0])
#    var = StringVar()
#
#    label = Message( root, textvariable=var, width=400)
#    label = Message( root, textvariable=var, relief=RAISED )
#    label.destroy()
    email = mylist.get(mylist.curselection()[0])
    for x in range(len(froms)):
        if froms[x] == email:
            var.set(messages[x])
#    var.set(msg)
#    label.pack()
#    wait(1000)
#    var.set(mylist.get(mylist.curselection()[0]))

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.title("spamFilterML")
#Button(root, text="Make me a Sandwich").pack()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for f in froms:
#    for f in m.getElementsByTagName('from'):
    mylist.insert(END, f)
#    mylist.insert(END, "EMAIL " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

#Tk()
var = StringVar()
#var = "No message selected"
label = Message( root, textvariable=var, width=600)
label.pack()

mylist.bind("<<ListboxSelect>>", callback)


#my2ndlist = Listbox(root, yscrollcommand = scrollbar.set )
#for line in range(5):
#    my2ndlist.insert(END, "EMAIL " + str(line))
#
#my2ndlist.pack( side = RIGHT, fill = BOTH)


#var.set(mylist.get(mylist.curselection()[0]))

mainloop()

