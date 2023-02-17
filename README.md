# DNAC to Teams Webhook Notifcations
Cisco DNA Center has a compatibility issue sending webhook notifications to Microsoft Teams,  attempting to do a test will cause the test to error with a gemeroc "Failure" message which doesn't really help in the investigation.  After further debugging/packet capturing you'll see that MS Teams replies with an error 400 stating 'Summary or Text is required'

Microsoft Teams Webhooks use a particular JSON structure before it'll accept a webhook which can be found here: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL one that Cisco DNA Center doesn't know about and at time of writing doesn't have any plans to intergrate it into the platform.

This is a simple script that utilises python flask to receive a Cisco DNA Centre webhook, convert it into something Microsoft Teams will accept for it to appear in your webhook alerts channel.  Basically a middleware server/webhook proxy

Hope this helps fellow engineers out pulling their hair out, trying to get better visiblity from their DNA Center 
