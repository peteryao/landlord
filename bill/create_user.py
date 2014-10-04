#!/usr/bin/python
# -*- coding: utf8 -*-

# Please install requests first if you don't have it: pip install requests
import requests
import hmac
import hashlib
import base64
import time
import re

# URL Endpoint to post the data
REQUEST_URL = "https://api.moxtra.com/oauth/token"

# Moxtra App Credentials from developer.moxtra.com
CLIENT_ID = "ulPImqICqYs"
CLIENT_SECRET = "mKB98J9rKRM"

# Function to setup/initialize user and get access token
def get_access_token(client_id, client_secret):

    # Unique ID of how user is identified in your system
    unique_id = "unique_user_id"

    # User Information
    firstname = "John"
    lastname = "Doe"

    # Create signature
    timestamp = str(int(time.time() * 1000))
    msg = client_id + unique_id + timestamp
    signature = base64.urlsafe_b64encode(hmac.new(key=client_secret, msg=msg, digestmod=hashlib.sha256).digest())
    # remove the tail "="
    signature = re.sub(r'=+$', '', signature)

    params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'http://www.moxtra.com/auth_uniqueid',
            'uniqueid': unique_id,
            'timestamp': timestamp,
            'signature': signature,
            'firstname': firstname,
            'lastname': lastname,
            }
    r = requests.post(REQUEST_URL, params = params)
    print r.status_code
    print r.text

if __name__ == '__main__':
    get_access_token(CLIENT_ID, CLIENT_SECRET) #Get Access Token to use with Moxtra SDKs and Rest APIs