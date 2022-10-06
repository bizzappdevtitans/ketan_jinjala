#-*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models

class StudentDetailWizard(models.TransientModel):
    _name = 'student.detail.wizard'
    _description  = "this is wizard "

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['student_detail_id'] = self.env['student.detail'].browse(self.env.context['active_ids'])
        return res



    checkout_ids = fields.Many2many("teacher.detail",string="Teacher",)
    student_detail_id =  fields.Many2one("student.detail",string="Student")
    address = fields.Char()
    age = fields.Integer(string="Age",required=True)
    gender = fields.Selection([('male','Male'),('female','Female')])



    def button_update(self):
        for rec in self:
            if rec.student_detail_id:
                #rec.student_detail_id.teacher_ids = [(6,0,rec.checkout_ids.ids or False)]
                rec.student_detail_id.address = rec.address
                rec.student_detail_id.age = rec.age
                rec.student_detail_id.gender = rec.gender
