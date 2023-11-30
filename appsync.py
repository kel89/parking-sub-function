import requests
import datetime as dt
import json
import os
import pytz

api_url = "https://delnlzxpzbebrlpigize73pqyq.appsync-api.us-east-1.amazonaws.com/graphql"

def get_subs():
    # Get Today's date in the correct Timezone
    utc_now = dt.datetime.utcnow()
    desired_timezone = pytz.timezone("America/Denver")
    desired_time = utc_now.replace(tzinfo=pytz.utc).astimezone(desired_timezone)
    desired_date = desired_time.date()
    today = desired_date.strftime("%Y-%m-%d")

    graphql_query = """
    query MyQuery {
        listToReserves(filter: {reserveOn: {eq: "%s"}}) {
            items {
                id
                reserveOn
                reserveTarget
                reserveTime
                resort
                user
            }
        }
    }
    """ % today

    # AWS AppSync requires a specific header for authorization
    headers = {
        "Content-Type": "application/json",
        "x-api-key": os.environ['appsync_api_key']  # should work with lambda env var, or could use secret manager...
    }

    response = requests.post(api_url, headers=headers, data=json.dumps({"query": graphql_query}))
    if response.status_code == 200:
        # Parse them out
        result = response.json()
        items = result['data']['listToReserves']['items']
        return items
    else:
        return []
        


