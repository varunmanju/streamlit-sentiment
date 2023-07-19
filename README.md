# Sentiment Analysis Twitter Dataset using Oracle Cloud.

Prerequisites:\

An Oracle Cloud Free tier account.

Steps:
1> Make sure to create an Oracle autonomous database on the Oracle cloud with ATP(Autonomous transaction processing) option enabled. In addition to that set a password for the database and make sure to enable free tier.

2> Download the database wallet and ensure that you use this Wallet to connect to the database via Mutual TLS connection.

3> Once this is done then make sure you set the connection parameters in the connection variable in the sentiment.py file.

4> Run the populate_test.ipynb file to populate the database.This is the test data which contains the model's prediction and actual label of the sentiment

5> Rhen do streamlit run sentiment.py. Open the url in the browser to view the test dataset analysis.




