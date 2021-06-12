income = int(input('净利润:'))
bonus = 0.0
if income <= 100000:
    bonus = 0.01 * income
   
elif 100000<= income <= 200000:
    bonus = 0.02 * income
    
elif 200000 <= income <= 500000:
    bonus = 0.05* income
    
else:
    bonus = 0.1 * income
print ("the bonus is " + str(bonus))