
import random
import string

from flask import Flask, request, Response
from pymongo import MongoClient
import pymongo
import json
import time

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DSAirlines']
# Choose collections
users = db['users']
users = db['users']
reservations = db['reservations']
flights = db['flights']
app = Flask(__name__)


@app.route('/createUser', methods=['POST', 'GET'])
def create_user():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content", status=500,
                        mimetype='application/json')
    if data is None:
        return Response("bad request", status=500, mimetype='application/json')
    if not "email" in data or not "username" in data or not "name" in data or not "surname" in data or not "password" or not "passport" in data:
        return Response("Information incomplete", status=500,
                        mimetype="application/json")

    # Checking email username passport
    if not (users.find_one({"email": data["email"]})) and not (users.find_one({"username": data["username"]})) and not (
    users.find_one({"passport": data["passport"]})):
        str(data["password"])
        contains_digit = False

        # Checking password length

        if len(data["password"]) >= 8:
            for characters in data["password"]:
                # Checking that password contains 1 number at least
                if characters.isdigit():
                    contains_digit = True
            if not contains_digit:
                return Response("Your password does not have a number",
                                mimetype='application/json')
            else:
                temp_passport = data['passport']

                # Dividing passport into two strings
                if len(temp_passport) == 9:
                    first_passport = slice(0, 2)
                    second_passport = slice(2, 9)
                    check_sum = 0
                    check_sum_2 = 0
                    # Checking that the first two are characters
                    for passCharacters in temp_passport[first_passport]:
                        if passCharacters.isalpha():
                            check_sum = check_sum + 1
                    # Checking that the last 7 are numbers
                    for passCharacters2 in (temp_passport[second_passport]):
                        if passCharacters2.isdigit():
                            check_sum_2 = check_sum_2 + 1
                    if check_sum == 2 and check_sum_2 == 7:
                        # Passing the data.
                        new_user = {"email": data['email'], "username": data['username'], "name": data['name'],
                                    "surname": data['surname'], "password": data['password'],
                                    "passport": data['passport'], "category": 'user', "recoveryPass": ""}
                        users.insert_one(new_user)
                        return Response(data['name'] + " was added to the MongoDB",
                                        mimetype='application/json')
                    else:
                        return Response("Your passport does not have the requirements.",
                                        mimetype='application/json')
                else:
                    return Response("Your passport does not have 9 characters)",
                                    mimetype='application/json')
        else:
            return Response("Your password does not have the minimum length of 8 characters",
                            mimetype='application/json')

    else:
        return Response("A user with the given email or username or passport already exists",
                        mimetype='application/json')  # ΠΡΟΣΘΗΚΗ STATUS#


# Login into the system
@app.route('/login', methods=['POST'])
def login():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content", status=500,
                        mimetype='application/json')
    if data is None:
        return Response("bad request", status=500, mimetype='application/json')
    if not "email" in data or not "password" in data:
        return Response("Information incomplete", status=500,
                        mimetype="application/json")

    # Checking if email exists
    if users.find_one({"email": data["email"]}):
        # Finding a user that has a matching email
        global selected_user
        selected_user = users.find_one({"email": data['email']})
        # Checking Password
        if selected_user['password'] == data['password']:
            if selected_user['category'] != "disabled":
                global user_email
                global user_category
                global user_username
                global user_name
                user_email = str(data['email'])
                user_name = str(selected_user['name'])
                user_category = str(selected_user['category'])
                if user_category != 'admin' and user_category != "newAdmin":
                    user_username = str(selected_user['username'])
                else:
                    user_username = "Admin"
                    user_name = "Admin"
                return Response(f"{user_name} Logged in.", status=200, mimetype='application/json')
            else:

                return Response("Your account is disabled.Please reactivate", status=200, mimetype='application/json')
        else:
            # Could not authenticate.
            return Response("Wrong email or password.", status=400, mimetype='application/json')
    else:
        # Could not authenticate.
        return Response("Wrong email or password.", status=400, mimetype='application/json')  # ΠΡΟΣΘΗΚΗ STATUS


