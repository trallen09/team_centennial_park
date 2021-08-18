# Team Centennial Park Project: Zillow Pricing Predictor

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
- Data filtered by states.
- Identify number of null values by region and remove.

###### 3. Data Cleaning
- Cleaning was completed in Jupyter Notebook. All unnecessary and unneeded data stated above was removed through python coding.

## Machine Learning Model
- Import data utilizing sqlite3
- Convert data to dataframe using Pandas
- Using Jupyter Notebook, choose Machine Learning Model
	- We chose Linear Regression as our ML model because regression is used to predict continuous variables. Since we are trying to predict future or even past TN house prices, regression is needed.
	
- A function was created to take inputs from the webpage and run the predictions on the spot
- We have two features and one variable that can be changed by the user.
		- The two features are number of bedrooms and year
		- The variable that will modify the dataframe going into the model is the city in TN

#### Tableau Dashboard
* These dashboards provide options for the user of the final website to play around with the data.
* [Tableau Public Dashboard1](https://public.tableau.com/views/TNHousingForecastandMap/TN_House_Forecast?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
* [Tableau Public Dashboard2](https://public.tableau.com/views/TNCountyPrices/CountiesDash?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

### Week 1 for Machine Learning
* Created basic plan for machine learning processing of the data.
* Included different aspects that need to be considered during the process.
* Based on the dataset, different models and strategies will be tried.

## Challenges

Outlier Data in Forest Hills. A 1 bedroom home has the same price as a 5 bedroom home for a certain number of years.

Dataset only included Zillow housing prices which may have not been complete.

Model was determined on 5 variable. There are other variables that could effect housing prices including square footage, land size, and other common housing features.



		
                   
               
