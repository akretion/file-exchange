# -*- coding: utf-8 -*-
###############################################################################
#
#   file_repository for OpenERP
#   Authors: Sebastien Beau <sebastien.beau@akretion.com>
#            Benoît Guillot <benoit.guillot@akretion.com>
#   Copyright 2013 Akretion
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

import os
import re
from openerp.osv import fields, orm
from openerp.addons.file_autotask_rel.file_document import add_task
from openerp.tools.translate import _
from tempfile import TemporaryFile
import base64

add_task('repository.task')


class FileDocument(orm.Model):
    _inherit = "file.document"

    _columns = {
        'repository_id': fields.many2one(
            'file.repository',
            'File Repository'),
    }

    def export_file_document(self, cr, uid, connection, file_doc,
                             context=None):
        task = file_doc.task_id
        filename = file_doc.datas_fname
        if task.rename_after_send:
            # check if we can get the new filename before to send it
            # so if the renaming fails, the file won't be send
            try:
                new_filename = task.get_rename_new_name(filename)
            except re.error as err:
                raise orm.except_orm(
                    _('Error'),
                    _('Cannot rename file with name %s. Please check the '
                      'rename settings of the task %s. Error: %s') %
                    (filename, task.name, err))

        folder = task.folder or ''
        outfile = TemporaryFile('w+b')
        decoded_datas = base64.decodestring(file_doc.datas)
        outfile.write(decoded_datas)
        outfile.seek(0)
        connection.send(folder, filename, outfile)
        if task.rename_after_send and filename != new_filename:
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)
            connection.rename(old_path, new_path)
        return outfile

    def _run(self, cr, uid, file_doc, context=None):
        super(FileDocument, self)._run(cr, uid, file_doc, context=context)
        repo_obj = self.pool['file.repository']
        if file_doc.direction == 'output' and file_doc.active is True:
            connection = repo_obj.repository_connection(
                cr, uid, file_doc.repository_id.id, context=context)
            self.export_file_document(cr, uid, connection, file_doc,
                                      context=context)
            file_doc.done()
