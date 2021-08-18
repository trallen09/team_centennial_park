# Team Centennial Park Project: Zillow Pricing Predictor

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

## Google Slide Presentation Link

* https://docs.google.com/presentation/d/1OoIsgp5mlWcPvbk-57R-t8Uln5zaWwtiQtzcT7-NKdI/edit#slide=id.p

## Link for the Dashboard Storyboard

* These dashboards provide options for the user of the final website to play around with the data.
* [Tableau Public Dashboard1](https://public.tableau.com/views/TNHousingForecastandMap/TN_House_Forecast?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
* [Tableau Public Dashboard2](https://public.tableau.com/views/TNCountyPrices/CountiesDash?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

Database Description

Data provided on Kaggle: https://www.kaggle.com/paultimothymooney/zillow-house-price-data?select=Sale_Prices_City.csv. This data is U.S. housing market compiled from zillow.com. Data included housing prices for Tennessee and was limited to city and number of bedrooms.

Format

The dataframe has 84 rows and 63 columns with the following variables:

Bedrooms

*Homes with 1-5 bedrooms were included in the database.

RegionName

*Name of the city the houses for sale were located.

Date

*Date of housing prices recorded in Zillow.

Price

*Housing price.

DeltaDate

*Difference in time from current date to housing sales price.

## Data Choice

Team Centennial Park chose house pricing in Tennessee because it is one of the most popular topics in Tennessee today. At one point or another everyone has thought about living in a home, currently lives in a home and wants to know what its worth, or wants to know what their future or current home will be worth. We at Team Centennial Park are here to solve some of your questions and help tell you where your dollar will go the farthest in Tennessee real estate investing. We are looking to help anyone in Tennessee looking for a house. 

## Outline of Project

###### 1. Determine the scope of the project

Selected Data:
- "city_county"
- "city_xhvi_1bedroom"
- "city_xhvi_2bedroom"
- "city_xhvi_3bedroom"
- "city_xhvi_4bedroom"
- "city_xhvi_5bedroomormore"
- "sale_prices_city"
- "TN_counties"
- Zillow housing price data from 1996-2021 which included number of bedrooms, city, housing prices by date, and county.

Determined topic of our Research
- Housing data is relevant to almost every adult in the United States. Most people at one point in their life are interested in purchasing a home or want to know what their current home is worth, or what their home will be worth in the future.

Selected the Questions We Wanted to Answer
- What will a home I purchase in Tennessee be worth in the future?

Identify data limitations
- Housing pricing is limited before 2009.
- Housing pricing is only from Zillow.
- Data only includes number of bedrooms, location, price, and number of days from current date.

###### 2. Review and Understand the Data
- Determine the datatypes for each column
- Filtered Data by State to Tennessee
- Dropped unneeded columns: 'Unnamed', 'RegionID', 'StateName', 'SizeRank'



## Machine Learning Model

## Database Integration

## Dashboard

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

## Challenges

Outlier Data in Forest Hills. A 1 bedroom home has the same price as a 5 bedroom home for a certain number of years.

Dataset only included Zillow housing prices which may have not been complete.

Model was determined on 5 variable. There are other variables that could effect housing prices including square footage, land size, and other common housing features.


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
		
                   
               
