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


# enc : 3sji}7b3c3f93yh7db73747r__0rm5_r35fmn_u81d0_ngta{0mklobnekre
