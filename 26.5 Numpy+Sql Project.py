import mysql.connector

# 1. ESTABLISH CONNECTION (THE BRIDGE & KEYS)

backend =mysql.connector.connect(
    host='localhost',
    user='root',
    password='******',
    database='Numpy_Project'
    )

print("Connected Successfully to MySQL!")

dict_cursor=backend.cursor(dictionary=True)

import Connection
print(Connection.__file__)
print(Connection.backend.database)




import Connection
import numpy as np

query="""
select c.*,t.* from customers c
inner join transactions t on c.customer_id = t.customer_id
"""

Connection.mycursor.execute(query)
data =Connection.mycursor.fetchall()

arr = np.array(data)


income = arr[:,1]
spending = arr[:,2]
loan = arr[:,3]
credit = arr[:,4]

trans_id=arr[:,5]
customer_id=arr[:,6]
amount=arr[:,7]
txn_type=arr[:,8]
txn_type = txn_type.astype(str) #---> This Is used to change the array to pure string array
Tnx_type=np.char.lower(txn_type) #---> why its change to lower i can use any kind case to find the exact word


print(income,"\n",spending,"\n",loan,"\n",credit)
print(trans_id,"\n",customer_id,"\n",amount,"\n",txn_type)


Income_Change=np.where(income=="none",np.nan,income)
Income_Change=income.astype(float)  #---> this step is necessary to convert the string values to (float) 
                                                    #after replacing "none" with np.nan
print(Income_Replace)

'''-------------Handle Missing Values------------------------------------'''

Nanmean=np.nanmean(Income_Change)
print(Nanmean)

Income_Replace=np.where(np.isnan(Income_Change),Nanmean,Income_Change)
print(Income_Replace)

'''------------Basic Calculations---Total loan amount---Average income----Maximum credit score----------'''

Total_load_amount=np.sum(Income_Replace)
print("Total Loan Amount:",Total_load_amount)

Average_Income_Amount=np.average(Income_Replace)
print("Average Income Amount :",Average_Income_Amount)

Maximum_Credit_score=np.max(credit)
print("Maximun Credit Score Is :",Maximum_Credit_score)

'''----------Income Category--High → income > 50000--Medium → income 30000–50000---Low → <30000--------'''
Income_Category=np.where(Income_Replace>=50000,"High",
                         np.where(Income_Replace>=3000,"Medium","Low"))

print("Income Category :",Income_Category)

'''----Loan Risk Flag---High Risk → loan > 20000 Else Low Risk---'''

Loan_Risk=np.where(loan>20000,"High Risk","Low Risk")

print("Loan Risk Catagory :",Loan_Risk)

'''-----Credit Score Status----Excellent → >750---Good → 650 to 750-----Poor → <650-----'''

Credit_Score_Status=np.where(credit>750,"Excellent",
                             np.where(credit>650,"Good","Poor"))
print("Credit Score Status Is :",Credit_Score_Status)

'''Multiple Conditions
✅ Q7: Premium Customers
Condition:
income > 50000 AND spending_score > 70
✅ Q8: Risky Customers
Condition:
credit_score < 650 OR loan_amount > 25000
✅ Q9: Smart Customers (Important 🔥)
Condition:
High income & Low loan & High credit'''

Premium_Customers=(Income_Replace>50000) & (spending>70)
Risky_Customer=(credit<650) | (loan>25000)

Smart_Customer =(Income_Replace>np.mean(Income_Replace)) & \
                        (loan<np.mean(loan)) & \
                        (credit>np.mean(credit))

print(Smart_Customer)

multiple_condition=np.where(Premium_Customers,"Premium Customers",
                            np.where(Risky_Customer,"Risky Customers",
                                     np.where(Smart_Customer,"Smart Customer","Normal")))
print(multiple_condition)

'''----Separate Debit & Credit----total debit amount----total credit amount'''

Debit_transactions=(Tnx_type=="debit")
print(txn_type[Debit_transactions])

Debit_Amount=amount[Debit_transactions]
Total_Debit_Amount=np.sum(Debit_Amount)
print("Total Debit Amount Is :",Total_Debit_Amount)

Credit_Transactions=(Tnx_type=="credit")
print(txn_type[Credit_Transactions])

Credit_amount=amount[Credit_Transactions]
Total_Credit_Amount=np.sum(Credit_amount)
print("Total Credit Amount Is :",Total_Credit_Amount)


'''----Net Balance Per Customer---Logic:credit - debit-----'''

unique_ids=np.unique(customer_id)
Net_Balance_Per_Customer=[]
for id in unique_ids:
    find=customer_id==id

    credits=np.sum(amount[(Tnx_type=="credit") & find])

    debits=np.sum(amount[(Tnx_type=="debit") & find])

    Net_Balance_Per_Customer.append(credits-debits)

Net_Balance_Per_Customer=np.array(Net_Balance_Per_Customer)
print(Net_Balance_Per_Customer)

for cid, balance in zip(unique_ids, Net_Balance_Per_Customer):
    print(cid, balance)
