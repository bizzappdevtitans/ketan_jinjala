# -*- coding: utf-8 -*-
from odoo import models,fields


class ClassDetail(models.Model):
    _name = "class.detail"
    _description = "class Detail"
    
    class_std = fields.Char(string = "Class Std", required=True)
    class_location = fields.Char(string="Class Location",required=True)
    class_size = fields.Char(string="Class Size", required=True,)
    student_ids =fields.One2many(comodel_name = "student.detail", inverse_name="name")
    partner_ids = fields.Many2many(comodel_name="teacher.detail",relation='Subject')
    


