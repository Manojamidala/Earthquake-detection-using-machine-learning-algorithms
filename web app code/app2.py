from flask import Flask, render_template, request
import pandas as pd
import joblib


app = Flask(__name__)

# Load the pre-trained machine learning model
rf = joblib.load('rf_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input values from the form
    longitude = float(request.form['longitude'])
    latitude = float(request.form['latitude'])
    depth = float(request.form['depth'])
    cdi = float(request.form['cdi'])
    mmi = float(request.form['mmi'])
    sig = float(request.form['sig'])
    dmin = float(request.form['dmin'])
    nst = float(request.form['nst'])
    gap = float(request.form['gap'])

    # Create a dictionary with the input values
    data = {'longitude': longitude, 'latitude': latitude, 'depth': depth, 'cdi': cdi, 'mmi': mmi, 'sig': sig,
            'dmin': dmin, 'nst': nst, 'gap': gap}
    df = pd.DataFrame(data, index=[0])

    # Use the pre-trained model to make a prediction
    val = rf.predict(df)

    # Map the predicted value to a magnitude category
    if val == 'orange':
        magnitude = 'high '
    elif val == 'green':
        magnitude = 'low'
    elif val == 'yellow':
        magnitude = 'medium'
    elif val == 'red':
        magnitude = 'very high'

    # Render the prediction result template with the predicted magnitude category
    return render_template('result.html', magnitude=magnitude)

if __name__ == '__main__':
    app.run(debug=True)
