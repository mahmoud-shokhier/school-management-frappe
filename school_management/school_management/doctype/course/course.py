# Copyright (c) 2022, mahmoud-shokhier and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class course(Document):
	def before_save(self):
		self.validate_enrolled_students()

	def validate_enrolled_students(self):
		# check if a valid membership exist for this library member
		for enrolled_student in self.enrolled_students:
			count = frappe.db.count(
				"student",
				{"first_name": enrolled_student.name.split('-')[0], "last_name": enrolled_student.name.split('-')[1], "level": self.level},
			)
			print('0000->>>>>>>>', count)
			if count == 0:
				frappe.throw("The member does not have a valid level")
			enrolled_student.level = self.level