# Disable the user.
@app.route('/disableThisUser', methods=['POST', 'GET'])
def disable_this_user():
    global user_category
    global selected_user
    # Empty string as temporary Password
    temp_pass = ""
    if users.find_one({"username": selected_user['username']}):
        matching_user = users.find_one({"username": selected_user['username']})
        if matching_user['category'] == 'user':

            # Generate other characters
            random_source = string.ascii_letters + string.digits
            # Creating random password
            for i in range(12):
                temp_pass += random.choice(random_source)

            password_list = list(temp_pass)
            # shuffle all characters
            random.SystemRandom().shuffle(password_list)
            temp_pass = ''.join(password_list)
            # Assigning the recovery pass
            db.users.update_one({"username": matching_user['username']},
                                {"$set": {'category': "disabled", "recoveryPass": temp_pass}})
            return Response(f"Your account has been disabled and your recovery password is {temp_pass}.", status=200,
                            mimetype='application/json')
        else:
            return Response("Your account is already disabled.", status=200, mimetype='application/json')


# Enabling the user
@app.route('/enableThisUser', methods=['POST', 'GET'])
def enable_this_user():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content", status=500,
                        mimetype='application/json')  #
    if data is None:
        return Response("bad request", status=500, mimetype='application/json')
    if not "passport" in data or not "recoveryPass" in data:
        return Response("Information incomplete", status=500,
                        mimetype="application/json")
    global userPassport
    global userTempPass
    global selected_user
    if users.find_one({"recoveryPass": selected_user['recoveryPass']}):
        matchingUser = users.find_one({"recoveryPass": selected_user['recoveryPass']})
        db.users.update_one({"username": matchingUser['username']},
                            {"$set": {'category': "user", "recoveryPass": ""}})

        return Response("Your account has been enabled.", status=200, mimetype='application/json')
    else:
        return Response("wrong", status=200, mimetype='application/json')

# Searching for the flight


@app.route('/SearchFlight', methods=['POST', 'GET'])
def search_flight():
    # Ελεγχος Χρηστη
    global user_category
    if user_category == "admin" or user_category == "newAdmin":
        return Response("Permission Denied", status=401, mimetype="application/json")
    elif user_category == "User":
        # Ελεγχος Δεδομενων
        data = None
        try:
            data = json.loads(request.data)
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "date" in data or not "departure" in data or not "destination" in data:
            return Response("Information incomplete, please fill all fields", status=500,
                            mimetype="application/json")
        else:
            # Empty lists of flights
            availableFlights = []
            flight_matching = list(flights.find({"departure": data['departure']} and
                                                {"destination": data['destination']} and {"date": data['date']}))
            if not flight_matching:
                return Response("No matching flights", status=200,
                                mimetype='application/json')
            else:
                for allFlights in flight_matching:
                    if int(allFlights['availability']) > 0:
                        availableFlights.append(allFlights)
                if availableFlights:
                    return Response(f"Your flights\n {availableFlights}", status=200,
                                    mimetype='application/json')
                else:
                    return Response("No available flights", status=200,
                                    mimetype='application/json')

# Reservations


@app.route('/makeReservation', methods=['POST', 'GET'])
def make_reservation():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content", status=500,
                        mimetype='application/json')
    if data is None:
        return Response("bad request", status=500, mimetype='application/json')
    if not "passport" in data or not "name" in data or not "credit_card" in data or not "surname" in data or not "flightID" in data:
        return Response("Information incomplete", status=500,
                        mimetype="application/json")
    # Checking Credit Card
    credit_card = data["credit_card"]
    if len(credit_card) == 16 and credit_card.isdigit():
        matchingFlight = flights.find_one({"flightID": data['flightID']})
        newReservation = {"name": data["name"], 'surname': data["surname"], 'flightID': data["flightID"]}
        reservations.insert_one(newReservation)
        return Response("Reservation added", status=201, mimetype='application/json')
    else:
        return Response("Information incomplete", status=500,
                        mimetype="application/json")


    # ADMIN

