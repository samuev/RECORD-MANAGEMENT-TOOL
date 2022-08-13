# This is - Helper functions Module
# import regular expression module
import re


# Function Purpose: check record name by regex if typed valid expected value and return True or False
# Parameters:
#           string: record_name
# Return: True or False
def is_record_name_valid (record_name):
    if re.match("^[a-zA-Z]+$", record_name):
        return True
    else:
        return False


# Function Purpose: check record name already exist
# Parameters:
#         string: record_name
#         list: cd_dict
# Return: True or False
def is_record_name_exist (record_name,cd_dict):
    for key in cd_dict.keys():
        if record_name in key:
            return True
    else:
        return False

'''
Function Purpose: check record amount if typed valid expected value and return True or False
Parameters:
         int: record_amount
Return: True or False
'''
def is_record_amount_valid (record_amount):
    if type(record_amount) == int and record_amount > 0:
        return True
    else:
        return False


'''
Function Purpose: Insert new record to record list
Parameters: 
          string: record_name
          int: record_amount 
          list: cd_dict
'''
def add_new_record (record_name,record_amount,cd_dict):
    cd_dict[record_name] = record_amount
    print("Insert New Record - Successfully!")

'''
Function Purpose: find matched record names
Parameters:
          string: record_name
          list: cd_dict
          bool: add_as_new_record_flag
Return: True or False
'''
def find_record_name_matches (record_name, cd_dict, add_as_new_record_flag):
    temp_cd_key_list = []
    print("record name matches:")
    for key in cd_dict.keys():
        if record_name in key:
            temp_cd_key_list.append(key)
    temp_cd_key_list.sort()
    if add_as_new_record_flag:
        temp_cd_key_list.append("Add as new record")

    for i,key in enumerate(temp_cd_key_list):
        print(i+1,".", key)

    return temp_cd_key_list


def update_record_amount(cd_name, cd_dict):
    try:
        record_amount = int(input("Enter record amount in digits: "))
        if is_record_amount_valid(record_amount):
            cd_dict[cd_name] += record_amount                    # update amount of existed record
            print("Update Record amount - Successfully!")
        else:
            print("The record amount Invalid: ", record_amount)
    except ValueError:
        print(
            "Invalid Value Type - record amount must be digits")  # catch exception if typed not digit value of rec.amount


def check_is_record_exist(record_name, temp_cd_key_list):
    for name in temp_cd_key_list[:-1]:
        if re.match(name, record_name):
            print("This record already existed!")
            return True

    print("This record not exist: " + record_name)
    return False


def select_from_matches(record_name, temp_cd_key_list, cd_dict):
    try:
        line_number = int(input("Enter line number: "))
        if line_number > 0 and line_number <= len(temp_cd_key_list):   # check if typed line number are valid
            cd_name = temp_cd_key_list[line_number-1]
            if cd_name == temp_cd_key_list[-1]:   # if selected Add as new record options
                if not check_is_record_exist(record_name, temp_cd_key_list):
                    try:
                        record_amount = int(input("Enter record amount in digits: "))
                        if is_record_amount_valid(record_amount):
                            add_new_record(record_name,record_amount,cd_dict)             # add as new record
                        else:
                            print("The record amount Invalid: ", record_amount)
                    except ValueError:
                        print("Invalid Value Type - record amount must be digits")  # catch exception if typed not digit value of rec.amount
            else:
                print("selected record is: ", cd_name, ":", cd_dict[cd_name])
                update_record_amount(cd_name, cd_dict)
        else:
            print("Invalid value")
    except ValueError:
        print(
            "Invalid Value Type - record amount must be digits")  # catch exception if typed not digit value


def delete_from_matches(record_name, temp_cd_key_list, cd_dict):
    try:
        line_number = int(input("Enter line number: "))
        if line_number > 0 and line_number <= len(temp_cd_key_list):   # check if typed line number are valid
            cd_name = temp_cd_key_list[line_number - 1]
            cd_dict.pop(cd_name)
            print(f"Record: {record_name} - Successfully Deleted!")
        else:
            print("Invalid line number")
    except ValueError:
        print(
            "Invalid Value Type - line number must be digits")  # catch exception if typed not a digit value


def update_from_matches(record_name, temp_cd_key_list, cd_dict):
    try:
        line_number = int(input("Enter line number: "))
        if line_number > 0 and line_number <= len(temp_cd_key_list):  # check if typed line number are valid
            cd_name = temp_cd_key_list[line_number - 1]
            cd_dict.pop(cd_name)
            print(f"Record: {record_name} - Successfully Deleted!")
        else:
            print("Invalid line number")
    except ValueError:
        print(
            "Invalid Value Type - line number must be digits")  # catch exception if typed not a digit value

