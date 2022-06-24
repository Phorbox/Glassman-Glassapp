import re
import regex
from pathlib import Path


# def make_job(facility, order_number):
#     order_file = open_order(facility, order_number)
#     Structo = file_to_structure(order_file)
#     write_job(facility, order_number, Structo)
#     order_file.close()


# def write_job(facility, order_number, structo):
#     pass


def open_file(facility, order_number, file_type):
    num = order_number_to_string(order_number)
    file_folder = Path(f"../{file_type}/{facility}/{facility}_{num}.txt")
    return open(file_folder, "r")


def open_order(facility, order_number):
    return open_file(facility, order_number, "Orders")


def order_number_to_string(order_number):
    return str(order_number).zfill(6)


def file_to_structure(file):
    structure = []
    for Each_line in file:
        temp_line = list(part_line(Each_line.lower()))
        structure.append(temp_line)
    print(structure)
    return structure


def part_line(line):
    truck_number = find_id_number(line)
    side = find_side(line)
    glass = find_glass(line)
    style = find_installation(line)

    return truck_number, side, glass, style


def find_id_number(line):
    temp = re.search(regex.TIN, line)
    if regex_success(temp):
        return int(temp.group())
    return -1


def regex_success(temp):
    return temp is not None


def find_side(line):
    if regex_success(left_side(line)):
        return "Left"
    if regex_success(right_side(line)):
        return "Right"
    if regex_success(both_side(line)):
        return "Both"
    return -1


def find_glass(line):
    if regex_success(wind_glass(line)):
        return "Windshield"
    if regex_success(vent_glass(line)):
        return "Vent"
    if regex_success(door_glass(line)):
        return "Door"
    return -1


def find_installation(line):
    if regex_success(bonded_style(line)):
        return "Bonded"
    if regex_success(rubber_style(line)):
        return "Rubber"
    return -1


def bonded_style(line):
    return apply_regex(regex.BONDED, line)


def rubber_style(line):
    return apply_regex(regex.RUBBER, line)


def wind_glass(line):
    return apply_regex(regex.WINDSHIELD, line)


def vent_glass(line):
    return apply_regex(regex.VENT, line)


def door_glass(line):
    return apply_regex(regex.DOOR, line)


def left_side(line):
    return apply_regex(regex.LEFT, line)


def right_side(line):
    return apply_regex(regex.RIGHT, line)


def both_side(line):
    return apply_regex(regex.BOTH, line)


def apply_regex(regexer, line):
    return re.search(regexer, line)


thing = open_order("SanAngelo", 1)
printer_structure = file_to_structure(thing)
thing.close()
