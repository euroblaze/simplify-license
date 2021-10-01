# -*- coding: utf-8 -*-

from odoo import models, fields, api


class simplify_licences(models.Model):
    _name = 'simplify_licences.simplify_licences'
    _description = 'simplify_licences.simplify_licences'

    name = fields.Char()
    value = fields.Char()
    description = fields.Text()
    date_start = fields.Date("Starting Date")
    date_end = fields.Date('Expiration Date')
    partner_id = fields.Many2one('res.partner', string = 'Customer')
    active = fields.Boolean(string = 'Active', default = True)
    module_list = fields.Char(string = "Modules Installed")
    number_of_modules = fields.Integer(string = "Number of modules installed")



    # price of the whole package (as total price)
    # price per module
    # accomodate 3rd party modules (take the author + field for number of sold copies -> can be new menu)
    
