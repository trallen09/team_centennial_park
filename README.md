# Team JavaScript Crash Data

## Google Slide Presentation Link

### https://docs.google.com/presentation/d/1rCUgGdReLXpcnDJisHFbRMw03b5xDLH4zoAbk-zz0tE/edit?usp=sharing

## Link for the Dashboard Storyboard

### https://docs.google.com/presentation/d/1jLxOb1EkOrz2bPw1YZ-Z6WS_bTuhQcq5VOKu3fQD41U/edit?usp=sharing

#### Dataset Description
US data, for 1997-2002, from police-reported car crashes in which there is a harmful event (people or property), and from which at least one vehicle was towed. Data is restricted to front-seat occupants, include only a subset of the variables recorded, and is restricted in other ways.
#### Format
A data frame with 26217 observations on the following 15 variables:
##### dvcat
* Ordered factor with levels (estimated impact speeds) 1-9km/h, 10-24, 25-39, 40-54, 55+
##### weight
* Observation weights, albeit of uncertain accuracy, designed to account for varying sampling probabilities.
##### dead
* Factor with levels alive and dead
##### airbag
* Factor with levels none and airbag
##### seatbelt
* Factor with levels none and belted
##### frontal
* Numeric vector; 0=non-frontal, 1=frontal impact
##### sex
* Factor with levels f and m
##### ageOFocc
* Age of occupant in years
##### yearacc
* Year of accident
##### yearVeh
* Year of model of vehicle; a numeric vector
##### abcat
* Did one or more (driver or passenger) airbag(s) deploy? This factor has levels deploy nodeploy unavail
##### occRole
* Factor with levels driver pass
##### deploy
* Numeric vector: 0 if an airbag was unavailable or did not deploy; 1 if one or more bags deployed.
##### injSeverity
* Numeric vector: 0=none, 1=possible injury, 2=no incapacity, 3=incapacity, 4=killed; 5=unknown, 6=prior death
##### caseid
* Created by pasting together the populations sampling unit, the case number, and the vehicle number.<br> Within each year, use this to uniquely identify the vehicle.

## Data Choice

#### Team JavaScript chose data that was relevent to anyone. Crash data is relevant to any driver, any parent with children who have earned their driver license, and anyone who uses public roadways. This data included factors we had a general interest in to include age and sex of injured individual, airbag deployment, seatbelt usage, and year of vehicle. This data allows us to learn more about crash safety. We are also looking forward to making connections to injury severity and vehicle specifications and driver/passenger attributes.

## Outline of Project

### 1. Determine the scope of the project

        a. Selected data
                i. "Airbag and other influences on accident fatalities"
                ii. Description: US data, for 1997-2002, from police-reported car crashes in which 
                there is a harmful event (people or property), and from which at least one vehicle 
                was towed. Taken from nassCDS with 26,217 observations before data cleanup.

        b. Determined topic of our research
                i. Crash data is relevant to any driver, any parent with
                   children who have earned their driver license, and
                   anyone who uses public roadways. We are also looking
                   forward to making connections to injury severity and
                   vehicle specifications and driver/passenger attributes.

        c. Selected the questions we wanted to answer
                i.  What is the likelihood of fatality in a car
                    accident given a variety of vehicle and passenger
                    factors?

        d. Identify data limitations
                i. There are coonsiderably less data for >40km/h
                   than <40km/h
                ii. Only driver and frontseat passengers are reflected in
                    the data, backseat passenger data was not collected.
                iii. Speed at impact is estimated
                iv. Data is for accidents occuring between 1997-2002
                v. Data is specific to accidents where a vehicle was towed

### 2. Review and understand the data

        a. Identify missing data

        b. Identify data that is not helpful for the project
                i. Columns removed include:
                   - 'weight': Value of unknown significance or origin
                   - 'yearacc': Year the accident occurred from 1997-2002
                      and is not relevant to the analysis
                   - 'caseid': Not unique identifiers,
                      numerous indicents assigned to single id's
                   - 'airbag' & 'deploy': Values are duplicated in the
                     'abcat' column
                   - 'injury_severity': Values are not relevant to alive/dead outcome being saught

        c. Map the plan for cleaning data
                i. Remove null values
                ii. rename column names for user
                    clarity
                iii. renamed classification values for seatbelt
                     column for clarity
                iv. renamed classification values for frontal impact
                    to (1) and non-frontal impact to (0)

### 3. Data Cleaning

        a. Import data utilizing Pandas

        b. Using Jupyter Notebook, eliminate missing and un-needed data

        c. Transform the data as needed to binary values or binning
                i. Binning utilized for speed
                ii. Binary values used for "frontal" column for impact
                    location

### 4. Feature Engineering and Selection

        a. Feature engineering- there is no need for feature engineering with
           this data set

        b. Feature selection- 'est_impact_kmh',
                        'ultimate_outcome',
                        'airbag_available',
                        'front_impact',
                        'occupant_age',
                        'vehicle_year',
                        'airbag_deployment',
                        'occupant_role'
                These features were chosen for the relevance of answering
                our research question: "What factors are most relevant in
                prediciting survival rates in a car accident?"

        c. Make predictions on how feature engineering and selection may
           affect data later in the project.
                i. We believe removing "airbag" and "deploy" columns will
                   allow our data to increase in accuracy.   Whether an
                   airbag was installed and whether the airbag deployed
                   was already represented in the "airbag_deployment"
                   column.  Removing this redundancy allowed for more
                   concise learning for the model.
                ii. Removing the columns indicating weight, year of
                    accident and the case id will have no affect on our
                    data outcomes.  Weight is a previously indiciated
                    importance level from the original data collector and
                    has no place in our analysis.  The year of the
                    accident did not seem important because

### 5. Database Creation

        a. Import data utilizing SQLite
                i. Create 2 tables: "Occupants" & "Accidents"

        b. Joined databases using Natural Join

### 6. Machine Learning

        a. Import data utilizing Pandas

        b. Using Jupyter Notebook, choose Machine Learning Model
                i. We chose Random Oversampling as our ML model because we
                   have far less rows of "alive" than "dead" in the "ultimate_outcome" column.
                   Random oversampling manipulates the minority class
                   "dead" to allow for a resampled test and training
                   process.
                ii. Limitations of Random Over Sampling include a
                    low precision score for the minority class (dead).
                    The low precision score may indicate an inflated
                    accuracy score.

### 7. Dashboard Creation

        a. Use HTML template and css to create the dashboard
                i. html will include jumbotron, project title, music, drop down selections
                   for predictions, reset button, a gif and our data limitation.  
                ii. Google Slides may be added 
                iii. css will include neon colors, consistent courier font, borders around
                     images and boxes 

        b. Use Python and Flask to develop interactive elements
                i.  import joblib, numpy, flask, pandas and pickle to run app.py
                ii. use joblib to import model data to populate the machine learning
                    interactive elements of the dashboard.
                iii. Ultimate outcome prediction:
                        a. You did not survive.
                        b. YOU SURVIVED!
