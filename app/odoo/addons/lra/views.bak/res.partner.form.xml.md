<?xml version="1.0"?>
<form string="Partners">
                <div class="alert alert-warning oe_edit_only" role="alert" attrs="{'invisible': [('same_vat_partner_id', '=', False)]}">
                  A partner with the same <span><span class="o_vat_label">Tax ID</span></span> already exists (<field name="same_vat_partner_id"/>), are you sure to create a new one?
                </div>
                <sheet>
                    <div class="oe_button_box" name="button_box"/>
                    <widget name="web_ribbon" title="Archived" bg_color="bg-danger" attrs="{'invisible': [('active', '=', True)]}"/>
                    <field name="avatar_128" invisible="1"/>
                    <field name="image_1920" widget="image" class="oe_avatar" options="{&quot;preview_image&quot;: &quot;avatar_128&quot;}"/>
                    <div class="oe_title mb24">
                        <field name="is_company" invisible="1"/>
                        <field name="commercial_partner_id" invisible="1"/>
                        <field name="active" invisible="1"/>
                        <field name="country_code" invisible="1"/>
                        <field name="company_type" widget="radio" options="{'horizontal': true}"/>
                        <h1>
                            <field id="company" class="o_text_overflow" name="name" default_focus="1" placeholder="e.g. Lumber Inc" attrs="{'required' : [('type', '=', 'contact'),('is_company', '=', True)], 'invisible': [('is_company','=', False)]}"/>
                            <field id="individual" class="o_text_overflow" name="name" default_focus="1" placeholder="e.g. Brandom Freeman" attrs="{'required' : [('type', '=', 'contact'), ('is_company', '=', False)], 'invisible': [('is_company','=', True)]}"/>
                        </h1>
                        <div class="o_row">
                            <field name="parent_id" widget="res_partner_many2one" placeholder="Company Name..." domain="[('is_company', '=', True)]" context="{'default_is_company': True, 'show_vat': True}" attrs="{'invisible': ['|', '&amp;', ('is_company','=', True),('parent_id', '=', False),('company_name', '!=', False),('company_name', '!=', '')]}"/>
                                <field name="company_name" attrs="{'invisible': ['|', '|', ('company_name', '=', False), ('company_name', '=', ''), ('is_company', '=', True)]}"/>
                                <button name="create_company" icon="fa-plus-square" string="Create company" type="object" class="oe_edit_only btn-link" attrs="{'invisible': ['|', '|', ('is_company','=', True), ('company_name', '=', ''), ('company_name', '=', False)]}"/>
                        </div>
                        <field string="Accepts backorders?" name="x_accepts_backorders"/>
                    </div>

                    <group>
                        <group>
                            <span class="o_form_label o_td_label" name="address_name">
                                <field name="type" attrs="{'invisible': [('is_company','=', True)], 'required': [('is_company','!=', True)], 'readonly': [('user_ids', '!=', [])]}" class="font-weight-bold"/>
                                <b attrs="{'invisible': [('is_company', '=', False)]}">Address</b>
                            </span>
                            <div class="o_address_format">
                                <field name="street" placeholder="Street..." class="o_address_street" attrs="{'readonly': [('type', '=', 'contact'),('parent_id', '!=', False)]}"/>
                                <field name="street2" placeholder="Street 2..." class="o_address_street" attrs="{'readonly': [('type', '=', 'contact'),('parent_id', '!=', False)]}"/>
                                <field name="city" placeholder="City" class="o_address_city" attrs="{'readonly': [('type', '=', 'contact'),('parent_id', '!=', False)]}"/>
                                <field name="state_id" class="o_address_state" placeholder="State" options="{'no_open': True, 'no_quick_create': True}" attrs="{'readonly': [('type', '=', 'contact'),('parent_id', '!=', False)]}" context="{'country_id': country_id, 'default_country_id': country_id, 'zip': zip}"/>
                                <field name="zip" placeholder="ZIP" class="o_address_zip" attrs="{'readonly': [('type', '=', 'contact'),('parent_id', '!=', False)]}"/>
                                <field name="country_id" placeholder="Country" class="o_address_country" options="{&quot;no_open&quot;: True, &quot;no_create&quot;: True}" attrs="{'readonly': [('type', '=', 'contact'),('parent_id', '!=', False)]}"/>
                            </div>
                            <field name="vat" placeholder="e.g. BE0477472701" attrs="{'readonly': [('parent_id','!=',False)]}"/>
                        </group>
                        <group>
                            <field name="function" placeholder="e.g. Sales Director" attrs="{'invisible': [('is_company','=', True)]}"/>
                            <field name="phone" widget="phone"/>
                            <field name="mobile" widget="phone"/>
                            <field name="user_ids" invisible="1"/>
                            <field name="email" widget="email" context="{'gravatar_image': True}" attrs="{'required': [('user_ids','!=', [])]}"/>
                            <field name="website" string="Website" widget="url" placeholder="e.g. https://www.odoo.com"/>
                            <field name="title" options="{&quot;no_open&quot;: True}" placeholder="e.g. Mister" attrs="{'invisible': [('is_company', '=', True)]}"/>
                            <field name="active_lang_count" invisible="1"/>
                            <label for="lang" attrs="{'invisible': [('active_lang_count', '&lt;=', 1)]}"/>
                            <div class="o_row" attrs="{'invisible': [('active_lang_count', '&lt;=', 1)]}">
                                <field name="lang"/>
                                <button type="action" name="56" class="btn-sm btn-link mb4 fa fa-globe" aria-label="More languages" groups="base.group_system" title="More languages"/>
                            </div>
                            <field name="category_id" widget="many2many_tags" options="{'color_field': 'color', 'no_create_edit': True}" placeholder="Tags..."/>
                        </group>
                    </group>

                    <notebook colspan="4">
                        <page string="Contacts &amp; Addresses" name="contact_addresses" autofocus="autofocus">
                            <field name="child_ids" mode="kanban" context="{'default_parent_id': active_id, 'default_street': street, 'default_street2': street2, 'default_city': city, 'default_state_id': state_id, 'default_zip': zip, 'default_country_id': country_id, 'default_lang': lang, 'default_user_id': user_id, 'default_type': 'other'}">
                                <kanban>
                                    <field name="id"/>
                                    <field name="color"/>
                                    <field name="name"/>
                                    <field name="title"/>
                                    <field name="type"/>
                                    <field name="email"/>
                                    <field name="parent_id"/>
                                    <field name="is_company"/>
                                    <field name="function"/>
                                    <field name="phone"/>
                                    <field name="street"/>
                                    <field name="street2"/>
                                    <field name="zip"/>
                                    <field name="city"/>
                                    <field name="country_id"/>
                                    <field name="mobile"/>
                                    <field name="state_id"/>
                                    <field name="image_128"/>
                                    <field name="avatar_128"/>
                                    <field name="lang"/>
                                    <!-- fields in form x2many view to diminish requests -->
                                    <field name="comment"/>
                                    <field name="x_accepts_backorders"/>
                                    <field name="display_name"/>
                                    <templates>
                                        <t t-name="kanban-box">
                                            <t t-set="color" t-value="kanban_color(record.color.raw_value)"/>
                                            <div t-att-class="color + (record.title.raw_value == 1 ? ' oe_kanban_color_alert' : '') + ' oe_kanban_global_click'">
                                                <div class="o_kanban_image">
                                                    <img alt="Contact image" t-att-src="kanban_image('res.partner', 'avatar_128', record.id.raw_value)"/>
                                                </div>
                                                <div class="oe_kanban_details">
                                                    <field name="name"/>
                                                    <div t-if="record.function.raw_value"><field name="function"/></div>
                                                    <div t-if="record.email.raw_value"><field name="email" widget="email"/></div>
                                                    <div t-if="record.type.raw_value != 'contact'">
                                                        <div>
                                                            <field name="zip"/>
                                                            <field name="city"/>
                                                        </div>
                                                        <field t-if="record.state_id.raw_value" name="state_id"/>
                                                        <field name="country_id"/>
                                                    </div>
                                                    <div t-if="record.phone.raw_value">Phone: <t t-esc="record.phone.value"/></div>
                                                    <div t-if="record.mobile.raw_value">Mobile: <t t-esc="record.mobile.value"/></div>
                                                </div>
                                            </div>
                                        </t>
                                    </templates>
                                </kanban>
                                <form string="Contact / Address">
                                    <sheet>
                                        <!-- parent_id and type fields needed in attrs in base_address_city module which overwrites
                                        _fields_view_get() of partner. It would be better to put those fields there but the web client
                                        dosen't support when a field is displayed several times in the same view.-->
                                        <field name="type" required="1" widget="radio" options="{'horizontal': true}"/>
                                        <field name="parent_id" invisible="1"/>
                                        <hr/>
                                        <group>
                                            <group>
                                                <field name="name" string="Contact Name" attrs="{'required' : [('type', '=', 'contact')]}"/>
                                                <field name="title" options="{'no_open': True}" placeholder="e.g. Mr." attrs="{'invisible': [('type','!=', 'contact')]}"/>
                                                <field name="function" placeholder="e.g. Sales Director" attrs="{'invisible': [('type','!=', 'contact')]}"/>
                                                <label for="street" string="Address" attrs="{'invisible': [('type','=', 'contact')]}"/>
                                                <div attrs="{'invisible': [('type','=', 'contact')]}">
                                                    <div class="o_address_format" name="div_address">
                                                        <field name="street" placeholder="Street..." class="o_address_street"/>
                                                        <field name="street2" placeholder="Street 2..." class="o_address_street"/>
                                                        <field name="city" placeholder="City" class="o_address_city"/>
                                                        <field name="state_id" class="o_address_state" placeholder="State" options="{'no_open': True, 'no_quick_create': True}" context="{'country_id': country_id, 'default_country_id': country_id, 'zip': zip}"/>
                                                        <field name="zip" placeholder="ZIP" class="o_address_zip"/>
                                                        <field name="country_id" placeholder="Country" class="o_address_country" options="{&quot;no_open&quot;: True, &quot;no_create&quot;: True}"/>
                                                    </div>
                                                </div>
                                            </group>
                                            <group>
                                                <field name="email" widget="email"/>
                                                <field name="phone" widget="phone"/>
                                                <field name="mobile" widget="phone"/>
                                                <field name="company_id" invisible="1"/>
                                            </group>
                                        </group>
                                        <group>
                                            <field name="comment" placeholder="Internal notes..."/>
                                        </group>
                                        <field name="lang" invisible="True"/>
                                        <field name="user_id" invisible="True"/>
                                    </sheet>
                                </form>
                            </field>
                        </page>
                        <page name="sales_purchases" string="Sales &amp; Purchase">
                            <group name="container_row_2">
                                <group string="Sales" name="sale" priority="1">
                                    <field name="user_id" domain="[('share', '=', False)]"/>
                                </group>
                                <group string="Purchase" name="purchase" priority="2">
                                </group>
                                <group name="misc" string="Misc">
                                    <field name="ref" string="Reference"/>
                                    <field name="company_id" groups="base.group_multi_company" options="{'no_create': True}" attrs="{'readonly': [('parent_id', '!=', False)]}" force_save="1"/>
                                    <field name="industry_id" attrs="{'invisible': [('is_company', '=', False)]}" options="{'no_create': True}"/>
                                </group>
                            </group>
                        </page>
                        <page name="internal_notes" string="Internal Notes">
                            <field name="comment" placeholder="Internal note..."/>
                        </page>
                    </notebook>
                </sheet>
                </form>
