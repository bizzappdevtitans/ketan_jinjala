# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError, ValidationError


class TeacherDetail(models.Model):
    _name = "teacher.detail"
    _description = "Teacher Detail"

    serial_number = fields.Char("Serial Number", default=lambda self: _('New') , copy=False)
    t_name = fields.Char(string="Name", required=True)
    subject = fields.Char(string="Subject",size=35)
    age = fields.Char(string="Age",required=True)
    dob = fields.Date(string="DOB", required=True, help="Date of Birth")
    active = fields.Boolean(string="Active", default=True)
    notes = fields.Text(string='notes')
    fields.Datetime.now()
    file = fields.Binary()
    signature = fields.Image('Signature', help='Signature received.', copy=False, attachment=True, max_width=1024, max_height=1024)
    principale_detail = fields.Many2one(comodel_name="principale.detail")
    teacher_mobile_No = fields.Char(string="Mobile Number",required=True)



    @api.constrains('teacher_mobile_No')
    def _constrains_mobile_No(self):
        if len(self.teacher_mobile_No) != 10:
            raise ValidationError('enter 10 digit number')
            
    @api.model
    def create(self,vals):
        print("__________vals__________________", vals)
        if vals.get('serial_number', _('New')) == _('New'):
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('teacher.detail') or _('New')
        res = super(TeacherDetail, self).create(vals)
        return res


