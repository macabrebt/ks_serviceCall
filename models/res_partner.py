# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"


    service_call_ids = fields.One2many('ks.service.call', 'owner', string=' ')

    service_calls_count = fields.Integer(string='Number of service calls', compute='_compute_count_service_calls')

    @api.depends('service_call_ids')
    def _compute_count_servicel_calls(self):
        for r in self:
            r.service_calls_count = len(r.service_call_ids)