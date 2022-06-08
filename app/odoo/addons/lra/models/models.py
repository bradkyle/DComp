# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LRAEntity(models.Model):
    _inherit = 'res.partner'
    _description = 'LRA principal contact'

    # DealerID	FLOAT	NULLABLE		
    entity_manager_id = fields.Many2one(
          "res.users", string="Entity manager", store=True)
    # DealerID	FLOAT	NULLABLE		
    dealer_id = fields.Many2one(
          "res.users", string="Entity dealer", store=True)
    # Company	STRING	NULLABLE		
    company_ids = fields.Many2many(
          "res.users", string="Entity companies", store=True)
    # EntityTypeID	FLOAT	NULLABLE		
    entity_type_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # EntityCategoryID	FLOAT	NULLABLE		
    entity_category_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # EntityCreatorID	FLOAT	NULLABLE		
    entity_creator_id = fields.Many2one(
          "res.users", string="Entity creator", store=True)
    # EntityUpdaterID	FLOAT	NULLABLE		
    entity_updater_id = fields.Many2one(
          "res.users", string="Entity updater", store=True)
    # ABCCatID	FLOAT	NULLABLE		
    abc_category_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # BusCatID	FLOAT	NULLABLE		
    bus_category_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # Notes	FLOAT	NULLABLE		
    Notes = fields.Text()
    # LegalName	STRING	NULLABLE		
    legal_name = fields.Char()
    # Switchboard	STRING	NULLABLE		
    Switchboard = fields.Char()
    # Fax	STRING	NULLABLE		
    Fax = fields.Char()
    # URL	FLOAT	NULLABLE		
    URL = fields.Char()
    # Email	STRING	NULLABLE		
    Email = fields.Char()
    # VATnum	FLOAT	NULLABLE		
    VATnum = fields.Char()
    # VATexemptNum	FLOAT	NULLABLE		
    VATexempt_num = fields.Char()
    # AcceptsBackOrders	INTEGER	NULLABLE		
    accepts_back_orders = fields.Boolean()
    # MenthodOfContact	FLOAT	NULLABLE		
    menthod_of_contact = fields.Char()
    # catdesc	FLOAT	NULLABLE		
    catdesc = fields.Char()
    # website	FLOAT	NULLABLE		
    website = fields.Char()
    # comptel	FLOAT	NULLABLE		
    comptel = fields.Char()
    # NextCallDate	FLOAT	NULLABLE		
    next_call_date = fields.Date()
    # accounttypeid	FLOAT	NULLABLE		
    account_type_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # compregnum	FLOAT	NULLABLE		
    compregnum = fields.Char()
    # accountnum	STRING	NULLABLE		
    accountnum = fields.Char()
    # IsAccountCustomer	FLOAT	NULLABLE		
    is_account_customer = fields.Boolean()
    # AccountSupplierID	FLOAT	NULLABLE		
    account_supplier_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # AccountCustomerID	FLOAT	NULLABLE		
    account_customer_id = fields.Many2one(
          "res.users", string="Entity companies", store=True)
    # IsBirthDaySupplier	FLOAT	NULLABLE		
    is_birth_day_supplier = fields.Boolean()
    # IsBirthDayCourier	FLOAT	NULLABLE		
    is_birth_day_courier = fields.Boolean()
    # IsAnniversaryCourier	FLOAT	NULLABLE		
    is_anniversary_courier = fields.Boolean()
    # IsAnniversarySupplier	FLOAT	NULLABLE		
    is_anniversary_supplier = fields.Boolean()
    # IsAccountSupplier	FLOAT	NULLABLE		
    is_account_supplier = fields.Boolean()
    # IsSupplier	FLOAT	NULLABLE		
    is_supplier = fields.Boolean()


class LRACrimeEvent(models.Model):
    _name = 'lra.lra'
    _description = 'lra.lra'

    time = field.Date()
    unit_number = field.Char()
    severity = field.()
    description = field.Text()
    entity_ids = fields.One2Many(
          "res.users", string="Entity ids", store=True)
    region = field.Char()
    coordinates = field.Char()

