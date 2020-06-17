import tweepy as tw 
import time
import sys
from TwitterAPI import TwitterAPI
import json

import keys  


consumer_key= keys.Consumer_key
consumer_secret= keys.Consumer_secret
access_token= keys.Access_token
access_token_secret= keys.Access_token_secret
try:

    auth = tw.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    c = tw.Cursor(api.followers_ids, screen_name = 'Randomexperime2', count = 1)

    ids = []
    for page in c.pages():
        ids.append(page)
    print ("ids=", ids)
   

except tw.TweepError:

    print ("tweepy.TweepError=")#, tweepy.TweepError

print("ranking ids in assending order")    
ids.sort()
print(ids)    



apii = TwitterAPI(consumer_key, 
                 consumer_secret,
                 access_token,
                 access_token_secret)

for i in ids:

    user_id = ids[i]
    message_text = "Thank you for following me"

    event = {
        "event": {
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": user_id
                },
                "message_data": {
                    "text": message_text
                }
            }
        }
    }

    r = apii.request('direct_messages/events/new', json.dumps(event))
    print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)    



