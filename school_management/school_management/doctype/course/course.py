# Copyright (c) 2022, mahmoud-shokhier and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class course(Document):
	def before_save(self):
		self.validate_enrolled_students()

	def validate_enrolled_students(self):
		# check if a valid membership exist for this library member
		for student in self.enrolled_students:
			if int(student.level) != int(self.level):
				frappe.throw("The member does not have a valid level")
