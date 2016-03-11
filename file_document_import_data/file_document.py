# -*- coding: utf-8 -*-
##############################################################################
#
#   account_statement_file_document for OpenERP
#   Copyright (C) 2016-TODAY Akretion <http://www.akretion.com>.
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
##############################################################################

from openerp.osv import fields, orm
import base64


class FileDocument(orm.Model):
    _inherit = "file.document"

    def get_file_document_type(self, cr, uid, context=None):
        res = super(FileDocument, self).get_file_document_type(
            cr, uid, context=context)
        res.append(('import_data', 'Import Data'))
        return res

    _columns = {
        'import_model': fields.many2one('ir.model', 'Model')
    }

    def get_import_file_format(self, cr, uid, context=None):
        return {
            'headers': True,
            'quoting': '"',
            'separator': ',',
            'encoding': 'utf-8'
        }

    def _run(self, cr, uid, filedocument, context=None):
        if context is None:
            context = {}
        super(FileDocument, self)._run(cr, uid, filedocument, context=context)
        import_obj = self.pool['base_import.import']
        if filedocument.file_type == 'import_data':
            options = self.get_import_file_format(cr, uid, context=context)

            import_vals = {
                'res_model': filedocument.import_model.model,
                'file': base64.b64decode(filedocument.datas),
                'file_name': filedocument.datas_fname,
            }
            import_wizard_id = import_obj.create(
                cr, uid, import_vals, context=context)
            parse_datas = import_obj.parse_preview(
                cr, uid, import_wizard_id, options, count=10, context=context)
            fields = map(lambda (k, v): v and v[0] or False,
                parse_datas['matches'].iteritems())
            messages = import_obj.do(cr, uid, import_wizard_id, fields,
                    options, dryrun=False, context=context)
            if messages:
                messages = [str(rec) for rec in messages]
                raise orm.except_orm('Import Data error', '\n'.join(messages))
        return
