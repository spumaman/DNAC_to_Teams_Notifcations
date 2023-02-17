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

# Parse the details section of the alert payload sent by DNAC, put each key\value of that section into pre_payload, add new lines so it looks pretty on the MS Teams channel
  pre_payload = "\\\n ".join(key +': ' + value.capitalize() for key,value in json_webhook['details'].items())
 
# Create a payload with the JSON object "Text": and the value of the pre_payload as a string.
  payload = {"text": str(pre_payload)}
 
# Send the payload off to MS Teams webhook URL for it to display in your chosen channel
  response = requests.post(teams_webhook, json=payload)
 
# Print the payload for debugging purposes can comment out.
  print(payload)
  return "Webhook received!"
 
#Spin up the Flask instance using ssl adhoc (only use adhoc for testing, never use in a production environment)
app.run(host='0.0.0.0', port=8000, ssl_context='adhoc')
