# Copyright (c) 2022, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ClientRequest(Document):
	pass

def validate(self,cdt):
	if self.workflow_state == "Approved":	
			cr_id = self.name1
			cr_contact_no = self.contact_no	
			vals = frappe.get_doc({
				"doctype": "Customer",
				"customer_name":cr_id,
				"is_client": 1,
				"customer_group": "Government",
				"territory": "India",
				"customer_type":"Company" 
			})
			vals.insert()