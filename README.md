# temp Alert API

### Direction to Run

- Create a Venv
- Pip Install requierments.txt
- Add environment variables as defined in the settings.py file
- Run flask run command
##### !! I ran out of time after an hour to dockerize the app so ill be updating that later !!
##### !! This means you will need to add an environment variable to add a database connection !!
##### !! this is done using flask_sqlalchemy so it should be agnostic as to which databse is used but it was tested in postgres !!

###  For adding rules

- New rules are added using a POST method to the '/rules' endpoint
- The rule should be defined using Celsius
- the rule should be defined using a comma separated string Ex. 'temp, >, 37'
- the rule may also include the 'and' or  'or' keyword Ex. 'temp, > 31, or, temp, <, 20'  
- the keyword 'temp' will be a variable representing the temperature collected by the sensor


### For updating and deleting rules

- Updates and Deletes should be 'PUT' or 'DELETE' requests to the '/rules/<rule_id>'
- Put requests should be done using Celsius
- Put requests should carry a json payload with the new rule string under the 'rule' key

