# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "telegram"
app_title = "TelegramIntegration "
app_publisher = "OpenB Networks"
app_description = "Sends all doctype events to telegram"
app_icon = "octicon radio-tower"
app_color = "blue"
app_email = "hansel@openb.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/telegram/css/telegram.css"
# app_include_js = "/assets/telegram/js/telegram.js"

# include js, css files in header of web template
# web_include_css = "/assets/telegram/css/telegram.css"
# web_include_js = "/assets/telegram/js/telegram.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "telegram.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "telegram.install.before_install"
# after_install = "telegram.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "telegram.notifications.get_notification_config"

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
# doc_events = {
#     "Scheduler Log": {
#         "after_insert": "telegram.events.notify_telegram"
#     }
# }


doc_events = {
	"*": {
		"on_update": "telegram.events.notify_telegram",
		"on_cancel": "telegram.events.notify_telegram",
		"on_trash": "telegram.events.notify_telegram",
		"on_submit":"telegram.events.notify_telegram",
		"on_update_after_submit":"telegram.events.notify_telegram"
	}
}

# doc_events = {
# 	"*": {
# 		"on_update": "telegram.events.notify_telegram_update",
# 		"on_cancel": "telegram.events.notify_telegram_cancel",
# 		"on_trash": "telegram.events.notify_telegram_trash",
# 		"on_submit":"telegram.events.notify_telegram_submit",
# 		"on_update_after_submit":"telegram.events.notify_telegram_update_after_submit"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"telegram.tasks.all"
# 	],
# 	"daily": [
# 		"telegram.tasks.daily"
# 	],
# 	"hourly": [
# 		"telegram.tasks.hourly"
# 	],
# 	"weekly": [
# 		"telegram.tasks.weekly"
# 	]
# 	"monthly": [
# 		"telegram.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "telegram.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "telegram.event.get_events"
# }
