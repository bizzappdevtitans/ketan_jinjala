# -*- coding: utf-8 -*-
from odoo import models,fields


class SchoolLibraryDetail(models.Model):
    _name = "school.library.detail"
    _description = "School Library Detail"
    
    # Added field.
    librarian_name = fields.Char(string = "Librarian Name", required=True)
    librarian_age = fields.Integer(string="Age",required=True)
    librarian_address = fields.Char(string="Address",required=True)
    librarian_weight = fields.Float(string="Weight",required=True)
    librarian_dob = fields.Date(string="DOB", required=True, help="Date of Birth")
  