class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0





#        res = 0 
#        if -2**31<= x <= 2**31-1:
#            if x == 0:
#                return 0 
#        
#            else:
#                if x > 0:
#                    z = str(x)
#                    for i in range (len(z)):
#                        k = 10**i * int(z[i])
#                        res = k + res
#                   return res
#                else:
#                    z = str(0 - x)
#                    for i in range (len(z)):
#                        k = 10**i * int(z[i])
#                        res = k + res
#                    a = "-" + str(res)
#                    return int(a)
