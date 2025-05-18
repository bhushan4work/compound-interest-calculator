# python compound interest calculator 

principle = 0 
rate = 0 
time = 0 

while principle <= 0:
     principle =  int(input("enter principle amt"))
     if principle <= 0 :
        print( " principal cant be negative  ")
  
    

while rate <= 0:
     rate =  int(input("enter interest rate "))
     if rate <= 0 :  
        print( " interest rate cant be negative or zero  ")
      


while time <= 0:
     time =  int(input("enter time in years "))
     if time <= 0 :
        print( " time cant be negative  ")  
     

total = principle * pow((1 + rate / 100) , time)

print(f" the balance after {time} years is $ {total}")