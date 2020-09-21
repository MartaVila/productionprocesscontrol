# -*- coding: utf-8 -*-
{
    'name': "Control Facturación",

    'summary': """""",

    'description': """
        Este módulo controla si un producto es de categoria de servicio y no permite la facturación de una linea del mismo sin rellenar completamente
    """,

    'author': "ProcessControl",
    'website': "https://www.processcontrol.es",
    'category': 'Revenues',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','account'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'wizard/alert_debt_wizard.xml',
        'views/views.xml',
    ]
    # only loaded in demonstration mode
    #'demo': [
        #'demo/demo.xml',
    #],
}