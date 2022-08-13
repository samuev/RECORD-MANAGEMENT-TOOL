#===============================================================================================
# NAME:
# PURPOSE: THIS IS RECORD MANAGEMENT TOOL!
# DESCRIPTION:
# This Python script provide records management abilities like:
# Insert Record, Delete Record, Update Record Name, Update Record Amount, Search Record by name,
# Print Total Record Amount, Print All Record list
# USAGE:
# Run as regular py script: ./main.py
# Or Run with new record_file_list as positional arguments:  ./script_name.sh record_file_list
# The log file including all user actions and events will be created automatically
# AUTHOR: Stas Amuev
# REVIEWER:
# VERSION: 0.1
# LINK_TO_GIT:
#=================================================================================================

# import helper module
import helper


class Record:

    def __init__(self,record_dict):
        self.cd_dict = record_dict

    # Function Purpose: Insert new record to record list
    def insert_record(self):
        print("insert record")
        record_name = input("Enter record name: ")
        # call check record name function from helper module and returned True\False if name valid\invalid
        if helper.is_record_name_valid(record_name):
            if not helper.is_record_name_exist(record_name, self.cd_dict):
                print("The record Not existed: ", record_name)
                try:
                    record_amount = int(input("Enter record amount in digits: "))
                    if helper.is_record_amount_valid(record_amount):
                        print("The record amount valid: ", record_amount)
                        helper.add_new_record(record_name,record_amount,self.cd_dict) # add new record
                    else:
                        print("The record amount Invalid: ", record_amount)
                except ValueError:
                    print("Invalid Value Type - record amount must be digits") # catch exception if typed not digit value of rec.amount
            else:
                print("The record existed: ", record_name)
                temp_cd_key_list = helper.find_record_name_matches(record_name,self.cd_dict,add_as_new_record_flag = True)
                helper.select_from_matches(record_name, temp_cd_key_list,self.cd_dict)
        else:
            print("Invalid record name : ", record_name)

    # Function Purpose: Delete record from record list
    def delete_record(self):
        print("delete record")
        self.print_all()
        record_name = input("Enter record name: ")
        # call check record name function from helper module and returned True\False if name valid\invalid
        if helper.is_record_name_valid(record_name):
            if helper.is_record_name_exist(record_name, self.cd_dict):
                temp_cd_key_list = helper.find_record_name_matches(record_name, self.cd_dict, add_as_new_record_flag = False)
                helper.delete_from_matches(record_name, temp_cd_key_list, self.cd_dict)
            else:
                print("The record name Not existed: ", record_name)
        else:
            print("Invalid record name : ", record_name)

    # Function Purpose: Search record from record list
    def search_record(self):
        temp_cd_key_list = []
        print("search record")
        self.print_all()
        record_name = input("Enter record name for search: ")
        # call check record name function from helper module and returned True\False if name valid\invalid
        if helper.is_record_name_valid(record_name):
            if helper.is_record_name_exist(record_name, self.cd_dict):
                temp_cd_key_list = helper.find_record_name_matches(record_name, self.cd_dict,
                                                                   add_as_new_record_flag=False)
                return temp_cd_key_list
            else:
                print("The record name Not existed: ", record_name)
        else:
            print("Invalid record name : ", record_name)

    # Function Purpose: Update existed record name with new record name
    def update_record_name(self):
        print("update record name")
        temp_cd_key_list = self.search_record()   # call function of search_record()
        if temp_cd_key_list:
            try:
                line_number = int(input("Enter line number: "))
                if line_number > 0 and line_number <= len(temp_cd_key_list):  # check if typed line number are valid
                    cd_name = temp_cd_key_list[line_number - 1]
                    print(f"Selected record: {cd_name} for update")
                    new_record_name = input("Enter new record name: ")
                    if helper.is_record_name_valid(new_record_name):
                        if not helper.is_record_name_exist(new_record_name, self.cd_dict):
                            self.cd_dict[new_record_name] = self.cd_dict.pop(cd_name)
                            print("Replace New Record Name - Successfully!")
                        else:
                            print("This record name already existed: ", new_record_name)
                    else:
                        print("Invalid record name : ", new_record_name)
                else:
                    print("Invalid value")
            except ValueError:
                print("Invalid Value Type - record amount must be digits")  # catch exception if typed not digit value
        else:
            print()

    # Function Purpose: Update record amount to existed record
    def update_record_amount(self):
        print("update record amount")
        self.print_all()
        record_name = input("Enter record name: ")
        # call check record name function from helper module and returned True\False if name valid\invalid
        if helper.is_record_name_valid(record_name):
            if helper.is_record_name_exist(record_name, self.cd_dict):
                helper.update_record_amount(record_name,self.cd_dict)
            else:
                print("The record name Not existed: ", record_name)
        else:
            print("Invalid record name : ", record_name)

    # Function Purpose: Print total record amount
    def print_total_record_amount(self):
        self.print_all()
        print("Print total record amount:", sum(self.cd_dict.values()))

    # Function Purpose: Print all records from record list
    def print_all(self):
        print("Print all records:")
        for k, v in self.cd_dict.items():
            print(f'{k},{v}')

#================================ End Record Class =====================================


def select_case(case, Cd):

    if case == '1':
        Cd.insert_record()
    elif case == '2':
        Cd.delete_record()
    elif case == '3':
        Cd.search_record()
    elif case == '4':
        Cd.update_record_name()
    elif case == '5':
        Cd.update_record_amount()
    elif case == '6':
        Cd.print_total_record_amount()
    elif case == '7':
        Cd.print_all()
    elif case == 'q':
        return
    else:
        print("Invalid choice try again!")

def print_menu():
    menu_list = '''----------  M E N U -----------
    Press-[1]  Insert Record 
    Press-[2]  Delete Record
    Press-[3]  Search Record
    Press-[4]  Update Record Name
    Press-[5]  Update Record Amount
    Press-[6]  Print Total Record Amount
    Press-[7]  Print All Record Collections
    Press-[q]  Exit!
    '''
    print(menu_list)

###############-MAIN START HERE -##################

if __name__ == '__main__':

    key_press = " "   # initial input variable in order to enter menu while block
    record_dict = { 'pop':2, 'popsa':3, 'popbob':1, 'rock':2 } # hardcoded init record_dict
    Cd = Record(record_dict)
    while key_press not in "q":
        print_menu()
        key_press = input("Enter your choice is: ")
        print("Your choice is: ",key_press)
        select_case(key_press, Cd)
    else:
        print("Pressed Exit from program")


