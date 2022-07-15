# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
Goals.- build a solid model in order to determine if a loan will be given base on different data. Model will be build using Feature Engineering and EDA in order to determine the best approach and then create that model using Pipeline.Deploy the model using Flask locally and to the AWS Cloud.

## Hypothesis
Applicants that will have a loan accepted:
  . Most likely those with a credit history.
  . Those with a high amount income. 
  . Those that are educated, married, high amount income of both applicants.
  . Those who have an average income and live in a urban area.
In order to test this hypothesis , getting a relationship of each feature versus loan status using group by or a ghraphic. Also pivot table.

## EDA 
Applicant Income falls in the range from 10k to 20k and some outliers with 50K,60K
There is a relationship between Credit History and people who are married, educated and lives in a semiurban and urban area, which points Credit History will play a big role in deciding the Loan Status
Most of the applicants are males 489 versus female 112, which points a bias on the dataset
Most people are not self employed and educated, pointint this two factors might play a big role in making decisions.
Property Area classes are divided in equal distributions.
People with education have more income and those without.

## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
EDA : plot  different graphs comparing features, using group by function and getting unique values,pivot table in order to understand the distribution of data.
Cleaning and Feature Engineering: categorical features with empty values were fill using the most frequent value, numerical feature were fill using the median,also
the categorical features were replace using cat encoding ( one hot encoding not use in this case since it will add more features), features like LOAN ID were drop from the dataframe.
Modeling : in this case I decide to use Random Forest Classifier with Grid Search , this model is a better fit to Data with several features and handling categorical , numerical values without scaling. Also I did my pipeline base on my observations with the Feature Engineering and the Random Forest Classifier results
Deployment: I deploy locally my model using and app.py function with JSON Requests. For my AWS cloud deployment , since I had Windows has my operative system I had to transfer my data using WINSCP.
Testing : Multiple testing change values on my JSON dictionary for the requests.

## Results/Demo
RFC Accurary Score on train data of : .7945
Pipeline Accurary Score on train data of : .8054
For my API , I use the Class Prediction and POST instructions in order to able to interact with the the model just modifying the JSON dictionary values.
## Challanges 
Main challenge was to create the API working locally and the connection to the cloud, for some reason I was getting permission denied on my Ubuntu instance, even if I have the connection set up, I decided to use WINSCP to trasnfer my files locally to the remote cloud.

## Future Goals
I would probably try more models not only Random Forest Classifier, and I will try to deploy my model to POSTMAN or using GITBASH
