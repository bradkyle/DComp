# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LRAEntity(models.Model):
    _name = 'lra.entity'
    _description = 'lra.lra'

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
    # DateAdded	STRING	NULLABLE		
    date_added = fields.Date()
    # DateModified	STRING	NULLABLE		
    date_modified = fields.Date()
    # LegalName	STRING	NULLABLE		
    legal_name = fields.()
    # Switchboard	STRING	NULLABLE		
    Switchboard = fields.()
    # Fax	STRING	NULLABLE		
    Fax = fields.()
    # URL	FLOAT	NULLABLE		
    URL = fields.()
    # Email	STRING	NULLABLE		
    Email = fields.()
    # VATnum	FLOAT	NULLABLE		
    VATnum = fields.()
    # VATexemptNum	FLOAT	NULLABLE		
    VATexempt_num = fields.()
    # AcceptsBackOrders	INTEGER	NULLABLE		
    accepts_back_orders = fields.()
    # MenthodOfContact	FLOAT	NULLABLE		
    menthod_of_contact = fields.()
    # catdesc	FLOAT	NULLABLE		
    catdesc = fields.()
    # website	FLOAT	NULLABLE		
    website = fields.()
    # comptel	FLOAT	NULLABLE		
    comptel = fields.()
    # NextCallDate	FLOAT	NULLABLE		
    next_call_date = fields.()
    # accounttypeid	FLOAT	NULLABLE		
    accounttypeid = fields.()
    # dateupdated	FLOAT	NULLABLE		
    dateupdated = fields.()
    # TempID	FLOAT	NULLABLE		
    temp_iD = fields.()
    # compregnum	FLOAT	NULLABLE		
    compregnum = fields.()
    # accountnum	STRING	NULLABLE		
    accountnum = fields.()
    # modifiedby	STRING	NULLABLE		
    modifiedby = fields.()
    # IsAccountCustomer	FLOAT	NULLABLE		
    is_account_customer = fields.()
    # AccountSupplierID	FLOAT	NULLABLE		
    account_supplier_iD = fields.()
    # AccountCustomerID	FLOAT	NULLABLE		
    account_customer_iD = fields.()
    # IsBirthDaySupplier	FLOAT	NULLABLE		
    is_birth_day_supplier = fields.()
    # IsBirthDayCourier	FLOAT	NULLABLE		
    is_birth_day_courier = fields.()
    # IsAnniversaryCourier	FLOAT	NULLABLE		
    is_anniversary_courier = fields.()
    # IsAnniversarySupplier	FLOAT	NULLABLE		
    is_anniversary_supplier = fields.()
    # IsAccountSupplier	FLOAT	NULLABLE		
    is_account_supplier = fields.()
    # IsSupplier	FLOAT	NULLABLE		
    is_supplier = fields.()
    # InvoiceTo	FLOAT	NULLABLE		
    invoice_to = fields.()
    # Currency	FLOAT	NULLABLE		
    Currency = fields.()
    # CreditLimit	FLOAT	NULLABLE		
    credit_limit = fields.()
    # PaymentTerms	FLOAT	NULLABLE		
    payment_terms = fields.()
    # SDLNo	FLOAT	NULLABLE		
    SDLNo = fields.()
    # SICCode	FLOAT	NULLABLE		
    SICCode = fields.()
    # OFONo	FLOAT	NULLABLE		
    OFONo = fields.()
    # Markup	FLOAT	NULLABLE		
    Markup = fields.()
    # ClientRating	FLOAT	NULLABLE		
    client_rating = fields.()
    # Manualrating	FLOAT	NULLABLE		
    Manualrating = fields.()
    # SalesConsID	FLOAT	NULLABLE		
    sales_cons_iD = fields.()
    # AlternateCompanyID	FLOAT	NULLABLE		
    alternate_company_iD = fields.()
    # Comments	STRING	NULLABLE		
    Comments = fields.()
    # CardTypeID	FLOAT	NULLABLE		
    card_type_iD = fields.()
    # CreditCardName	FLOAT	NULLABLE		
    credit_card_name = fields.()
    # CreditCardNumber	FLOAT	NULLABLE		
    credit_card_number = fields.()
    # Expmonth	FLOAT	NULLABLE		
    Expmonth = fields.()
    # ExpYear	FLOAT	NULLABLE		
    exp_year = fields.()
    # BankReconNotes	FLOAT	NULLABLE		
    bank_recon_notes = fields.()
    # AccStatID	FLOAT	NULLABLE		
    acc_stat_iD = fields.()
    # AvgPaymentTime	FLOAT	NULLABLE		
    avg_payment_time = fields.()
    # VendorNumber	STRING	NULLABLE		
    vendor_number = fields.()
    # SourceID	FLOAT	NULLABLE		
    source_iD = fields.()
    # PriceListID	FLOAT	NULLABLE		
    price_list_iD = fields.()
    # BankBranchName	FLOAT	NULLABLE		
    bank_branch_name = fields.()
    # BankBranchCode	FLOAT	NULLABLE		
    bank_branch_code = fields.()


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class LRAEntityAddress(models.Model):
    _name = 'lra.lra'
    _description = 'lra.lra'

    # EntityAddressID	INTEGER	NULLABLE		
    entity_address_iD = fields.()
    # EntityID	STRING	NULLABLE		
    entity_iD = fields.()
    # AddressType	STRING	NULLABLE		
    address_type = fields.()
    # Address1	STRING	NULLABLE		
    Address1 = fields.()
    # Address2	STRING	NULLABLE		
    Address2 = fields.()
    # Address3	STRING	NULLABLE		
    Address3 = fields.()
    # City	STRING	NULLABLE		
    City = fields.()
    # Region	STRING	NULLABLE		
    Region = fields.()
    # Code	STRING	NULLABLE		
    Code = fields.()
    # Country	STRING	NULLABLE		
    Country = fields.()
    # State	STRING	NULLABLE		
    State = fields.()
    # TempID	STRING	NULLABLE		
    temp_iD = fields.()
    # IsDefault	INTEGER	NULLABLE		
    is_default = fields.()
    # Address4	STRING	NULLABLE		
    Address4 = fields.()

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class LRAEntityContactGroup(models.Model):
    _name = 'lra.lra'
    _description = 'lra.lra'

    # EntityContactGroupID	INTEGER	NULLABLE		
    entity_contact_group_iD = fields.()
    # EntityContactID	INTEGER	NULLABLE		
    entity_contact_iD = fields.()
    # GroupID	INTEGER	NULLABLE	
    group_iD = fields.()

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class LRAEntityContact(models.Model):
    _name = 'lra.lra'
    _description = 'lra.lra'

    # EntityContactID	INTEGER	NULLABLE		
    entity_contact_iD = fields.()
    # EntityID	STRING	NULLABLE		
    entity_iD = fields.()
    # EntityTypeID	STRING	NULLABLE		
    entity_type_iD = fields.()
    # EntityCategoryID	STRING	NULLABLE		
    entity_category_iD = fields.()
    # AlternateContactID	STRING	NULLABLE		
    alternate_contact_iD = fields.()
    # EntityContactUpdaterID	STRING	NULLABLE		
    entity_contact_updater_iD = fields.()
    # EntityContactCreatorID	STRING	NULLABLE		
    entity_contact_creator_iD = fields.()
    # PhysicalAddrID	STRING	NULLABLE		
    physical_addr_iD = fields.()
    # PostalAddrID	STRING	NULLABLE		
    postal_addr_iD = fields.()
    # ContTypeID	STRING	NULLABLE		
    cont_type_iD = fields.()
    # PositionID	STRING	NULLABLE		
    position_iD = fields.()
    # InterestID	STRING	NULLABLE		
    interest_iD = fields.()
    # SalesConsID	STRING	NULLABLE		
    sales_cons_iD = fields.()
    # buscatid	STRING	NULLABLE		
    buscatid = fields.()
    # ABCcatid	STRING	NULLABLE		
    ABCcatid = fields.()
    # IsDefault	STRING	NULLABLE		
    is_default = fields.()
    # Company	STRING	NULLABLE		
    Company = fields.()
    # FirstName	STRING	NULLABLE		
    first_name = fields.()
    # Surname	STRING	NULLABLE		
    Surname = fields.()
    # Title	STRING	NULLABLE		
    Title = fields.()
    # Initials	STRING	NULLABLE		
    Initials = fields.()
    # Phone1	STRING	NULLABLE		
    Phone1 = fields.()
    # Phone2	STRING	NULLABLE		
    Phone2 = fields.()
    # Phone3	STRING	NULLABLE		
    Phone3 = fields.()
    # HomePhone	STRING	NULLABLE		
    home_phone = fields.()
    # Cell	STRING	NULLABLE		
    Cell = fields.()
    # Fax	STRING	NULLABLE		
    Fax = fields.()
    # Email	STRING	NULLABLE		
    Email = fields.()
    # Ext	STRING	NULLABLE		
    Ext = fields.()
    # Department	STRING	NULLABLE		
    Department = fields.()
    # Spouse	STRING	NULLABLE		
    Spouse = fields.()
    # AsstTitle	STRING	NULLABLE		
    asst_title = fields.()

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class LRAEntityGroup(models.Model):
    _name = 'lra.lra'
    _description = 'lra.lra'

    # EntityGroupID	INTEGER	NULLABLE		
    entity_group_iD = fields.()
    # EntityID	STRING	NULLABLE		
    entity_iD = fields.()
    # GroupID	INTEGER	NULLABLE		
    group_iD = fields.()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class LRACrimeEvent(models.Model):
    _name = 'lra.lra'
    _description = 'lra.lra'

    time=field.()
    unit_number=field.()
    severity=field.()
    description=field.()
    category=field.()
    region=field.()
    coordinates=field.()
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
