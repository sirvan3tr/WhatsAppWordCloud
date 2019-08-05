#Extremely simple script to cleanup the conversation data that WhatsApp generates
#You can email yourself the conversation from your WhatsApp mobile application, run this script and use any popular word cloud generator like http://www.wordle.net/create.
#TO DO: Include code to create wordcloud as well. Possibly https://github.com/atizo/PyTagCloud or https://github.com/amueller/word_cloud
#Usage: python WhatsAppCleaner.py Foo.txt

from sys import argv
script, filename = argv
arr = []
f = open(filename,'r')
for line in f:
 try:
  temp = line.split(': ')[1];
  if('Media' not in temp): # If any form of media is sent, WhatsApp prints "<Media Omitted>". Getting rid of this. TO DO: Improve this functionality. 
   arr.append(temp)
 except:
     print " "
f.close()


f= open("whatsappchat.txt","w+")
#f=open("guru99.txt","a+")
for i in arr:
    f.write(i)
f.close()   
#Open the file back and read the contents
#f=open("guru99.txt", "r")
#   if f.mode == 'r': 
#     contents =f.read()
#     print contents
#or, readlines reads the individual line into a list
#fl =f.readlines()
#for x in fl:
#print x