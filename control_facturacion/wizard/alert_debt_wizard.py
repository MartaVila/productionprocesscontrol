# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AlertDebtWizard(models.TransientModel):
    _name = 'alert.debt.wizard'

    alerta_proyecto_vacio = fields.Char(
        string='Falta rellenar el proyecto',
        required=False)

    @api.model
    def default_get(self, default_fields):
        result = super(AlertDebtWizard, self).default_get(default_fields)
        if self._context.get('invoices_with_debt') != "":
            result['alerta_proyecto_vacio'] = "No puedes facturar. Las siguientes lineas son servicios y no tienen proyecto indicado: " + self._context.get(
                'lines_sale_order_without_project')
        return result
