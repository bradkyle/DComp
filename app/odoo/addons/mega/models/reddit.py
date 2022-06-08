# -*- coding: utf-8 -*-
from odoo import models, fields, api


class RedditComment(models.Model):
    _inherit = 'res.partner'
    _description = 'LRA principal contact'

class RedditSubmission(models.Model):
    _inherit = 'res.partner'
    _description = 'LRA principal contact'

class RedditSubreddit(models.Model):
    _inherit = 'res.partner'
    _description = 'LRA principal contact'

class RedditMessage(models.Model):
    _inherit = 'res.partner'
    _description = 'LRA principal contact'
