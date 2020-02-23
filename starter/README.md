# Article CMS (FlaskWebProject)
This project is a Python web application built using Flask. The user can log in and out and create/edit articles. An article consists of a title, author, and body of text stored in an Azure SQL Server along with an image that is stored in Azure Blob Storage.

## How to Run FlaskWebProject Locally:
1. Create a SQL Database on Azure.
2. Run the "users-table-init.sql" script from the "SQL Scripts" folder on the Azure SQL Database.
3. Run the "posts-table-init.sql" from the "SQL Scripts" folder on the Azure SQL Database.
4. Create an Azure Blob Storage account with a container called "images" where all uploaded images will be stored.
5. Open FlaskWebProject.sln using Visual Studio 2019 Community Edition.
6. Open config.py and provide all of the correct values for each of the environment variables to match what is set in Azure.
7. Run the FlaskWebProject locally and verify a login screen is displayed. If an error is displayed, it is likely that either a SQL environment variable or the Azure SQL Database is misconfigured.

## How to Run FlaskWebProject in Azure
1. Complete Steps 1-4 above if not done already.
5. Create an Azure Pipeline for a Python App Service. This will take care of deploying the App Service to Azure.
6. Go to the app service in the Azure Portal, select Configuration, and provide all of the correct values for each of the environment variables to match what is set in Azure.

## Log In Credentials for FlaskWebProject
Username: admin

Password: pass

### Dependencies

1. A free Azure account
2. A GitHub account
3. Python 3.7 or later
4. Visual Studio 2019 Community Edition (Free)
5. The latest Azure CLI

All Python dependencies are stored in the requirements.txt file. To install them, using Visual Studio 2019 Community Edition:
1. In the Solution Explorer, expand "Python Environments"
2. Right click on "Python 3.7 (64-bit) (global default)" and select "Install from requirements.txt"

## Project Instructions

You are expected to do the following to complete this project:
1. Create a Resource Group in Azure.
2. Create an SQL Database in Azure that contains a user table, an article table, and data in each table (populated with the scripts provided in the SQL Scripts folder).
3. Create a Blob Storage Container in Azure for images to be stored.
4. Create an Azure Pipeline to deploy the FlaskWebProject. After creating the Azure Pipeline, you will be provided with a file called "azure-pipelines.yml". Please provide this file when submitting your project solution.
6. Deploy the FlaskWebProject to Azure as an App Service.
7. To prove that the application in on Azure and working, go to the URL of the App Service, log in using the credentials in this README, click the Create button, and create an article with the following data:
	1. Title: "Hello World!"
	2. Author: "Jane Doe"
	3. Body: "My name is Jane Doe and this is my first article!"
	4. Upload an image of your choice. Must be either a .png or .jpg.
   After saving, click back on the article you created and provide a screenshot proving that it was created successfully. Please also make sure the URL is present in the screenshot.
8. Log into the Azure Portal, go to your Resource Group, and provide a screenshot including all of the resources that were created to complete this project. (see sample screenshot in "Sample Solution Screenshot" folder)