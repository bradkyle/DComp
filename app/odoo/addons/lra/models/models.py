# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LRAEntity(models.Model):
    _name = 'lra.entity'
    _description = 'LRA principal contact'
    # LegalName	STRING	NULLABLE		
    entity_id = fields.Char()

    # PartnerID FLOAT	NULLABLE		
    # entity_partner_id = fields.Many2many(
    #       "res.partner", string="Entity partners", store=True)
    # DealerID	FLOAT	NULLABLE		
    entity_manager_id = fields.Many2one(
          "res.users", string="Entity manager", store=True)
    # DealerID	FLOAT	NULLABLE		
    dealer_id = fields.Many2one(
          "res.users", string="Entity dealer", store=True)
    # Company	STRING	NULLABLE		
    # company_ids = fields.Many2many(
    #       "res.users", string="Entity companies", store=True)
    # EntityTypeID	FLOAT	NULLABLE		
    # entity_type_id = fields.Many2one(
    #       "res.users", string="Entity companies", store=True)
    # EntityCategoryID	FLOAT	NULLABLE		
    # entity_category_id = fields.Many2one(
    #       "res.users", string="Entity companies", store=True)
    # EntityCreatorID	FLOAT	NULLABLE		
    entity_creator_id = fields.Many2one(
          "res.users", string="Entity creator", store=True)
    # EntityUpdaterID	FLOAT	NULLABLE		
    entity_updater_id = fields.Many2one(
          "res.users", string="Entity updater", store=True)
    # ABCCatID	FLOAT	NULLABLE		
    # abc_category_id = fields.Many2one(
    #       "res.users", string="Entity companies", store=True)
    # BusCatID	FLOAT	NULLABLE		
    # bus_category_id = fields.Many2one(
    #       "res.users", string="Entity companies", store=True)
    # LegalName	STRING	NULLABLE		
    legal_name = fields.Char()
    # Switchboard	STRING	NULLABLE		
    switchboard = fields.Char()
    # accountnum	STRING	NULLABLE		
    accountnum = fields.Char()
    # IsSupplier	FLOAT	NULLABLE		
    is_supplier = fields.Boolean()


# class LRAIncedent(models.Model):
#     _name = 'lra.incident'
#     _description = 'An incident that has occured in the LRA (i.e. Crime)'

#     time = fields.Date()
#     unit_number = fields.Char()
#     severity = fields.Char()
#     description = fields.Text()
#     entity_ids = fields.One2many(
#           "res.partner", string="Entity ids", store=True)
#     region = fields.Char()
#     coordinates = fields.Char()

