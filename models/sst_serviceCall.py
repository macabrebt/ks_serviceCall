# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductType(models.Model):
    _name = 'sst.producttype'
    _description = 'Product Type'

    producttype = fields.Char('Product Type')
    _rec_name = 'producttype'

class sst_serviceCall(models.Model):
    _name = 'sst.serviceCall'
    _description = 'Service Call'

    productType = fields.Many2one('sst.producttype', string='Product Type', required=True)
    callDate = fields.Date('Call Date', required=True)
    contactMathod = fields.Selection(
        selection=[
            ('call', 'Call'),
            ('text', 'Text'),
            ('email', 'Email'),
            ('website', 'Website'),
            ('others', 'Others')
        ],
        string='Contact Method',
        default='email',
        required=True
    )

    shipment = fields.Char('Shipment details')

    callStatus = fields.Selection(
        selection=[
            ('done', 'Done'),
            ('pending', 'Pending'),
            ('canceled', 'HCanceled'),
            ('follow_up', 'Follow Up')
        ],
        string='Status',
        default='mediumDone',
        required=False
    )

    serviceTerm = fields.Selection(
        selection=[
            ('warrenty', 'Warrenty'),
            ('order', 'Order'),
            ('other', 'Other')
        ],
        string='Term',
        default='Warrenty',
        required=False
    )
    description = fields.Char('Service Details')

    owner = fields.Many2one('res.partner', string='Owner', required=True)

    notes = fields.Text('Internal Notes')
