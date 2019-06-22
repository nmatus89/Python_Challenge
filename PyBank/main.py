# Module for reading CSV files
import os
import csv

#Read file
csvpath = os.path.join('budget_data.csv')

with open(csvpath, 'r', newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None) #Remove header
    csvreader_ds = [month for month in csvreader] #Create dataset
   
    #print(months)
    
    cart = 0
    month = 0
    prev = 0
    sdif = 0
    dif = 0
    maxi = 0
    # = dif 
    for x in csvreader_ds:
       #print(x[1])
       cart = cart + int(x[1])
       month = month + 1
       dif = int(x[1]) - prev
       sdif = sdif + dif
       prev = int(x[1])
       
  
   

    print('Financial Analysis')
    print('-------------------------------------------------------------------------------------------')
    print("Total Months: " + str(month))
    print("Total:  $" + str(cart))
    print("Average change:  $"+ str(sdif))
    print(maxi)
