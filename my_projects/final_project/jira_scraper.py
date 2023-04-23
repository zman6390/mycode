#Import your libraries
import json 
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

#URL in order to search for all issues
url = "https://find-jira-errors.atlassian.net/rest/api/2/search"

#Create an object for authentication using the register email and the token from jira

auth = HTTPBasicAuth("zackery.davis6390@gmail.com","ATATT3xFfGF0DB7V0dhjowSj-B7OMdoBCM3u1pVIzxdwh9HhcY7TYFHs_yFH0rFWCTduHICsJdrvh8k8TDIEcB1mokE-0MP6497VHQEGmWu9L-kiTWeyP_hSWp5mHiPt4UKPuGDZuXukUa7j2tkhLIX7Z4aD9ro8Dlj9K7CQF3IaPab5EOJgWn0=9C67E2E5")

#Create a header parameter to mention the desired format for our data

headers = {
        "Accept": "application/json"
        }
#We need a parameter to find the name of our project
query = {
        "name": "final project"
        }

#Now we need to create a request with the above parameters
response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth,
        params=query
        )

#Now we will use the json loads method to read the json data and return key:value pairs

all_issues = json.dumps(json.loads(response.text),
        sort_keys=True,
        indent=2,
        separators=(",",": "))

#After that we will still have a JSON response and we can convert it into a pythonic dictionary using loads() method
dict_all_issues = json.loads(all_issues)

#We can create a variable which we will use to append issues into a list

list_all_issues = []

#For our output we are interested in the key, the summary, and reporter name off of jira
key_issue, key_summary, key_reporter = "","",""

#Function to iterate through the json data to pull the outputs we want
def iterate_issues(issues, inner):
    
    # the details for each issue might be directly accessible or inside another nested dictionary
    for key, values in issues.items():
        #If the key is 'fields' this will get its value which fetches the summary of the issue
        if(key == 'fields'):
            #The type of object is a json string so we convert it to a dict
            fields_dict = dict(values)

            #The summary field we want is located inside another nest dict so we can recursively call our function
            iterate_issues(fields_dict, inner)

        #We want to fetch the reporter name for an issue so if the key is 'reporter' get the value
        elif (key == "reporter"):
            #since the type is json we convert to dict
            dict_reporter = dict(values)

            #recursive call again to look for our value
            iterate_issues(dict_reporter, inner)

        #The key id for issue 'key' is easily accessible so we get that value and append it to a temp list
        elif(key == 'key'):
            key_issue = values
            inner.append(key_issue)

        #Get the value of 'summary' key and append it to a temp list
        elif(key == 'summary'):
            key_summary = values
            inner.append(key_summary)

        #Get the value of 'displayName' key and append it to a temp list 
        elif(key == 'displayName'):
            key_reporter = values
            inner.append(key_reporter)

#Iterate through the API data output and look for 'issues' key
for key, value in dict_all_issues.items():
    #THe issues that get fetched are present as a list when run against the key "issues"
    if(key == "issues"):
        #Get total number of issues
        total_issues = len(value)

        #Iterate through each item and grab the key,summary,and reporter name
        for each_issue in range(total_issues):
            inner = []
            #the data is a nest dict so we can iterate through
            iterate_issues(value[each_issue],inner)

            #Add the temp list data to our final list
            list_all_issues.append(inner)

#Create a framed object that holds the final list data
frame_issues = pd.DataFrame(list_all_issues, columns = ["Reporter", "Summary", "Key"])

#Reformat the data to get the sequence we want which is key,summary,reporter

column_values = ["Key", "Summary", "Reporter"]
frame_issues = frame_issues.reindex(columns=column_values)
print(frame_issues)

