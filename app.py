from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World !!"

# [] => list 
# {:} => dictionary
contact = [
    {
        "id" : 1,
        "Name": "Matthew",
        "Contact": "8700578914",
        "done": False
    },
    {
        "id" : 2,
        "Name": "Yennifer",
        "Contact": "9783376298",
        "done": False
    }
]

@app.route("/add-contact", methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data in the desired format"
        })
    new_contact = {
        'id':contact[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False

    }
    contact.append(new_contact)
    return jsonify({
        'status': 'success',
        'message': 'contact added successfully'
    })

@app.route('/get-data')
def get_contact():
    return jsonify({
        'data': contact
    })

# __ => dunder
if (__name__ == "__main__"):
    app.run(debug = True)






