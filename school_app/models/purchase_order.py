# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # Added field.
    purchase_detail = fields.Text("Purchase Detail")


    ''' this method to pass value from purchase order to purchase view form'''
    def _prepare_picking(self):
        if not self.group_id:
            self.group_id = self.group_id.create({
                'name': self.name,
                'partner_id': self.partner_id.id
            })
        if not self.partner_id.property_stock_supplier.id:
            raise UserError(_("You must set a Vendor Location for this partner %s", self.partner_id.name))
        return {
            'picking_type_id': self.picking_type_id.id,
            'partner_id': self.partner_id.id,
            'user_id': False,
            'date': self.date_order,
            'origin': self.name,
            'purchase_detail':self.purchase_detail,
            'location_dest_id': self._get_destination_location(),
            'location_id': self.partner_id.property_stock_supplier.id,
            'company_id': self.company_id.id,
            }
        
    def _get_new_picking_values(self):
        ''' this method to pass value from sale order to delivery'''
        vals = super(PurchaseOrder, self)._get_new_picking_values()
        purchase_detail = self.group_id.sale_id.purchase_detail
        vals['purchase_detail'] = purchase_detail   
        return vals


