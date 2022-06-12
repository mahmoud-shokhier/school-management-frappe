// Copyright (c) 2022, mahmoud-shokhier and contributors
// For license information, please see license.txt

frappe.ui.form.on('exam', {
	refresh: function (frm) {
		console.log(frm)
		frm.add_custom_button('Send emails to students', () => {
			frappe.db.get_doc('course', frm.doc.course)
				.then(course => {
					course.enrolled_students.forEach(element => {
						frappe.db.get_doc('student', element.student).then(student => {
							frm.call({
								method: "send_email_to_student",
								args: {
									'receiver_name': student.first_name,
									'receiver_email': student.email
								}
							})
								.fail(fail => console.log("failure", fail))
								.done(success => frappe.msgprint('Email successfully sent to ' + student.first_name));

						})
					});
				})
		})
	}
});
