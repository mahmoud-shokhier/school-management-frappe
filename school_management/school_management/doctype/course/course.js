// Copyright (c) 2022, mahmoud-shokhier and contributors
// For license information, please see license.txt
frappe.ui.form.on("course", {

})

frappe.ui.form.on("enrolled students", "student", function (doc, cdt, cdn) {
	//
	let row = frappe.get_doc(cdt, cdn);
	console.log('student', row)
	frappe.db.get_doc('student', row.student)
		.then(child_doc => {
			console.log('call-->')
			console.log(child_doc)
			if (doc.doc.level != child_doc.level) {
				frappe.msgprint('This student is not in the same level of the course')
			}
		})
})
