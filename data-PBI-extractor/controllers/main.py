from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
import json
import random
import requests

class PBIExport(CustomerPortal):
    @http.route(['/PBI/analytic/tickets'], type='http', auth="public", website=True)
    def get_tickets_analytic(self, access_token=None, report_type=None, download=False, **kw):
        url = 'https://processcontrol.odoo.com'
        db = 'marcosescano-productionprocesscontrol-master-977617'
        username = 'hector.cerezo@processcontrol.es'
        password = '2332AJahn2332$'

        json_endpoint = "%s/jsonrpc" % url
        headers = {"Content-Type": "application/json"}


        def get_json_payload(service, method, *args):
            return json.dumps({
                "jsonrpc": "2.0",
                "method": 'call',
                "params": {
                    "service": service,
                    "method": method,
                    "args": args
                },
                "id": random.randint(0, 100000000),
            })


        payload = get_json_payload("common", "login", db, username, password)
        response = requests.post(json_endpoint, data=payload, headers=headers)
        user_id = response.json()['result']

        print("user_id: ", user_id)

        if user_id:
            search_domain = [['name', 'ilike', 'hector']]
            payload2 = get_json_payload("object", "execute_kw", db, user_id, password, 'res.partner', 'search', [search_domain], {'limit': 5})
            res = requests.post(json_endpoint, data=payload2, headers=headers).json()

            payload3 = get_json_payload("object", "execute_kw", db, user_id, password, 'res.partner', 'read', [res['result']])
            resultado = requests.post(json_endpoint, data=payload3, headers=headers).json()

            print("Resultado", resultado)

        else:
            print("Failed credentials")
