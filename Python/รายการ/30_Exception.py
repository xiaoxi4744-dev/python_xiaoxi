#Exception คือ ข้อผิดพลาดที่เกิดขึ้นระหว่างที่โปรแกรมกำลังรัน
try:
    number1 =int(input("enter number : "))
    number2 =int(input("enter number : "))
    if number1 < 0 or number2 < 0:
        raise Exception("ข้อมูลต้องเป็นค่าบวก")
    result = number1/number2
    print(result)
except ValueError:
    print("กรูณากรอกแค่ตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("หาร 0 ไม่ได้ ")
finally:
    print("----------------")
    print("End")