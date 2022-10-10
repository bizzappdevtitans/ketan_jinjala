# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from datetime import date, timedelta
from odoo.exceptions import AccessError, UserError, ValidationError



class StudentDetail(models.Model):
    _name = "student.detail"
    _description = "Student Detail"
    
    
    serial_number = fields.Char("Serial Number", default=lambda self: _('New'),copy=False)
    name = fields.Char(string = "Name", required=True)
    age = fields.Integer(string="Age",required=True)
    address = fields.Char(string="Address",required=True)
    weight = fields.Float(string="Weight",required=True)
    dob = fields.Date(string="DOB", required=True, help="Date of Birth")
    gender = fields.Selection([('male','Male'),('female','Female')])
    image = fields.Image()
    term_end_date = fields.Datetime()
    priority = fields.Selection([('0', 'Normal'),('1', 'Good'),('2', 'Very Good'),('3', 'Excellent')])
    principal_id = fields.Many2one(comodel_name="principale.detail") 
    teacher_ids = fields.One2many(comodel_name = "teacher.detail", inverse_name="t_name")
    total = fields.Float(compute="mark_total")
    maths_mark = fields.Integer()
    physics_mark = fields.Integer()
    chemistry_mark = fields.Integer()
    total_female_count = fields.Integer("Female Count")
    total_male_count = fields.Integer("Male Count")
    state = fields.Selection(selection=[ ('draft', 'Draft'), ('in_progress', 'In Progress'),], string='Status', required=True, readonly=True, copy=False, default='draft')




    def button_in_progress(self):
        self.write({
           'state': "in_progress"
        })


    @api.model
    def create(self,vals):
        print("__________vals__________________", vals)
        if vals.get('serial_number', _('New')) == _('New'):
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('student.detail') or _('New')
        res = super(StudentDetail, self).create(vals)
        if res.gender == 'male':
            res.name = 'Mr. ' + res.name
        else:
            res.name = 'Mrs. ' + res.name
        return res


    @api.onchange("dob")
    def onchange_dob(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1

    @api.depends("age")
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.dob = today - relativedelta.relativedelta(years=rec.age)


    # @api.onchange("dob")
    # def onchange_dob(self):
    #     for record in self:
    #         if record.dob:
    #             today = date.today()
    #             record.age = today.year - record.dob.year - ((today.month, today.day) < (record.dob.month, record.dob.day))
    #             female_student = self.env["student.detail"].search([('gender', '=', 'female')])
    #             print("________________search female student____________________", female_student)

   
    @api.depends("total")
    def mark_total(self):
        for record in self:
            record.total = record.maths_mark + record.physics_mark + record.chemistry_mark


    @api.onchange("student_detail")
    def onchange_student(self):
        for record in self:
            if record.total_male_count:
                record = self.env['student_detail'].browse(name_record)


    def unlink(self):
        res = super(StudentDetail, self).unlink()
        self.env["res.users"].unlink()
        return res  


    # @api.model_create_multi
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = record.name 
    #         result.append((record.id,name))
    #     return result 


    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if record in self:
            return self._search(_name)
            # print("______________name_search______________________", _name)
        return super(StudentDetail, self)._name_search(_name, record=record)



    def get_portal_last_student(self):
        self.ensure_one()
        return self.total._get_last()



    @api.onchange('gender')        
    def onchange_gender(self):
        for rec in self:
            if rec.gender == 'male':  
                rec.total_male_count = self.search_count([('gender','=','male')])
            if rec.gender == 'female':        
                rec.total_female_count = self.search_count([('gender','=','female')])


    def name_get(self):
        res = []
        for rec in self:
            #name = "%s - %s" % (rec.name, str(rec.age))
            name= rec.name + ' - ' + str(rec.age)
            res += [(rec.id, name)]
        return res

    def open_update_wizard(self):
       return {
        'name': _('Update Wizard'),
        'type': 'ir.actions.act_window',
        'res_model': 'student.detail.wizard',
        'view_mode': 'form',
        'target': 'new'
           }


    def student_parameter_detail(self):
        for rec in self:
            if rec.allowed_student_detail:
                #rec.student_detail_id.teacher_ids = [(6,0,rec.checkout_ids.ids or False)]
                rec.allowed_student_detail.name = rec.name
        
             

