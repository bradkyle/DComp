#!/usr/bin/env python
"""A sample script to demonstrate some of functionalities of OERPLib."""
import odoorpc
import pandas as pd

# XMLRPC server configuration
SERVER = 'localhost'
PROTOCOL = 'xmlrpc'
PORT = 8069
# Name of the OpenERP database to use
DATABASE = 'lradev'

USER = 'odooscript@izonsa.dev'
PASSWORD = 'OuyQKg4HYyr6ZE'

# Prepare the connection to the server
odoo = odoorpc.ODOO(SERVER, port=PORT)

# Check available databases
print(odoo.db.list())

# Login
odoo.login(DATABASE, USER, PASSWORD)

# Current user
user = odoo.env.user
print(user.name)            # name of the user connected
print(user.company_id.name) # the name of its company

df = pd.read_csv('../../../.research/lra_data/csv/').fillna(0)

res = [{
    "entity_manager_id": int(user.id),
    "dealer_id": int(user.id),
    "entity_id": int(d["EntityID"]),
    "entity_category_id": int(d["EntityCategoryID"]),
    "entity_creator_id": int(user.id),
    "entity_updater_id": int(user.id),
    "abc_category_id": int(d["ABCCatID"]),
    "bus_category_id": int(d["BusCatID"]),
    "legal_name": d["LegalName"],
    "switchboard": d["Switchboard"],
    "email": d["Email"],
    "accepts_back_orders": bool(d["AcceptsBackOrders"]),
    "accountnum": d["accountnum"],
    "is_supplier": bool(d["IsSupplier"]),
} for d in df.to_records()]
