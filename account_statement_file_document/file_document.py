# -*- coding: utf-8 -*-
###############################################################################
#
#   account_statement_repository for OpenERP
#   Copyright (C) 2013 Akretion (http://www.akretion.com). All Rights Reserved
#   @author Benoît GUILLOT <benoit.guillot@akretion.com>
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
import os


class file_document(orm.Model):
    _inherit = "file.document"

    def get_file_document_type(self, cr, uid, context=None):
        res = super(file_document, self).get_file_document_type(cr, uid, context=context)
        res.append(('bank_statement', 'Bank Statement Import'))
        return res

    _columns = {
        'statement_profile_id': fields.many2one('account.statement.profile',
                                                string='Account Statement Profile')
    }

    def _run(self, cr, uid, filedocument, context=None):
        if context is None:
            context = {}
        super(file_document, self)._run(cr, uid, filedocument, context=context)
        acc_profile_obj = self.pool['account.statement.profile']
        attach_obj = self.pool['ir.attachment']
        if filedocument.file_type == 'bank_statement':
            ctx = context.copy()
            ctx['default_file_id'] = filedocument.id
            (shortname, ftype) = os.path.splitext(filedocument.datas_fname)
            acc_profile_obj.multi_statement_import(
                                            cr,
                                            uid,
                                            False,
                                            filedocument.statement_profile_id.id,
                                            filedocument.datas,
                                            ftype.replace('.', ''),
                                            context=ctx,
                                        )
