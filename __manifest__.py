# -*- coding: utf-8 -*-
{
    'name': "Service Call",

    'summary': """
        Customer service calls app for Odoo""",

    'description': """
        This module is created to manage customer's service calls
    """,

    'author': "Kai Song",
    'website': "https://www.sstuvled.com",

    'category': 'Services',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ks_service_call.xml',
        'views/res_partner_views.xml',
    ],
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
    "installable": True,
    "application": True,
}
