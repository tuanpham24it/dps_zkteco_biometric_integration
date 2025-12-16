# -*- coding: utf-8 -*-
from odoo import fields, models

class EmployeeLeaveLine(models.Model):
    _name = 'employee.leave.line'
    _description = 'Employee Leave Line'
    _order = 'date desc, id desc'

    employee_id = fields.Many2one('hr.employee', required=True, ondelete='cascade', index=True)
    date = fields.Date(required=True, index=True)

    leave_type = fields.Selection([
        ('none', 'None'),
        ('holiday', 'Holiday'),
        ('medical', 'Medical Leave'),
        ('vacation', 'Vacation'),
    ], string="Leave Type", default='none', required=True)

    description = fields.Char()
    paid_medical_leave = fields.Boolean(string='Paid')

    att_start_date = fields.Datetime(string="Start")
    att_end_date = fields.Datetime(string="End")
