# -*- coding: utf-8 -*-
from odoo import fields, models


class MailActivity(models.Model):
   _name = 'mail.activity'


   def action_done(self):
       print("function")