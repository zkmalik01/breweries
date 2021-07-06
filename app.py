from flask import Flask
import requests
import json

app = Flask(__name__)

def parsing(url): #Parses JSON files 
    response = requests.get(url) #gets the url
    text = json.dumps(response.json(), sort_keys=True, indent=4) #Cleans the output
    clean = json.loads(text) #decodes json file and returns a list
    return clean

@app.route('/list', methods=['GET'])
def list():
    breweries = parsing("https://raw.githubusercontent.com/openbrewerydb/openbrewerydb/master/breweries.json") #Print the list of breweries from the API's dataset 
    x = 0
    values = []
    jsonValues = {}
    while x <= len(breweries)-1: #iterates on all the brewerie names 
        print(breweries[x]['name']) #print the name by it's index - x is the index
        values.append(breweries[x]['name'])
        x += 1 #increment the index 
    jsonValues['values']=values
    return jsonValues

@app.route('/searching/<search>', methods=['GET']) #enter the search phrase in the URL e.g. /searching/dog
def searching (search):
   #name = input("Enter Brewerie Name: ") 
    search = parsing("https://api.openbrewerydb.org/breweries/search?query={0}".format(search))
    y = 0
    values = []
    jsonValues = {}
    while y <= len(search)-1:
        print(search[y]['name'])
        values.append(search[x]['name'])
        y += 1
    jsonValues['values']=values
    return jsonValues

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1, port = 5000')

while True: #Infinite loop
    x = int(input("Enter (1) for a list of Breweries or (2) to search Breweries or (3) to exit: ")) 
    if x  == 1:
        list()
    elif x == 2:
        searching()
    elif x == 3:
        break 