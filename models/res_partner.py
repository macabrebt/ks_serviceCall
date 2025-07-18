# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"


    serviceCall_ids = fields.One2many('sst.serviceCall', 'owner', string='Service Call')

    serviceCalls_count = fields.Integer(string='Number of service calls', compute='_compute_count_servicecalls')

    @api.depends('serviceCall_ids')
    def _compute_count_servicelCalls(self):
        for r in self:
            r.serviceCalls_count = len(r.serviceCall_ids)