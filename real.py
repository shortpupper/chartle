# this is a program that takes data from a json file and it run a input loop so the users can see the results of whats most common
import json,ast


#a function that take data and give out the most probly value
def sreach(searchKey, dataList):
 #a var that make all the values in dataList to lower
 dataList = [x.lower() for x in dataList]
 # makes the sreachKey lower case
 searchKey = searchKey.lower()
 # Loop through all list items, and hide those who don't match the search query
 return [x for x in dataList if searchKey in x]


# a function that gets data from a json file and returns a list data based on the arguments passed
def getDataFromJson(jsonFile, dataQuery):
 # try to open the json file and read if it doesnt exsist then raises a File error
 try:
  #open the json file
  with open(jsonFile) as jsonFile: fileData = jsonFile.read()
 except: raise FileNotFoundError
 # a var that uses json.loads to make the data readable by the json import library
 jsonData = json.loads(fileData)
 # returns a compressed list that loops through jsonData and gets the dataQuery
 return [jsonData[str(x)][dataQuery] for x in jsonData] if type(dataQuery) == str else [([jsonData[str(x)][y] for y in dataQuery]) for x in jsonData]

# a function that returns a string to print to the console and takes data to output the string properly
def outputData(searchKey, jsonFile, dataQuery=["title", "text", "18+", "comments"]):
 # varible that gets the data using getDataFromJson
 jsonDataList = getDataFromJson(jsonFile, dataQuery)
 # varible to take the data from jsonDataList and check if its in searchKey
 matchingData = sreach(searchKey, jsonDataList[dataQuery.index("title")]) if "title" in dataQuery and type(dataQuery) == list else sreach(searchKey, jsonDataList)
 # returns matchingData if the length of dataQuery is 1
 if len(dataQuery) == 1: return matchingData
 # the variable for the string
 text = ""
 # pop where title is
 jsonDataList.pop(dataQuery.index("title"))
 # a for loop to go through the data of jsonDataList
 for dataTuple in jsonDataList:pass
  # a 


# a function that make the data it to readings from
def readData(show18plus, showMax, maxComment):#data, numbersNot
 # make the data form a json to a dict
 dataTuple = getDataFromJson(r"E:\Python\prog\how\texts.json", ["title", "text", "18+", "comments"])
 oi = []
 for v, key in enumerate(dataTuple[:showMax]):
  # if show18plus is true then show all if not then skip it
  if not show18plus and str(show18plus) != key[2]:
   #skip this loop
   continue
  ks = ast.literal_eval(key[3])[:maxComment]
  ko = f"\n\n{v}.\n{key[0]}\n{key[1]}\n"
  for v, c in enumerate(ks):
   # add it to ko
   ko += f" {v}- '{c}'\n"
  oi.append(ko)
 return oi

def fixdata(searchKey, show18plus=True, showMax=-1, maxComment=5):
 #check if the search key is in x if not then remove it
 h = [x for x in readData(show18plus=show18plus, showMax=showMax, maxComment=maxComment) if searchKey in x]
 for x in h: print(x)

#
#setup to run the user inputs
def setup():
 show18plus, showMax, maxComment = False, -1, 5
 user = "guest"
 fiel = r"E:\Python\prog\how\fead.txt"
 oks = "commands:\n -search  ~ment to search for the whatever\n -show18plus  ~there are things that may have not the best words in them\n -showMax  ~uh shows the max searchs that show up\n -maxComment  ~the maximun amount of comments that are showen\n -foreverSearch  ~you cant use the other commands except for exit\n -exit  ~what do you think it does? if you realy dont know then,\n its the only why for you to deafet the foreverSearch in your battle on you can stop useing this\n -help  ~with this you can call the dungeon master\n to help you or to just annoy them & more users? or uses are that there is a 1/5,000\n chance to spawn a shiny angry DUNGEON master and a 1/500,000 chance to be insulted and theres\n a 1/5 chance that explosions apear and there is a 1/2 chance that you have\n read this and a 1/4 chance that you know who made this and a 1/24899 chance that a shiny command apears\n -feedBack  ~tell me what you have to say i might read it if im board\n -signup  ~if you don't have an account then f in the channel, chart, chat, and chartle\n or text me on my discord\n -getDevInfo  ~has my gmail and discord"
 print(oks)
 # a while loop to run forever until the users exits
 while True:
  # print the commands
  # get the user input
  inp = input("meun> ")
  # if the user types exit then break the loop
  if inp == "exit": break
  # elif the user types getDevInfo then print my info
  elif inp == "getDevInfo": print("Discord: chartledev#5586\nGmail: chartledev@gmail.com")
  #elif the user types search
  elif inp == "search":
   # get the user input to search
   inp = input("search> ")
   # run the function to print it
   fixdata(inp, show18plus, showMax, maxComment)
  #elif the user types show18plus
  elif inp == "show18plus":
   print(show18plus)
   # get the user input
   print("you can type 1 or 0, 1 for True and 0 for False, or type True or False")
   inp = input("show18plus> ")
   # try if the input an int
   try:
    inp = int(inp)
    if inp: show18plus = True
    elif not inp: show18plus = False
   except:
    inp = inp.lower()
    inp = inp[0].upper()+inp[1:]
    if bool(inp): show18plus = True
    elif not bool(inp): show18plus = False
  #elif the user types showMax
  elif inp == "showMax":
   print(showMax)
   inp = input("showMax> ")
   try: showMax = int(inp)
   except: print("there was an error")
  #elif the user types maxComment
  elif inp == "maxComment":
   print(maxComment)
   inp = input("maxComment> ")
   try: maxComment = int(inp)
   except: print("there was an error")
  # elif the user types foreverSearch
  elif inp == "foreverSearch":
   while True:
    inp = input("foreverSearch> ")
    # if the user types exit break loop
    if inp == "exit": break
    else: fixdata(inp, show18plus, showMax, maxComment)
  #elif the user types help
  elif inp == "help":
   print("no")
   print(oks)
  #elif the user types feedBack
  elif inp == "feedBack":
   inp = input("feedBack> ")
   try:
    with open(fiel, "a", encoding="utf-8", errors="ignore") as f: f.write(f"{user} says'{inp}'")
   except: print("there was an error")
  # elif the user types signup
  elif inp == "signup": print("no")
  #elif the user types test
  elif inp == "test": print(readData(show18plus, showMax, maxComment))
  

setup()
"""
from cryptography.fernet import Fernet
import os

with open("E:\Python\prog\how\mainf.py") as f: message = f.read()

key = b'sIefObIeq3cw2TbZ6qMwqIswtT2DcCZVurl4azWhFDg='

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())
 
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage[:12  ])
#b'gAAAAABiU40n95jQzvnHJawPoeUm7M2YBxw0ITqsK6Q6OBQlcwprWaK-yC7z-muPdETS6ON_9XYPdo2Bk_tBQpR2r70ssyVl7Q=='

"""
