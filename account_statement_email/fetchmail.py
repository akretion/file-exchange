# -*- coding: utf-8 -*-
###############################################################################
#
#   account_statement_email for OpenERP
#   Copyright (C) 2012-TODAY Akretion <http://www.akretion.com>.
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
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

class fetchmail_server(orm.Model):
    _inherit = "fetchmail.server"

    _columns = {
        'profile_id': fields.many2one('account.statement.profile', 'Bank Statement Profile'),
    }

    def get_file_type(self, cr, uid, context=None):
        res = super(fetchmail_server, self).get_file_type(cr, uid, context=context)
        res.append(('bank_statement', 'Bank Statement'))
        return res

    def get_context_for_server(self, cr, uid, server_id, context=None):
        server = self.browse(cr, uid, server_id, context=context)
        ctx = super(fetchmail_server, self).get_context_for_server(cr, uid, server_id, context=context)
        if server.file_type == 'bank_statement':
            ctx['default_file_document_vals'] = {
                    'statement_profile_id': server.profile_id.id,
                    'file_type': 'bank_statement',
                    }
        return ctx
