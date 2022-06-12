# Copyright (c) 2022, mahmoud-shokhier and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class exam(Document):	
	pass


@frappe.whitelist()
def send_email_to_student(**args):

	print('heelloooooo---->', args['receiver_name'], args['receiver_email'])
	content = frappe.render_template('school_management/templates/emails/email_template.html', {
			'recipient_name': args['receiver_name'],
			'email': args['receiver_email']
			#put here the variables in the template
		})
	frappe.sendmail(
		recipients =  args['receiver_email'], #this is the email to your recipient as you want
		sender = "mahmoud.aly.shokhier@gmail.com",
		subject = "The subject of your email",
		content = content,
		now = True
	)
