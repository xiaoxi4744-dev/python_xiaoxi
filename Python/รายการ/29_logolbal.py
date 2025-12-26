#ขอบเขตตัวแปร
balance = 1000 #Global

def dis():
    print(f"ยอดเงินคงเหลือ {balance} บาท")

def deposit(value):
    global balance
    money = value #local
    if (money<=0):
        return print("ไม่สามารถฝากเงินได้")
    print("ฝากเงิน",money)
    balance += money

def witdraw(value):
    global balance    
    amout = value
    if amout<=0 or amout > balance:
        return print("ไม่สามารถถอนเงินได้")
    print("ถอนเงินจำนวน",amout)
    balance -=amout

dis()
witdraw(1001)
dis()