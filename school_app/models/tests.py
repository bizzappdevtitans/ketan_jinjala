# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.purchase_requisition.tests.common import TestStudentDetail


class TestStudent(TestStudentDetail):


 def test_some_action(self):
 	print("*--*******************************************************************************")
    # add a record in a model.
    record = self.env['model.student_detail'].create({'field': 'value'})
    record.some_action()
    # Check if the field and match the expected result
    self.student_detail(record.field, 'expected_field_value')
    print('Your test was successful!')


