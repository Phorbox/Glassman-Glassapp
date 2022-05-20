TIN_Regex = ['\d+']
Right_Regex = ['rightside','right','rt','r','rv','passengerside','passside','passenger','pass']
Left_Regex = ['leftside','left','lt','l','lv','driver','driverside']
Both_Regex = ['l+r','l&r','lr','l + r','l & r']
Windshield_Regex = ['ws','w/s','windshield','wind','lt','rt']
Vent_Regex = ['vent','v','side glass']
Door_Regex = ['door','rd','ld','window']
Rubber_Regex = ['rub','rubber','seal']
Bonded_Regex = ['bond','bonded','glue']

def Make_Regex(List):
    Temp_Ex = r""
    for each in List:
        Temp_Ex = Temp_Ex + "\\b" + each +'\\b|'
    return Temp_Ex[:-1]

TIN = Make_Regex(TIN_Regex)
RIGHT = Make_Regex(Right_Regex)
LEFT = Make_Regex(Left_Regex)
BOTH = Make_Regex(Both_Regex)
WINDSHIELD = Make_Regex(Windshield_Regex)
VENT = Make_Regex(Vent_Regex)
DOOR = Make_Regex(Door_Regex)
RUBBER = Make_Regex(Rubber_Regex)
BONDED = Make_Regex(Bonded_Regex)