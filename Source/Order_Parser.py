import re
import Regex


def Make_Job(Facility, Order_Number):
    Order_File = Open_Order(Facility, Order_Number)
    Structo = File_To_Structure(Order_File)
    Write_Job(Facility, Order_Number,Structo)
    Order_File.close()

def Write_Job(Facility, Order_Number,Structo):
    
    pass

def Open_File(Facility, Order_Number,Type):
    Order_Number = Order_Number_To_String(Order_Number)
    File_Path = "{}\{}\{}_{}.txt".format(Type,Facility,Facility,Order_Number)
    return open(File_Path,"r")

def Open_Order(Facility, Order_Number):
    Order_Number = Order_Number_To_String(Order_Number)
    File_Path = "Orders\{}\{}_{}.txt".format(Facility,Facility,Order_Number)
    return open(File_Path,"r")

def Order_Number_To_String(Order_Number):
    return str(Order_Number).zfill(6)

def File_To_Structure(File):
    Structure = []
    for Each_Line in File:
        Temp_Line = list(Part_Line(Each_Line.lower()))
        Structure.append(Temp_Line)   
    print(Structure)

def Part_Line(Line):
    Truck_Number = Find_ID_Number(Line)
    Side  = Find_Side(Line)
    Glass = Find_Glass(Line)
    Style = Find_Installation(Line)

    return Truck_Number,Side,Glass,Style


def Find_ID_Number(Line): 
    Temp = re.search(Regex.TIN, Line)
    if Regex_Success(Temp):
        return int(Temp.group())
    return -1

def Regex_Success(temp):
    return temp != None

def Find_Side(Line):
    if Regex_Success(Left_Side(Line)):
        return "Left"
    if Regex_Success(Right_Side(Line)):
        return "Right"
    if Regex_Success(Both_Side(Line)):
        return "both"
    return -1

def Find_Glass(Line):
    if Regex_Success(Wind_Glass(Line)):
        return "Windshield"
    if Regex_Success(Vent_Glass(Line)):
        return "Vent"
    if Regex_Success(Door_Glass(Line)):
        return "Door"
    return -1

def Find_Installation(Line):
    if Regex_Success(Bonded_Style(Line)):
        return "Bonded"
    if Regex_Success(Rubber_Style(Line)):
        return "Rubber"
    return -1

def Bonded_Style(Line):
    return Apply_Regex(Regex.BONDED,Line)

def Rubber_Style(Line):
    return Apply_Regex(Regex.RUBBER,Line)

def Wind_Glass(Line):
    return Apply_Regex(Regex.WINDSHIELD,Line)

def Vent_Glass(Line):
    return Apply_Regex(Regex.VENT,Line)

def Door_Glass(Line):
    return Apply_Regex(Regex.DOOR,Line)

def Left_Side(Line):
    return Apply_Regex(Regex.LEFT,Line)   

def Right_Side(Line):
    return Apply_Regex(Regex.RIGHT,Line)    

def Both_Side(Line):
    return Apply_Regex(Regex.BOTH,Line)    

def Apply_Regex(Regexer,Line):
    Temp = re.search(Regexer, Line)
    return Temp


thing = Open_Order("SanAngelo",1)
Printer_Structure = File_To_Structure(thing)
thing.close()