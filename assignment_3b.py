# Created by Matthew Walsh
# Created on oct 2017
# Created for ICS3U
# this program will calculate the price of pizza

import ui

HST = 0.13
def calculate_button(sender):
	size_control = view['size_control'].selected_index
	topping_control = view['topping_control'].selected_index
	
	if size_control == 0:
		size_cost = 6
	elif size_control == 1:
	  size_cost = 10
	
	if topping_control == 0:
		topping_cost = 1
	elif topping_control == 1:
		topping_cost = 1.75
	elif topping_control == 2:
		topping_cost = 2.5
	else:
	  topping_cost = 3.25
	  
	subtotal = topping_cost + size_cost
	hst_total = subtotal * HST
	total = subtotal + hst_total
	view['subtotal_label'].text = str(subtotal)
	view['hst_label'].text = str(round(hst_total, 2))
	view['total_label'].text = str(round(total, 2))


view = ui.load_view()
view.present('full_screen')
