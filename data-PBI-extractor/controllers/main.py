from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
import json
import random
import requests

class PBIExport(CustomerPortal):
    @http.route(['/PBI/analytic/tickets'], type='http', auth="public", website=False)
    def get_tickets_analytic(self, access_token=None, report_type=None, download=False, **kw):
        print 'CONNECTION SUCCESSFUL ***'
        print 'args *** ' , args
        
        name = args.get('name', False)
        email = args.get('email', False)
        
        if not name:
            Response.status = '400 Bad Request'
        return '{"response": "OK"}'
