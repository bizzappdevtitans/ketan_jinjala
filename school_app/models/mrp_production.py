# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class MrpWorkorder(models.Model):
    _inherit = 'mrp.production'


    # Added field.
    delivery_details = fields.Text("Delivery Details")


class StockRule(models.Model):
    _inherit = 'stock.rule'

    """ This method for passing value from sale order to manufacturing  """
    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
        res = super(StockRule ,self)._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
        sales_order = self.env['sale.order'].search([('name', '=', origin )])      
        if sales_order:
            res['delivery_details'] = sales_order.delivery_details
        return res
                    