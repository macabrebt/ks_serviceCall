# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductType(models.Model):
    _name = 'ks.service.call.product.type'
    _description = 'Product Type'
    _rec_name = 'product_type'

    product_type = fields.Char('Product Type')

class ks_serviceCall(models.Model):
    _name = 'ks.service.call'
    _description = 'Service Call'

    ks_product_type = fields.Many2one('ks.service.call.product.type', string='Product Type', required=True)
    call_date = fields.Date('Call Date', required=True)
    contact_method = fields.Selection(
        selection=[
            ('call', 'Call'),
            ('from_sales', 'From Sales'),
            ('message', 'Message'),
            ('email', 'Email'),
            ('website', 'Website'),
            ('others', 'Others')
        ],
        string='Contact Method',
        default='email',
        required=True
    )

    shipment = fields.Char('Shipment Details')

    call_status = fields.Selection(
        selection=[
            ('done', 'Done'),
            ('pending', 'Pending'),
            ('follow_up', 'Follow Up')
        ],
        string='Status',
        default='pending',
        required=False
    )

    service_term = fields.Selection(
        selection=[
            ('warranty', 'Warranty'),
            ('order', 'Order'),
            ('other', 'Other')
        ],
        string='Term',
        default='warranty',
        required=False
    )
    description = fields.Text('Service Details')

    owner = fields.Many2one('res.partner', string='Owner', required=True)

    notes = fields.Text('Internal Notes')
