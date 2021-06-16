# temp Alert API


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

