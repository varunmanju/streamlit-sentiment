# Sentiment Analysis Twitter Dataset using Oracle Cloud.

# Pre-requisites or Technologies Used:

1> Python 3.11 for development.

2> Pandas to read the data from custom_pred.csv file and write it to an Oracle Autonomous Database

3> An Oracle Free Tire account to create an Oracle Autonomous Database with Automomous Transaction processing enabled

4> oracledb python package to connect to the Oracle Database.

5> Create a Python virtual environment and run pip install -r requirements.txt to install the packages.

# Setup Development Environment:

1> Make sure to create an Oracle autonomous database on the Oracle cloud with ATP(Autonomous transaction processing) option enabled. In addition to that set a password for the database and make sure to enable free tier.

2> Download the database wallet and ensure that you use this Wallet to connect to the database via Mutual TLS connection.

3> Create a .env file and create to set the following parameters:

    user (Username of the Database. By default it is admin)

    password (Password of your database you set during creation)

    dsn (Connection string in tnsnames.ora file)

    config_dir (Location of the tnsnames.ora file)

    wallet_location (Location where the wallet is downloaded)

    wallet_password (Password of the wallet directory downloaded when creating the Autonomous database)
    
4> Run the populate_test_data.ipynb file to populate the database. This is the test data which contains the model's prediction and actual label of the sentiment.

# Project Description:

1> I had created a custom Sentiment Classifier model and trained it on Oracle Cloud. Then I called the model endpoint via python and ran it on the test data. This test data is what I have written to the Oracle Database. The model was costing a lot when it was on cloud so I had to delete it. 

2> A Twitter Sentiment Analysis Clasifier was trained on Oracle Cloud that classifies text into Positive, Negative and Neutral Sentiments. 

3> Test data was provided for this classifier and the sentiment predicted by this classifieer, given a text as input was model_pred. actual_label was the assigned label to the text.

4> This project evaluates and displays the test data custom_pred.csv obtained by the classifier. Metrics such as precision, recall and F1 score obtained by the classifier are displayed. 

5> The test data is displayed by using streamlit a python package to render content in HTML.

# Validate Application:

1> Do streamlit run sentiment.py. Open the URL in the browser to view the test dataset analysis.










