import json
#pass dictonary in string format
odics = '{"K1": "val1", "K2": "val2"}'

#result
json_result = json.loads(odics)
print(json_result['K1'])

#REST API testing:

#Get - fetch data from app
#Post - Add new data/resource to app
#Put - update data into app
#Delete - Delete data in app
#Patch - similar to PUT method but will require only updated data to send

#Head - fetch only header data from app
#options-findout which request methods a server supports
#(Allow: options, get, head,post)
#Trace: This performs a message loop-back means
#it will return message content as reponse providing a useful debugging mechanism

#http://www.omdbapi.com/?t=Spiderman&v=&plot=short&r=json
