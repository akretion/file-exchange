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


class RepositoryTask(orm.Model):
    _inherit = "repository.task"

    _columns = {
        'import_model': fields.char('Model')
    }

    def prepare_document_vals(self, cr, uid, task, file_name, datas,
                              context=None):
        vals = super(RepositoryTask, self).prepare_document_vals(
            cr, uid, task, file_name, datas, context=context)
        if task.type == 'import_data':
            vals.update({'file_type': task.type,
                         'import_model': task.import_model})
        return vals
