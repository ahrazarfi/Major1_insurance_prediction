REAL-TIME CASH FLOW PREDICTION FOR INSURANCE COMPANY

Our main objective is to build a web application to predict patient hospitalization charges for an insurance company that wants to increase its cashflow using patient health risk metrics such as age, smoking, BMI, region, etc.

The goal is to solve this challenge in such a way that the insurance company can predict the charges in real time. Using past metrics, the insurance company would be able to predict the patient hospitalization charges and build products and plans around them.

•	Our goal is not only to create a model using already available data that can predict it in developer-friendly environments but to make the model accessible to the end user who does not know how to code, thereby enabling the non tech-savvy employees of the insurance company to make predictions.

•	We will be using PyCaret. PyCaret is an open source, low-code machine learning library in Python which covers the complete pipeline from the raw dataset to the deployable machine learning model.

•	We will be building the back end of the web-app using the Flask framework.

•	To make this model accessible to the end user, i.e., the insurance company, our goal will be to make a web app that communicates with our model and outputs the prediction to the front-end of our web-app. 

•	Our complete machine learning pipeline will be deployed to production using GitHub and Heroku, a container- based cloud Platform as a Service (PaaS) so that it can be accessed using the internet. We will also be pointing the Heroku web-app address to a custom domain by adding a CNAME record in the domain provider’s DNS settings.

•	The end-user will feed new data points using the front-end of our web-app which will communicate with our model to generate predictions using the trained model.

