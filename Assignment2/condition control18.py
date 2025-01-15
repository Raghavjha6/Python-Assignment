'''Q. An Insurance company follows following rules to calculate premium.
• If a person’s health is excellent and the person is between 25 and 35 years of age and lives in 
a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot 
exceed Rs. 2 lakhs.
• If a person satisfies all the above conditions except that the sex is female then the premium is 
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
• If a person’s health is poor and the person is between 25 and 35 years of age and lives in a 
village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 
10,000.
• In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and 
maximum amount for which he/she can be insured.'''

health = input("Enter the person's health (excellent/poor): ").lower()
age = int(input("Enter the person's age: "))
location = input("Enter the person's location (city/village): ").lower()
sex = input("Enter the person's sex (male/female): ").lower()
if health == "excellent" and 25 < age < 35 and location == "city" and sex == "male":
    premium = 4 
    policy_amount = 200000  
    print("Insured with a premium rate of Rs ",premium," per thousand.")
    print("Maximum amount for which he can be insured is Rs ",policy_amount)
    
elif health == "excellent" and 25 < age < 35 and location == "city" and sex == "female":
    premium = 3  
    policy_amount = 100000  
    print("Insured with a premium rate of Rs ",premium," per thousand.")
    print("Maximum amount for which she can be insured is Rs ",policy_amount)
    
elif health == "poor" and 25 < age < 35 and location == "village" and sex == "male":
    premium = 6  
    policy_amount = 10000  
    print("Insured with a premium rate of Rs ",premium,"per thousand.")
    print("Maximum amount for which he can be insured is Rs ",policy_amount)
    
else:
    print("The person is not insured.")
