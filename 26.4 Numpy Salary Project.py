import numpy as np

emp_ids = np.array([101,102,103,104,105,106,107,108])

salary = np.array([25000, 40000, np.nan, 32000, 28000, np.nan, 50000, 27000])

experience = np.array([1, 5, 3, 4, 2, 6, 8, 2])

rating = np.array([3, 5, 4, 2, 3, 5, 4, 1])

'''Task 1: Handle Missing Salary'''
Nan_mean=np.nanmean(salary)
print("NanMean Value is :",Nan_mean)

Clean_salary=np.where(np.isnan(salary),Nan_mean,salary)
print("CLeaned Salary is :",Clean_salary)

'''Task 2: Salary Hike Based on Experience-->5 years +20%-->3 years	+10%--else	+5%'''

hike_amount=np.where(experience>5,Clean_salary*0.20,
                     np.where(experience>3,Clean_salary*0.10,Clean_salary*0.05))
print("Hike Amount Is :",hike_amount)

New_Salary=Clean_salary+hike_amount
print("Salary After Hike Is :",New_Salary)

'''Task 3: Bonus Based on Rating---5-->5000---4-->3000---3-->2000--<=2--0'''

Bonus_Amount=np.where(rating==5,5000,
                      np.where(rating==4,3000,
                      np.where(rating==3,2000,0)))
#print("Bonus Amount Is :",Bonus_Amount)

salary_after_bonus=New_Salary+Bonus_Amount

print("Salary After Bonus Is :",salary_after_bonus)

'''Task 5: Top Performers----/Highest salary employee---/Best rating employee---'''

Highest_salary_index=np.argmax(salary_after_bonus)

Highest_salary_employee=emp_ids[Highest_salary_index]

print("Highest Salary Employee Id Is :",Highest_salary_employee)

Best_rating_index=(np.argmax(rating))
Best_rating_employee=emp_ids[Best_rating_index]

print(Best_rating_index)

print("Best Rating Employee Id Is :",Best_rating_employee)

'''Task 6: Statistics---Avg---Min--Max'''

avergae_salary=np.average(salary_after_bonus)
Minimum_salary=np.min(salary_after_bonus)
Maximum_salary=np.max(salary_after_bonus)

print("Average Salary Is :",avergae_salary)
print("Minimum Salary Is :",Minimum_salary)
print("Maximum Salary Is :",Maximum_salary)

'''Task 7: Filtering--Employees earning > 40000--Employees with rating < 3'''

Earning_above_4000=emp_ids[salary_after_bonus>40000]
print("Above 40000 Earning Employee Id's :",Earning_above_4000)

Rating_above_3=emp_ids[rating<3]
print("Rating Blow 3 Employee Id's :",Rating_above_3)

'''
Count of high performers (rating ≥ 4)
Percentage of low performers (rating ≤ 2)'''

high_performace=np.where(rating>=4)
Count_of_high_performace=np.sum(rating>=4)
print("High Performers Count Is:",Count_of_high_performace)

Low_performance=np.where(rating<=2)
Count_low_Performance=np.sum(rating<=2)
print(Count_low_Performance)

rating_count=len(rating)
print(rating_count)

Low_Performance_Percentage=(Count_low_Performance/rating_count)*100
print("Percentage of low performers : {:.2f}%".format(Low_Performance_Percentage))

'''High salary + High rating employees'''

high_combo = emp_ids[(salary_after_bonus > 40000) & (rating >= 4)]
print("High Salary + High Rating Employee Id's:", high_combo)




