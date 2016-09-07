# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "slack"
app_title = "Slack Integration "
app_publisher = "Bai Web and Mobile Labs"
app_description = "Frappe and ERPNext Notification Integration"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ccfiel@bai.ph"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/slack/css/slack.css"
# app_include_js = "/assets/slack/js/slack.js"

# include js, css files in header of web template
# web_include_css = "/assets/slack/css/slack.css"
# web_include_js = "/assets/slack/js/slack.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "slack.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "slack.install.before_install"
# after_install = "slack.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "slack.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
    "Scheduler Log": {
        "after_insert": "slack.events.notify_slack"
    }
}


# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"slack.tasks.all"
# 	],
# 	"daily": [
# 		"slack.tasks.daily"
# 	],
# 	"hourly": [
# 		"slack.tasks.hourly"
# 	],
# 	"weekly": [
# 		"slack.tasks.weekly"
# 	]
# 	"monthly": [
# 		"slack.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "slack.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "slack.event.get_events"
# }
