class Datammo:
    def __init__(status,ATK,MATK,DEF):
        status.ATK =ATK
        status.MATK =MATK
        status.DEF =DEF
        
    def Statshow(status):
        print("ค่าATK : {} ".format(status.ATK))
        print("ค่าMATK : {} ".format(status.MATK))
        print("ค่าDEF : {} ".format(status.DEF))
        
stus = Datammo(10,20,10)
stus.Statshow()