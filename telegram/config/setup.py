from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Integrations"),
            "icon": "octicon octicon-radio-tower",
            "items": [
                {
                    "type": "doctype",
                    "name": "Telegram Settings",
                    "label": _("Telegram Settings"),
                    "description": _("Telegram notification     for Frappe and ERPNext"),
                    "hide_count": True
                }
            ]
        }
    ]
