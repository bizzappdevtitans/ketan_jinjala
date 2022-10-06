# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Management',
    'version' : '15.0.0.1',
    'category': 'Serivies/School',
    'summary': 'Manage school teacher',
    'author':'Ketan Jinjala',
    'depends' : ['base','sale','stock','account','purchase'],

    'data': [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "wizard/student_detail_wizard_view.xml",
        "views/res_config_settings_views.xml",
        "views/student_detail_view.xml",
        "views/teacher_detail_view.xml",
        "views/principale_detail_view.xml",
        "views/School_library_detail_view.xml",
        "views/class_detail_view.xml",
        "views/school_menu.xml",
        "views/sale_view.xml",
        "views/stock_move_view.xml",
        "views/stock_picking_view.xml",
        "views/account_move_views.xml",
        "views/mrp_production_views.xml",
        "views/purchase_order_view.xml",
        "views/project_view.xml",

    ],     
    'license': 'LGPL-3',
    'Application':True,
}
