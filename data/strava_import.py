# from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# access dotenv
from dotenv import load_dotenv
load_dotenv("../.env")

#take STRAVA_ACCESS_TOKEN from .env
import os
STRAVA_ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")


# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = ''

# create an instance of the API class
api_instance = swagger_client.AthletesApi()

try: 
    # Get Authenticated Athlete
    api_response = api_instance.getLoggedInAthlete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->getLoggedInAthlete: %s\n" % e)