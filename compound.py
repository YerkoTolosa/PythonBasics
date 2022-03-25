print("Insert your name")
name = str(input()) 
print(' ')

print("Insert your surname")
surname =  str(input())
print(' ')

print("Insert your rut")
run = str (input())
print(' ')

print("Insert the inicial ammount")
s = int(input())
print(' ')

print("Insert the number of years")
n = int(input())
print(' ')

cliente = { "Name" : name, "Surname" : surname, "Rut": run, "Ammount" : s, "Time" : n}


print('<----------------------------------INFO---------------------------------------------------->')
print (name, surname, ',', 'Run: ', run, ', ','Inicial Ammount: ', s, ', ', 'Time: ', n ,'Years')
print('<------------------------------------------------------------------------------------------->')
print(' ')


intermediate_saving=[]
for i in range(n):
    monto_final = s * ( 1 + 1.2 / 100)**(i+1)
    interes_final = monto_final-s
    intermediate_saving.append(monto_final)
    print ('The final ammount in the year: ', i+1, 'is:', monto_final)
    print (' ')