# -*- coding: utf-8 -*-
from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Added field.
    delivery_details = fields.Text("Delivery Details")
    add_project = fields.Text("Add Project")

    def _prepare_invoice(self):
        """ This method for passing value from sale order to regular invoice """
        res = super(SaleOrder,self)._prepare_invoice()
        # update delivery detail in invoice 
        res.update({'delivery_details':self.delivery_details}) 
        return res