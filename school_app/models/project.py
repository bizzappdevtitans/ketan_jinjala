# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.osv.expression import OR


class Project(models.Model):
    _inherit = 'project.project'


    add_project = fields.Text("Add Project")