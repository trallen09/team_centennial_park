# Team Centennial Project!

## Team Roles
* Square - Thomas - GitHub
* Circle - Chris - SQL
* Triangle - Shana - Machine Learning
* X - Adam - Everything else

### Week 3
* Continued working on HTML, Flask, Google Slides, Tableau
* Finalized the ML interaction with user and ML function

### Week 2
* Lessons learned
	* Properly format the date if the analysis is based on a time series.
	* This conversion of the date to time delta improved the performance of the model. 
![DeltaDate](https://github.com/trallen09/team_centennial_park/blob/main/images/DeltaDate2.png)

* Premliminary Data Processing
	* Connected to Database
	* Converted the Date column to a difference between today and historical date.
	* Dataframe was encoded using OrdinalEncoder on City, # of Bedrooms, and DeltaDate
* Split and Train
	* sklearn.model_selection was used to train_test_split the data. Default of 75% training and 25% testing was used.
* Linear Regression Model
	* A Linear Regression Model was used for this data. Housing prices typically have a straight line trend upward.
	* The historical data used did not appear to be seasonally affected.
	* Proper formatting of the date is key to utilizing this data.

* https://docs.google.com/presentation/d/1OoIsgp5mlWcPvbk-57R-t8Uln5zaWwtiQtzcT7-NKdI/edit#slide=id.p

#### Tableau Dashboard
* These dashboards provide options for the user of the final website to play around with the data.
* [Tableau Public Dashboard1](https://public.tableau.com/views/TNHousingForecastandMap/TN_House_Forecast?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
* [Tableau Public Dashboard2](https://public.tableau.com/views/TNCountyPrices/CountiesDash?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

### Week 1 for Machine Learning
* Created basic plan for machine learning processing of the data.
* Included different aspects that need to be considered during the process.
* Based on the dataset, different models and strategies will be tried.

#### Dataset Description
Data provided on Kaggle: https://www.kaggle.com/paultimothymooney/zillow-house-price-data?select=Sale_Prices_City.csv. This data is U.S. housing market compiled from zillow.com.   
#### Format


## Data Choice

#### Team Centennial park chose data that useful to anyone looking to purchase a home in Tennessee. We will focusing the data to look specifically at this market but it could be used for other states. We will building a machine learning model to help predict the future prices of houses of varying sizes.




### Data Cleaning & Database

        a. Import data utilizing Pandas from 5 .csv files obtained from zillow.com

        b. Using Jupyter Notebook, to name a few, we used the following:
	- pd.concat
	- df.stack
	- df.set_index and reset_index
	- df.rename
	- pd.to_datetime
	- df.to_csv
	- df.loc
	
	c. Import data utilizing SQLite
                i. Created 2 tables: "zillow_table1" & "zillow_table2"
        d. sqlite was used as our database (zillow.db)
                i. The database contains two tables that needed to be joined
                ii. The sql query is as follows:
		'''SELECT *
		FROM zillow_table1
		LEFT JOIN zillow_table2
		ON zillow_table1.ID = zillow_table2.ID;'''
	e. 




### Machine Learning

        a. Import data utilizing sqlite3
	
	b. Convert data to dataframe using Pandas

        c. Using Jupyter Notebook, choose Machine Learning Model
                i. We chose Linear Regression as our ML model because regression 
		   is used to predict continuous variables. Since we are trying to 
		   predict future or even past TN house prices, regression is needed.
	
	d. A function was created to take inputs from the webpage and run the predictions on the spot
	
	e. We have two features and one variable that can be changed by the user.
		i. The two features are number of bedrooms and year
		ii. The variable that will modify the dataframe going into the model is the city in TN
		
                   
               
