# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Sale Management",
    "version": "15.0.0.1",
    "category": "Sale",
    "summary": "Manage sale order ",
    "author": "Ketan Jinjala",
    "depends": ["base", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_product_view.xml",
        "views/product_product_menu.xml",
    ],
    "license": "LGPL-3",
    "Application": True,
}
