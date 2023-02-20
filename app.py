# app.py
import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
#Microsoft Teams Webhook URL to the Alerts Channel
 teams_webhook = 'https://'

# Receiving the Webhook from DNAC grabbing the relevant information from the details section of the alert sent
 if request.method == 'POST':
  json_webhook = request.json

  #Grab Assurance name value to make it the Title of the notification
  alert_title = '<h1><b>' + json_webhook['details']['Assurance Issue Name'] + '</b></h1> '

# Parse on the details section of the payload of the alert put each key\value into pre_payload, add new lines so it looks pretty on the MS Teams channel
  pre_payload = "\\\n".join('<b>'+ key + ':</b> ' + value for key,value in json_webhook['details'].items())

# Create a payload with the JSON object "Title" and "Text": with the values of the alert_title and pre_payload as strings.
  payload = {"title": str(alert_title),"text":str(pre_payload) }

# Send the payload off to MS Teams webhook URL for it to display in your chosen channel
  response = requests.post(teams_webhook, json=payload)

# Print the payload for debugging purposes can comment out.
# print(payload)

  return "Webhook received!"

#Spin up the Flask instance using ssl adhoc (only use adhoc for testing, never use in a production environment) 
app.run(host='0.0.0.0', port=8000, ssl_context='adhoc')
