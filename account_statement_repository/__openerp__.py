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


{
    'name': 'account_statement_repository',
    'version': '0.1',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """
    This module use tasks created with the module file_repository to import automaticaly account statements.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['file_repository',
                'account_statement_file_document',
                ],
    'demo': [],
    'data': [
           'file_repository_view.xml',
    ],
    'installable': True,
    'active': False,
}
