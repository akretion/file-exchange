# -*- coding: utf-8 -*-
###############################################################################
#
#   account_statement_email for OpenERP
#   Copyright (C) 2012-TODAY Akretion <http://www.akretion.com>.
#   @author Florian da Costa <florian.dacosta@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import fields, orm

class file_document(orm.Model):
    _inherit = "file.document"

    def _get_file_document_data(self, cr, uid, condition, msg, att, context=None):
        vals = super(file_document, self)._get_file_document_data(cr, uid, condition, msg, att, context=context)
        if condition.profile_id:
            vals['statement_profile_id'] = condition.profile_id.id
        return vals

class file_document_condition(orm.Model):
    _inherit = "file.document.condition"

    _columns = {
        'profile_id': fields.many2one('account.statement.profile', 'Bank Statement Profile'),
    }


