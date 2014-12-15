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


class automatic_task(orm.Model):
    _inherit = "automatic.task"

    def get_task_type(self, cr, uid, context=None):
        res = super(automatic_task, self).get_task_type(cr, uid, context=context)
        res.append(('bank_statement', 'Bank Statement Import'))
        return res

    _columns = {
    }
