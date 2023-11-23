import requests
import datetime as dt
import json
import os

api_url = "https://delnlzxpzbebrlpigize73pqyq.appsync-api.us-east-1.amazonaws.com/graphql"

def get_subs():

    today = dt.datetime.today().strftime("%Y-%m-%d")
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
        "x-api-key": os.environ['appsync_api_key']  # Replace with your API key or other authentication headers
    }

    response = requests.post(api_url, headers=headers, data=json.dumps({"query": graphql_query}))

    if response.status_code == 200:
        # Parse them out
        result = response.json()
        items = result['data']['listToReserves']['items']
        return items
    else:
        return []
        


