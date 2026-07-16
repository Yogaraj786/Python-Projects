import mysql.connector

# 1. ESTABLISH CONNECTION (THE BRIDGE & KEYS)
backend =mysql.connector.connect(
    host='localhost',
    user='root',
    password='******',
    database='Bank_Project'
    )

print("Connected Successfully to MySQL!")

# 2. (CREATE THE CURSOR)
mycursor = backend.cursor()


import Connection
print(Connection.__file__)
print(Connection.backend.database)


import Connection
import customtkinter as Tkinder
from PIL import Image
from tkinter import messagebox

def save_data():
    user_id=e1.get()
    user_name=e2.get()
    bank_Acc=e3.get()
    amount=e4.get()
    bank_name=e5.get()
    
    view.insert("end",f"user_id = {user_id}\n")
    view.insert("end",f"user_name= {user_name}\n")
    view.insert("end",f"bank_Account= {bank_Acc}\n")
    view.insert("end",f"amount= {amount}\n")

    try:
        if transaction_var == "Deposit":
            update_query= "UPDATE Bank_Details SET balance = balance + amount WHERE Bank_Acc=bank_Acc"
            Connection.execute(update_query, (amount, bank_Acc))
            print(f"{amount} has been DEPOSITED to your account!")
            messagebox.showinfo("Success", f"₹{amount} Deposited successfully!")

        elif transaction_var == "Withdraw":
            update_query="UPDATE Bank_Details SET balance = balance - amount WHERE Bank_Acc = bank_Acc"
            Connection.execute(update_query, (amount, bank_Acc))
            print(f"{amount} has been WITHDRAWN from your account!")
            messagebox.showinfo("Success", f"₹{amount} Withdrawn successfully!")

            status = "Success"


            query=" insert into transactions(User_id,Bank_name,Bank_acc,Amount,status) values(%s,%s,%s,%s,%s)"
            val=(user_id,bank_name,bank_Acc,amount,status)
            Connection.execute(query,val)
            Connection.backend.commit()

    except Exception as e:

            Connection.backend.rollback() 
            
        
            status = "Failed"
            
            
            try:
                fail_query = "INSERT INTO transactions(User_id, Bank_name, Bank_acc, Amount, Trans_type, status) VALUES (%s, %s, %s, %s, %s, %s)"
                Connection.execute(fail_query, (user_id, user_name, bank_Acc, amount, transaction_var, status))
                Connection.backend.commit()
            except:
                pass
                
            messagebox.showerror("Transaction Failed", f"🛑 Error: Something went wrong!\n{e}")

            view.insert("end", f"[{status}] {transaction_var} of ₹{amount} for A/C: {bank_Acc}\n")

            e1.delete(0,"end")
            e2.delete(0,"end")
            e3.delete(0,"end")
            e4.delete(0,"end")


window=Tkinder.CTk()
window.title("Tkinder Payement App")
window.geometry("1920x1080")

transaction_var = Tkinder.StringVar(value="Deposit") 

# --- 2. Radio Buttons ---
radio_deposit = Tkinder.CTkRadioButton(window, text="Deposit (+)", variable=transaction_var, value="Deposit", fg_color="green")
radio_deposit.grid(row=5,column=1,padx=100,pady=20)

radio_withdraw = Tkinder.CTkRadioButton(window, text="Withdraw (-)", variable=transaction_var, value="Withdraw", fg_color="red")
radio_withdraw.grid(row=5,column=2,padx=100,pady=20)


view=Tkinder.CTkTextbox(window,width=250,height=400)
view.grid(row=7, column=1, columnspan=3, pady=20)

label1=Tkinder.CTkLabel(window,text="User Id").grid(row=1,padx=100,pady=20)
label2=Tkinder.CTkLabel(window,text="User Name").grid(row=2,padx=100,pady=20)
label3=Tkinder.CTkLabel(window,text="Bank Account").grid(row=3,padx=100,pady=20)
label4=Tkinder.CTkLabel(window,text="Amount").grid(row=4,padx=20,pady=20)
label5=Tkinder.CTkLabel(window,text="Bank_name").grid(row=5,padx=20,pady=20)

button1=Tkinder.CTkButton(window,text="Proceed",command=save_data)
button2=Tkinder.CTkButton(window,text="Cancel",command=window.destroy)
button1.grid(row=6,column=2,padx=100,pady=20)
button2.grid(row=6,column=3,padx=100,pady=20)

e1=Tkinder.CTkEntry(window)
e1.grid(row=1,column=2)
e2=Tkinder.CTkEntry(window)
e2.grid(row=2,column=2)
e3=Tkinder.CTkEntry(window)
e3.grid(row=3,column=2)
e4=Tkinder.CTkEntry(window)
e4.grid(row=4,column=2)
e5=Tkinder.CTkEntry(window)
e5.grid(row=5,column=2)

window.mainloop()

