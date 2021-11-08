"""
连续输入
"""
while True:
    try:
        p = input().strip()
        res = 0
        if len(p) <= 4:
            res = res + 5
        elif len(p) < 8:
            res = res + 10
        else:
            res += 25
        l,u,d,o = 0,0,0,0
        for i in p:
            if i.islower():
                l += 1
            elif i.isupper():
                u += 1
            elif i.isdigit():
                d += 1
            else:
                o += 1
                
        if d == 1:
            res += 10
        elif d > 1:
            res += 20
        else:
            pass
        
        if l == 0 and u == 0:
            pass
        else:
            if min(l,u) == 0:
                res += 10
            else:
                res += 20
        
        if o == 1:
            res += 10
        elif o > 1:
            res += 25
        
        if l+u and d:
            if o:
                res += 3
                if l and u:
                    res += 2
            else:
                res += 2
        
        if res>= 90:
            print('VERY_SECURE')
        elif res >= 80:
            print('SECURE')
        elif res >= 70:
            print('VERY_STRONG')
        elif res >= 60:
            print('STRONG')
        elif res >= 50:
            print('AVERAGE')
        elif res >= 25:
            print('WEAK')
        else:
            print('VERY_WEAK')
        
    except:
        break

        

"""
def def_len(pswd):
    a =len(pswd)
    if a<=4:
        score=5
    elif a<=7:
        score=10
    else:
        score = 25
    return score

def def_lett(pswd):
    up = 0 
    low = 0
    
    for i in pswd:
            if i == i.lower():
                low += 1
            else:
                up += 1
           
    if (up==0 and low!=0) or (low==0 and up!=0) :
        score = 10 
    elif 0 < up < len(pswd) and 0 < low < len(pswd):
        score = 20
    else:
        score = 0 
    return score
def def_dec (pswd):
    dec = 0
    for i in pswd:
        if i.isdigit():
            dec += 1
    if dec == 0:
        score = 0
    elif dec == 1:
        score = 10
    else:
        score = 20
    return score
def def_sym(pswd):
    sym = 0
    for i in pswd:
        if i.isdigit():
            pass
        elif i.isalpha():
            pass
        else:
            sym += 1
    if sym == 0:
        score = 0
    elif sym == 1:
        score = 10
    else:
        score = 20
    return score
def def_bonus_and_all(pswd):

   
    lett, up, low, dec, sym = 0, 0, 0, 0, 0
    for i in pswd:
        if i.isalpha():
            lett += 1
            if i.isupper():
                up += 1
            else:
                low += 1
                pass
            pass
        elif i.isdigit():
            dec += 1
            pass
        else:
            sym += 1
            pass
    if (up!= 0 and low == 0 or up == 0 and low !=0) and dec!= 0 and sym == 0:
        bon_pts = 2
    elif (up!= 0 and low == 0 or up == 0 and low !=0) and dec!= 0 and sym != 0:
        bon_pts = 3
    elif up!= 0 and low !=0 and dec!= 0 and sym != 0:
        bon_pts = 5
    final_pts = bon_pts + def_dec(pswd)+def_len(pswd)+def_lett(pswd)+def_sym(pswd)
    return final_pts

while True:
    try:
        str_data = input().strip()
        final = def_bonus_and_all(str_data)
        if final >= 90:
             print('VERY_SECURE')
        elif 80 <= final <= 90:
             print('SECURE')
        elif 70 <= final <= 80:
             print('VERY_STRONG')
        elif 60 <= final <= 70:
             print('STRONG')
        elif 50 <= final <= 60:
             print('AVERAGE')
        elif 0 <= final <= 25:
             print('WEAk')
        else:
             print('VERY_WEAK')

    except:
        break
                
"""