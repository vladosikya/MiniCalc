deflt = "| |               0 | |"

def numbers_art(a, b, operation, res):
    new = f"{a} {operation} {b} = {res}"
    cnt = 0
    for x in new:
        cnt+=1
    if cnt < 16:
        er = 16 - cnt
        new_line = "| |" + er * " " + new + " | |"
    else:
        cnt = 0
        res = round(res, 4)
        res_str = str(res)
        print(res_str)
        for x in res_str:
            cnt +=1
        if cnt > 7:
            new_line = "| |  Too big number | |"
        else:
            er = 7 - cnt
            new_line = "| |" + er * " " + " Result: " + res_str + " | |"


    return  f'''
     _____________________
    |  _________________  |
    {new_line}
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    '''

logo = ''' 
 _____________________
|  _________________  |
| |               0 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

