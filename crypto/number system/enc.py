from secret import FLAG

flag = FLAG[::-1]
new_flag = ''

for i in range(0, len(flag), 5):
    new_flag += flag[i+1]
    new_flag += flag[i+3]
    new_flag += flag[i+4]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)


# enc : 3a_2}3pyhr_1_nc135_7_7_0ul4_830_fyu_n471rpm07_0t015_n1_7y553rbm3_nta{umklobneKre
