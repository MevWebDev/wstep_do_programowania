import datetime
def Date_birth_from_pesel(pesel):
    rok=pesel[0:2]
    miesiac=pesel[3]    
    dzien=pesel[4:6]
    if pesel[2]== "2":
        a="20"
    else:
        a="19"
    MINIPESEL=a+rok+miesiac+dzien
    return MINIPESEL
x="05292406439"


def is_of_age(Mx,data2):

    rok=Mx[0:4]
    miesiac=Mx[4]    
    dzien=Mx[5:7]
    
    rok2=data2[0:4]
    miesiac2=data2[4]    
    dzien2=data2[5:7]
    x1=datetime.datetime(rok,miesiac,dzien)
    y1=datetime.datetime(rok2,miesiac2,dzien2)
    print(x,y)


y="20231111"

is_of_age(Date_birth_from_pesel(x),y)




