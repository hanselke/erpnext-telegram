from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Integrations"),
            "icon": "octicon octicon-cloud-upload",
            "items": [
                {
                    "type": "doctype",
                    "name": "Slack Settings",
                    "label": _("Slack Settings"),
                    "description": _("Slack notification     for Frappe and ERPNext"),
                    "hide_count": True
                }
            ]
        }
    ]
