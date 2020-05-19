#SHRINIKETAN S TIKARE(19BEC041)
import pandas as pd
import csv
import random

df=pd.read_csv("G:\\phytho\\uma mam\currency.csv")#PLEASE CHANGE PATH FILE ACCORDING TO YOU AND MAKE SURE THAT U HAVE DOWNLOADED currency.csv WHICH IS BEEN UPLOADED IN THE SAME REPOSITORY

df.head()

lst={}
lst_names=[]
lst_symbols=[]

lst_symbols=list(df['Unnamed: 2'])
lst_names=list(df['Unnamed: 1'])

lst_symbols.remove('Symbol')
lst_names.remove('Name')

#     lst = {lst_names[i]: lst_symbols[i] for i in range(len(lst_symbols))}
lst=dict(zip(lst_names,lst_symbols))



def formation_of_question(no_of_question):
    file = open('solution_4_ques_bank.txt', 'a')
    file.truncate(0)
    file.close()
    for i in range(1,no_of_question+1):

        lst1=[]

        correct=random.choice(lst_names)
        lst1.append(lst[correct])

        for i1 in range(0,3):
            other_options=random.choice(lst_symbols)
            if(other_options!=correct and other_options not in lst1 ):
                lst1.append(other_options)
    
        print(f"{i}.What's the symbol for {correct}?\n a.{lst1[0]}\t b.{lst1[1]}\t c.{lst1[2]}\t d.{lst1[3]}")
        ur_answer=input("enter your choice:")
        lst2=['a','b','c','d']
        
        if ur_answer not in lst2:
            print("invalid respose...   ,, answer entered should be in [a,b,c,d] ,,run the program again")
            break
        print("\n")
        
        
        file1 = open('solution_4_ques_bank.txt', 'a')
        file1.writelines(f"{i}.What's the symbol for {correct}? : {lst[correct]}\n")
        file1.close()
        
formation_of_question(10)
