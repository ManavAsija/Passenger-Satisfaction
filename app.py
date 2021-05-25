from flask import Flask, app, render_template, request
import pickle
import numpy as numpy
app=Flask(__name__)

model =  pickle.load(open("random_forest.pkl",'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        customer_type = request.form['customer_type'] 
        class_type = request.form['class_type']
        travel_type = request.form['travel_type']
        inflight_wifi_service = request.form['inflight_wifi_service']
        ease_of_online_booking = request.form['ease_of_online_booking']
        food_and_drink = request.form['food_and_drink']
        online_boarding = request.form['online_boarding']
        seat_comfort = request.form['seat_comfort']
        inflight_entertainment = request.form['inflight_entertainment']
        onboard_service = request.form['onboard_service']
        leg_room = request.form['leg_room']
        baggage_handling = request.form['baggage_handling']
        checkin_service = request.form['checkin_service']
        inflight_service = request.form['inflight_service']
        cleanliness = request.form['cleanliness']

    else:
        prediction = model.predict([['inflight_wifi_service', 'ease_of_online_booking', 'food_and_drink', 'online_boarding','seat_comfort','inflight_entertainment', 'onboard_service','leg_room','baggage_handling','checkin_service','inflight_service','cleanliness','customer_type','travel_type','class_type']])
        return render_template("index.html",predict=prediction)

    


if __name__=="__main__":
    app.run(debug=True)