# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    school_information = fields.Char(string = "School Information ", config_parameter="school_app.add_school_information")
    


