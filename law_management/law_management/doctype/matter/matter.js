// Copyright (c) 2022, Solufy and contributors
// For license information, please see license.txt

frappe.ui.form.on('Matter', {
	// refresh: function(frm) {

	// }

});
frappe.ui.form.on('Matter',{
	onload: function(frm) {
		cur_frm.set_query("assign_to", function() {
		return {
		"filters": {
			"is_lawyer": ("=", "1")
		}
		};
	});
	}
});

frappe.ui.form.on('Matter',{
	onload: function(frm) {
		cur_frm.set_query("client_name", function() {
		return {
		"filters": {
			"is_client": ("=", "1")
		}
		};
	});
	}
});


frappe.ui.form.on('Matter', {
	refresh: function(frm,cdt,cdn) {

		if(frm.doc.workflow_state == "In Progress" || frm.doc.workflow_state == "Approved" || frm.doc.workflow_state == "Closed"){
			frm.add_custom_button(__("Create Sales Invoice"), function() {	    		
				frappe.route_options = {
				    "sales_invoice": frm.doc.sales_invoice,
				    "status": "Open",
				    "reference_owner": frm.doc.owner
				};
				frappe.new_doc("Sales Invoice", {
					"customer": cur_frm.doc.client_name,
					"payment_type": frm.doc.payment_type,
					"item_code": frm.doc.name
				});
			}, __("View"));
		}

	}	
});


