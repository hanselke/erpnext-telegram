import json
import frappe
import urllib
import urllib2


def notify_telegram(doc, method):
    config = frappe.get_site_config()
    if config["developer_mode"] != 1:
        send_telegram(doc.title, frappe.db.get_value("Telegram Settings", None, "chat_id"),
                   frappe.db.get_value("Telegram Settings", None, "api_key"))



# Generate a bot ID here: https://core.telegram.org/bots#botfather


# Send a message to a chat room (chat room ID retrieved from getUpdates)


def send_telegram(message,chat_id,api_key):
    ## code from https://stackoverflow.com/questions/24330922/sending-messages-with-telegram-apis-or-cli
    import urllib2
    urllib2.urlopen("https://api.telegram.org/bot" + api_key + "/sendMessage", urllib.urlencode({ "chat_id": chat_id, "text": message })).read()

# def send_telegram(message, username, channel, icon):
#     import httplib
#     parsed_uri = urlparse("https://api.telegram.org/bot" + 
#     domain = '{uri.netloc}'.format(uri=parsed_uri)
#     path = '{uri.path}'.format(uri=parsed_uri)

#     data = json.dumps({"channel": channel, "username": username, "text": message, "icon_emoji": icon})
#     h = httplib.HTTPSConnection(domain)
#     headers = {"Content-type": "application/json", "Accept": "application/json"}
#     h.request('POST', path, data, headers)
#     r = h.getresponse()
