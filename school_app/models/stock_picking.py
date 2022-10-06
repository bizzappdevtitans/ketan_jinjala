# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields,api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    delivery_details = fields.Text("Delivery Details")
    purchase_detail = fields.Text("Purchase Detail")

