TIN_Regex = ['\d+']
Right_Regex = ['rightside', 'right', 'rt', 'r', 'rv', 'passengerside', 'passside', 'passenger', 'pass']
Left_Regex = ['leftside', 'left', 'lt', 'l', 'lv', 'driver', 'driverside']
Both_Regex = ['l+r', 'l&r', 'lr', 'l + r', 'l & r']
Windshield_Regex = ['ws', 'w/s', 'windshield', 'wind', 'lt', 'rt']
Vent_Regex = ['vent', 'v', 'side glass']
Door_Regex = ['door', 'rd', 'ld', 'window']
Rubber_Regex = ['rub', 'rubber', 'seal']
Bonded_Regex = ['bond', 'bonded', 'glue']


def make_regex(List):
    Temp_Ex = r""
    for each in List:
        Temp_Ex = Temp_Ex + "\\b" + each + '\\b|'
    return Temp_Ex[:-1]


TIN = make_regex(TIN_Regex)
RIGHT = make_regex(Right_Regex)
LEFT = make_regex(Left_Regex)
BOTH = make_regex(Both_Regex)
WINDSHIELD = make_regex(Windshield_Regex)
VENT = make_regex(Vent_Regex)
DOOR = make_regex(Door_Regex)
RUBBER = make_regex(Rubber_Regex)
BONDED = make_regex(Bonded_Regex)
