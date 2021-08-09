# Team Centennial Project!

## Team Roles
* Square - Thomas - GitHub
* Circle - Chris - SQL
* Triangle - Shana - Machine Learning
* X - Adam - Everything else

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
* [Tableau Public Dashboard](https://public.tableau.com/views/TNHousingForecastandMap/TN_House_Forecast?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
* This an option for the user of the final website to play around with the data.

### Week 1 for Machine Learning
* Created basic plan for machine learning processing of the data.
* Included different aspects that need to be considered during the process.
* Based on the dataset, different models and strategies will be tried.

#### Dataset Description
Data provided on Kaggle: https://www.kaggle.com/paultimothymooney/zillow-house-price-data?select=Sale_Prices_City.csv. This data is U.S. housing market compiled from zillow.com.   
#### Format


## Data Choice

#### Team Centennial park chose data that useful to anyone looking to purchase a home in Tennessee. We will focusing the data to look specifically at this market but it could be used for other states. We will building a machine learning model to help predict the future prices of houses of varying sizes.
