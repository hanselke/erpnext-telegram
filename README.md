## Slack Integration 

Frappe and ERPNext Slack Notification Integration

## How to Install

In Slack Menu
1. Go to Apps & Integration Menu
2. Search and Select "Incoming WebHooks" App
3. Click Add Configuration
4. Select or Create a channel where you want to be notified
5. Click Add Incoming Webhooks Integration
6. Take note the Webhook URL value
    * It should look like this: https://hooks.slack.com/services/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


In Frappe/ERPNext Menu
1. Go to Setup -> Slack Settings
2. Set the the values.
    Mandatory Fields:
      * Webhook URL  = copy the value that you get in Slack Incomming Webhooks Integration ( Step 6 in Slack Menu Section )
      * Channel = copy the value the one you select or create in ( Step 4 in Slack Menu Section )

#### License

MIT