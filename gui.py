                       GUI APPLICATION USING TKINTER WITH DATABASE:
import tkinter as tk
from tkinter import messagebox

class DanceClassApp:
	def __init__(self, root):
    	self.root = root
    	self.root.title("DANCE CLASS APPLICATION")

    	self.root.config(bg="lightpink")

    	self.label_name = tk.Label(self.root, text="Name:", font=("Helvetica", 12), bg="lightpink")
    	self.label_name.grid(row=0, column=0, pady=10, padx=10)
   	 
    	self.entry_name = tk.Entry(self.root, font=("Helvetica", 12), bg="white")
    	self.entry_name.grid(row=0, column=1, pady=10)

    	self.label_age = tk.Label(self.root, text="Age:", font=("Helvetica", 12), bg="lightpink")
    	self.label_age.grid(row=1, column=0, pady=10, padx=10)
   	 
    	self.entry_age = tk.Entry(self.root, font=("Helvetica", 12), bg="white")
    	self.entry_age.grid(row=1, column=1, pady=10)

    	self.label_email = tk.Label(self.root, text="Email:", font=("Helvetica", 12), bg="lightpink")
    	self.label_email.grid(row=2, column=0, pady=10, padx=10)
   	 
    	self.entry_email = tk.Entry(self.root, font=("Helvetica", 12), bg="white")
    	self.entry_email.grid(row=2, column=1, pady=10)

    	self.label_phone = tk.Label(self.root, text="Phone Number:", font=("Helvetica", 12), bg="lightpink")
    	self.label_phone.grid(row=3, column=0, pady=10, padx=10)
   	 
    	self.entry_phone = tk.Entry(self.root, font=("Helvetica", 12), bg="white")
    	self.entry_phone.grid(row=3, column=1, pady=10)

    	self.label_gender = tk.Label(self.root, text="Gender:", font=("Helvetica", 12), bg="lightpink")
    	self.label_gender.grid(row=4, column=0, pady=10, padx=10)

    	self.gender_var = tk.StringVar()

    	self.radio_male = tk.Radiobutton(self.root, text="Male", variable=self.gender_var, value="Male", font=("Helvetica", 12), bg="white")
    	self.radio_male.grid(row=4, column=1, sticky="w")

    	self.radio_female = tk.Radiobutton(self.root, text="Female", variable=self.gender_var, value="Female", font=("Helvetica", 12), bg="white")
    	self.radio_female.grid(row=5, column=1, sticky="w")

    	self.radio_other = tk.Radiobutton(self.root, text="Other", variable=self.gender_var, value="Other", font=("Helvetica", 12), bg="white")
    	self.radio_other.grid(row=6, column=1, sticky="w")

    	self.button_apply = tk.Button(self.root, text="Apply for Dance Class", font=("Helvetica", 12), command=self.apply_for_class, bg="lightblue")
    	self.button_apply.grid(row=7, column=0, columnspan=2, pady=10)

    	self.base_fee = 1000 # Standard class fee in rupees
    	self.gst_rate = 0.18# GST rate of 18%

    	
    	self.gst_amount = self.base_fee * self.gst_rate
    	self.fees = self.base_fee + self.gst_amount

    	
    	self.label_fees = tk.Label(self.root, text=f"GST AMOUNT: ₹{self.gst_amount:.2f}", font=("Helvetica", 14), bg="lightpink")
    	self.label_fees.grid(row=8, column=0, columnspan=2, pady=10)

    	# Fee Transaction Entry Label
    	self.label_amount = tk.Label(self.root, text="Amount:", font=("Helvetica", 12), bg="lightpink")
    	self.label_amount.grid(row=9, column=0, pady=10)

    	self.entry_amount = tk.Entry(self.root, font=("Helvetica", 12), bg="white")
    	self.entry_amount.grid(row=9, column=1, pady=10)

    	self.button_pay = tk.Button(self.root, text="Pay Fee", font=("Helvetica", 12), command=self.pay_fee, bg="lightblue")
    	self.button_pay.grid(row=10, column=0, pady=10)

    	self.button_refund = tk.Button(self.root, text="Refund Fee", font=("Helvetica", 12), command=self.refund_fee, bg="lightblue")
    	self.button_refund.grid(row=10, column=1, pady=10)

    	self.button_clear = tk.Button(self.root, text="Clear", font=("Helvetica", 12), command=self.clear, bg="lightblue")
    	self.button_clear.grid(row=11, column=0, columnspan=2, pady=10)

	def update_fees(self):
    	"""Updates the class fees label with the total fee including GST"""
    	self.label_fees.config(text=f"GST AMOUNT: ₹{self.gst_amount:.2f}\nTotal Fee: ₹{self.fees:.2f}")

	def pay_fee(self):
    	"""Handle fee payment transaction"""
    	try:
        	amount = float(self.entry_amount.get())
        	if amount <= 0:
            	raise ValueError("Amount must be positive.")
        	self.fees += amount
        	self.update_fees()
        	messagebox.showinfo("Transaction Success", f"Paid ₹{amount}. Total fees: ₹{self.fees:.2f}")
    	except ValueError as ve:
        	messagebox.showerror("Invalid Input", str(ve))
    	except Exception as e:
        	messagebox.showerror("Error", str(e))

	def refund_fee(self):
    	"""Handle fee refund transaction"""
    	try:
        	amount = float(self.entry_amount.get())
        	if amount <= 0:
            	raise ValueError("Amount must be positive.")
        	if amount > self.fees:
            	raise ValueError("Refund amount exceeds total fees.")
        	self.fees -= amount
        	self.update_fees()
        	messagebox.showinfo("Transaction Success", f"Refunded ₹{amount}. Remaining fees: ₹{self.fees:.2f}")
    	except ValueError as ve:
        	messagebox.showerror("Invalid Input", str(ve))
    	except Exception as e:
        	messagebox.showerror("Error", str(e))

	def apply_for_class(self):
    	"""Handle student application"""
    	try:
        	name = self.entry_name.get().strip()
        	age = int(self.entry_age.get())
        	email = self.entry_email.get().strip()
        	phone = self.entry_phone.get().strip()
        	gender = self.gender_var.get()

        	# Validate student details
        	if not name or not email or not phone or not gender:
            	raise ValueError("All fields are required.")

        	if not (3 <= age <= 60):
            	raise ValueError("Age must be between 3 and 60 years.")
       	 
        	messagebox.showinfo("Application Successful", f"Student {name} successfully applied for the dance class!\nAge: {age}\nGender: {gender}\nEmail: {email}\nPhone: {phone}")

    	except ValueError as ve:
        	messagebox.showerror("Invalid Input", str(ve))
    	except Exception as e:
        	messagebox.showerror("Error", str(e))

	def clear(self):
    	"""Clear the entry fields"""
    	self.entry_name.delete(0, tk.END)
    	self.entry_age.delete(0, tk.END)
    	self.entry_email.delete(0, tk.END)
    	self.entry_phone.delete(0, tk.END)
    	self.entry_amount.delete(0, tk.END)
    	self.gender_var.set("")  # Reset the gender radio button selection

if __name__ == "__main__":
	root = tk.Tk()
	app = DanceClassApp(root)
	root.mainloop()


