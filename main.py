
from flask import Flask, render_template, request
import sqlalchemy as sqla
# import numpy as np
# import sqlite3 as sq
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)
db = sqla.create_engine('sqlite:///zillow.db')
df = pd.read_sql('SELECT * FROM zillow', db, parse_dates=['Date'])
#df = pd.read_csv('/../Resources/combined_zillow.csv')
df['Year'] = df['Date'].dt.year


def TN_House_Predictor(City,Bedrooms,Year):
    df_func = df.loc[(df['Bedrooms'] != 0) & (df['RegionName'] == City)]
    features = ['Bedrooms','Year']
    output_label = 'Price'
    x_train, x_test, y_train, y_test = train_test_split(
        df_func[features],
        df_func[output_label],
        test_size = 0.3)
    model = LinearRegression()
    model.fit(x_train, y_train)
    data = {'Bedrooms': [Bedrooms],'Year': [Year]}
    df2 = pd.DataFrame(data)
    y_test=model.predict(df2)
    return y_test


@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/predictor')
def predictor():
    return render_template('/predictor.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/map')
def map():
    return render_template('/map.html')


@app.route('/county')
def county_price():
    return render_template('/county.html')


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

@app.route('/handle-form', methods=['POST'])
def handle_form():
    
    if request.method == 'POST':
        city = request.form['city']
        beds = request.form['bedrooms']
        year = request.form['year']
        prediction = TN_House_Predictor(city, beds, year)
        # use your pickled model with the user input
        # to generate a new prediction
        return f'${float(prediction[0]):,.2f}' 


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    # app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    app.run(debug=False)