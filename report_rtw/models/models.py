# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class report_rtw(models.Model):
#     _name = 'report_rtw.report_rtw'
#     _description = 'report_rtw.report_rtw'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