# CREATE ADMIN
@app.route('/createAdmin', methods=['POST', 'GET'])
def create_admin():
    # Checking user category
    global user_category
    if user_category == "User":
        return Response("Permission Denied", status=401, mimetype="application/json")
    elif user_category == "admin" or user_category == "newAdmin":

        # Request JSON data
        data = None
        try:
            data = json.loads(request.data)
        except Exception as e:
            return Response("bad json content", status=500,
                            mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "email" in data or not "name" in data or not "password" in data:
            return Response("Information incomplete", status=500,
                            mimetype="application/json")

        # Checking email
        if not (users.find_one({"email": data["email"]})):
            new_user = {"email": data['email'], "name": data['name'], "password": data['password'],
                        "category": 'newAdmin'}
            users.insert_one(new_user)
            return Response(data['name'] + " was added to the MongoDB", mimetype='application/json')  # ΠΡΟΣΘΗΚΗ STATUS

        else:
            return Response("An admin with the given email already exists",
                            mimetype='application/json')  # ΠΡΟΣΘΗΚΗ STATUS


# Creating flight
@app.route('/insertFlight', methods=['POST', 'GET'])
def insert_flight():
    global user_category
    global newFlight
    # Ελεγχος Χρηστη
    if user_category == "user":
        return Response("Permission Denied", status=401, mimetype="application/json")
    elif user_category == "admin" or user_category == "newAdmin":

        # Checking Data
        data = None
        try:
            data = json.loads(request.data)
        except Exception as e:
            return Response("bad json content", status=500,
                            mimetype='application/json')
        if data is None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "date" in data or not "departure" in data or not "destination" or not "cost" or not "duration" in data:
            return Response("Information incomplete", status=500,
                            mimetype="application/json")
        tempDeparture = data["departure"]
        tempDestination = data["destination"]
        tempDataDate = str(data["date"])
        # Creating unique Flight ID
        flightID = tempDeparture[0] + tempDestination[0] + tempDataDate[2:4] + tempDataDate[5:7] + tempDataDate[
                                                                                                   8:10] + tempDataDate[
                                                                                                           11:13]
        # Inserting Data
        newFlight = {"date": data["date"], 'departure': data["departure"], 'destination': data["destination"],
                     'cost': data["cost"], 'duration': data["duration"], 'availability': 220, 'flightID': flightID}
        flights.insert_one(newFlight)
        return Response("flight added in flights.", status=201, mimetype='application/json')


# Updating flight
@app.route('/updateFlight', methods=['POST', 'GET'])
def updateFlight():
    # Checking User
    global user_category
    if user_category == "user":
        return Response("Permission Denied", status=401, mimetype="application/json")
    elif user_category == "admin" or user_category == "newAdmin":

        # Checking Data
        data = None
        try:
            data = json.loads(request.data)
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "flightID" or not "cost" in data:
            return Response("Information incomplete", status=500, mimetype="application/json")

        # Updating the flight
        if flights.find_one({"flightID": data['flightID']}):
            matchingFlight = flights.find_one({"flightID": data['flightID']})
            newCost = int(data["cost"])
            if matchingFlight['availability'] == 220:
                if newCost <= 0:
                    return Response(f"flight with flightID: {data['flightID']} wasnt updated due to incorrect price",
                                    status=500,
                                    mimetype="application/json")
                # this_one = flights.find_one({"flightID": data['flightID']})
                db.flights.update_one({"flightID": data['flightID']}, {"$set": {'cost': data["cost"]}})
                return Response(f"flight with flightID: {data['flightID']} updated.", status=200,
                                mimetype='application/json')
            else:
                return Response(f"flight with flightID: {data['flightID']} wasnt updated due to availability",
                                status=500,
                                mimetype="application/json")

        else:
            return Response(f"flight with flightID: {data['flightID']} doesnt exist", status=500,
                            mimetype="application/json")


# Deleting flight
@app.route('/deleteFlight', methods=['POST', 'GET'])
def deleteFlight():
    # checking if user is admin
    global user_category
    if user_category == "User":
        return Response("Permission Denied", status=401, mimetype="application/json")
    elif user_category == "admin" or user_category == "newAdmin":
        # Checking Data
        data = None
        try:
            data = json.loads(request.data)
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "flightID" in data:
            return Response("Information incomplete", status=500, mimetype="application/json")

        if flights.find_one({"flightID": data['flightID']}):
            flights.delete_many({"flightID": data['flightID']})
            return Response("flight deleted.", status=200, mimetype='application/json')
        else:
            return Response(f"flight with flightID: {data['flightID']} doesnt exist", status=500,
                            mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

