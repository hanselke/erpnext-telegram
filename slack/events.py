import json
import frappe
from urlparse import urlparse


def notify_slack(doc, method):
    if frappe.db.get_value("Slack Settings", None, "icon"):
        icon = frappe.db.get_value("Slack Settings", None, "icon")
    else:
        icon = ':ghost:'
    send_slack(doc.error, frappe.db.get_value("Slack Settings", None, "bot_name"), frappe.db.get_value("Slack Settings", None, "channel"), icon)


def send_slack(message, username, channel, icon):
    import httplib
    parsed_uri = urlparse(frappe.db.get_value("Slack Settings", None, "webhook"))
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    path = '{uri.path}'.format(uri=parsed_uri)

    data = json.dumps({"channel": channel, "username": username, "text": message, "icon_emoji": icon})
    h = httplib.HTTPSConnection(domain)
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    h.request('POST', path, data, headers)
    r = h.getresponse()

