# -*- coding: utf-8 -*-
{
    'name': "SST Service Call",

    'summary': """
        Customer service calls """,

    'description': """
        This module is created to manage customer's service calls
    """,

    'author': "Kai Song",
    'company': 'SST Inc.',
    'website': "https://www.sstuvled.com",

    'category': 'Services',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/sst_serviceCall.xml',
        'views/res_partner_views.xml',
    ],
    'license': 'MIT',
    'images': ['static/description/icon.png'],
    "installable": True,
    "application": True,
}
