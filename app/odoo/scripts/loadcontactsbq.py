#!/usr/bin/env python
"""A sample script to demonstrate some of functionalities of OERPLib."""
import odoorpc

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

# Simple 'raw' query
user_data = odoo.execute('res.users', 'read', [user.id])
print(user_data)

# Use all methods of a model
if 'sale.order' in odoo.env:
    Order = odoo.env['sale.order']
    order_ids = Order.search([])
    for order in Order.browse(order_ids):
        print(order.name)
        products = [line.product_id.name for line in order.order_line]
        print(products)

# Simple 'raw' query
cont_data = odoo.execute('res.partner', 'read', [user.id])
print(90*"=")
print(cont_data)

# Update data through a record
# user.name = "Brian Jones"
# new_contact_id = odoo.execute('res.partner', 'create', {
#       'login': ""
# })

# Simple 'raw' query
fld_data = odoo.execute('ir.model.fields', 'search_read', [
    ('model', '=', 'res.partner')])
print(90*"=")
print(fld_data)

# f = [
#     ['switchboard'],
#     ['accountnum'],
#     ['iscustomer'],
#     ['issupplier'],
#     ['isvatexempt'],
#     ['acceptsbackorders'],
#     [''],
# ]

cont_data = odoo.execute('res.partner', 'read', [user.id])

