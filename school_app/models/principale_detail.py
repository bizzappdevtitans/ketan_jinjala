# -*- coding: utf-8 -*-
from odoo import models,fields


class PrincipaleDetail(models.Model):
    _name = "principale.detail"
    _description = "Principale Detail"
    
    name = fields.Char(string = "Name", required=True)
    age = fields.Integer(string="Age",required=True)
    dob = fields.Date(string="DOB", required=True, help="Date of Birth")
    teacher_details = fields.One2many(comodel_name = "teacher.detail", inverse_name="t_name")
    student_details = fields.Many2many(comodel_name="student.detail",relation='age')


    #Name Get example

    def name_get(self):
        res = []
        for rec in self:
            name= rec.name + ' - ' + str(rec.age)
            res += [(rec.id, name)]
        return res
        