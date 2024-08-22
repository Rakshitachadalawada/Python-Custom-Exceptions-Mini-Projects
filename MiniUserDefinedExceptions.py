#!/usr/bin/env python
# coding: utf-8

# # 1)Negative Age Exception

# if age<0 then raise/throw the exception
# kid:age>0 and less than 13
# Teen:age between 13 and 19
# Adult:age between 19 and 50
# Old:age greater than 50 
# 

# In[2]:


class NegativeAgeException(Exception):
    pass
def stage(age):
    if age<0:
        raise NegativeAgeException("enter valid age")
    elif age>0 and age<13:
        print("kid")
    elif age>=13 and age<=19:
        print("Teen")
    elif age>19 and age<=50:
        print("Adult")
    else:
        print("old")
          
try:
    age=int(input())
    stage(age)
except (ValueError,NegativeAgeException) as msg:
    print(msg)
    


# # 2)Account Balance Exception
# 

# Total balance is 10000.Now you need to with draw some amount so that the minimum amount should be 5000 and you cant with draw so that the minimum balance should not get decreased. if so raise account balance exception
# 

# In[13]:


balance=10000
class AccountBalanceException(Exception):
    pass
def withdraw(amt):
    global balance
    balance=balance-amt
    if balance<5000:
        raise AccountBalanceException("insufficient balance")
    else:
        print("amount with drawn successfully. to balace left=",balance)
try:
    a=int(input())
    withdraw(a)
except (ValueError,AccountBalanceException) as msg:
    print(msg)
      


# # 3)Simple Calculator

# the input should be in the for of the expression EX:5+10 if yes the evaluate and print that result

# In[8]:


class InvalidFormulaException(Exception):
    pass
def evaluate(formula):
    formula=formula.split()
    a=int(formula[0])
    b=int(formula[2])
    if formula[1]=='+':
        print(a+b)
    elif formula[1]=='-':
        print(a-b)
    elif formula[1]=='*':
        print(a*b)
    elif formula[1]=='/':
        print(a/b)
    else:
        raise InvalidFormulaException("not in given format")
try:
    s=input()
    evaluate(s)
except InvalidFormulaException as msg:
    print(msg)


# In[ ]:




