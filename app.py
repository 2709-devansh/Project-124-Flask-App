from flask import Flask, jsonify, request

app = Flask(__name__)
contactList = [
    {
        "ID":"1",
        "Name":"Devansh",
        "Conatct Number":"7415675745",
        "Done":False
    },

    {
        "ID":"2",
        "Name":"Ram",
        "Conatct Number":"9863574195",
        "Done":False
    }
]

@app.route('/')
def hello():
    return """PROJECT 124 - STORING CONTACTS, TYPE GET DATA AFTER THE LINK
    TO SEE THE CONTACT LIST, AND GO TO POSTMAN AND TYPE ADD DATA AFTER THE LINK TO ADD A CONTACT""" 

@app.route('/get-data')    
def getdata():
    return jsonify({
        "Data":contactList
    })

@app.route('/add-data', methods = ["POST"])
def addData():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "Message":"Provide some data"
        }, 404)
    contact = {
        "ID":request.json["ID"],
        "Name":request.json["Name"],
        "Conatct Number":request.json["Contact Number"],
        "Done":False
    }
    contactList.append(contact)
    return jsonify({
        "Status":"Success",
        "Message":"Uploaded Succesfully"    
    })

if __name__ == '__main__':
    app.run(debug = True)