#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:34:01 2019

@author: venkat
"""

import openpyxl
wb=openpyxl.load_workbook('accountmanager.xlsx')
u=input('enter the number of users')
i=0
while(i<u):
    tit=("Sheet of user"+str(i))
    wb.create_sheet(title=tit)
    wb.save('accountmanager.xlsx')
    i=i+1
ask=input("Enter the user number")
na="Sheet of user"+(ask)
sheet = wb.get_sheet_by_name(na)
name_of=input("Enter the name of the user")
sheet['A1'].value=name_of
amt=input("Enter the amt transacted")
sheet['A2'].value=amt
ticker=input("Enter the ticker transaction")
sheet['A3'].value=ticker
wb.save('accountmanager.xlsx')

#To send Email I will use yagmail instead of smtplib directly.
#yagmail is simplified way to send mail through gmail account
mail=input('Enter the email id of the person to be sent to(gmail)')
import yagmail
yag = yagmail.SMTP('venkat_test@gmail.com','xxxxx')#This is a fake account as my gmail administration is not allowing to use yagmail
contents = ["This mail has the excel sheet of account manager attached",'/home/venkat/python/accountmanager.xlsx']
yag.send(mail, 'subject', contents)

