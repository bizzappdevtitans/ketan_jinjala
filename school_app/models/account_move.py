# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'


    # Added field.
    delivery_details = fields.Text("Delivery Details")



    # inherited method
class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        """ This method for passing value of sale order to Down payment invoice """
        res = super()._prepare_invoice_values(order, name, amount, so_line)
        # update delivery detail in invoice
        res.update({'delivery_details':order.delivery_details})
        return res
