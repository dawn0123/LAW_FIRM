# Copyright (c) 2022, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Matter(Document):
	pass

def validate(self,cdt):
	test_d = frappe.db.get_value("Item",{'name':self.name},'name')
	if not test_d:
		vals = frappe.get_doc({
			"doctype": "Item",
			"name":self.name,
			"item_name":self.matter_name,
			"item_code":self.name,
			"item_group":"All Item Groups"

			})
		vals.insert()
	
		