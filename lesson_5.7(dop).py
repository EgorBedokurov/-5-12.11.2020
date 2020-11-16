from datetime import date

def ymd(y, m, d):
    try:                    # как работает эта команда?
        data=datetime.date(y,m,d)
        print("True")
    except:
        print("False")

y=int(input("enter year - "))# тут все понятно, но почему всегда - False
m=int(input("enter mounth - "))# 
d=int(input("enter day - "))# 

print(ymd(y, m, d))
