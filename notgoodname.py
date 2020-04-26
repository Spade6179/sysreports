#!/usr/bin/env python3

# r"^.*(ERROR|INFO): (.*) \((.*)\)$"
# sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
# sorted(dict.items(), key=operator.itemgetter(0))

import csv
import operator
import os
import re

def error_freqs (in_log):
    """Receives a syslog and exports errors and their occurance frequencies as a dictionary."""
    
    if type(in_log) != str or not os.path.exists(in_log):
        print("Please provide a valid file path.")
        raise(FileNotFoundError)
    
    dict = {}
    
    with open(in_log, 'r') as slog:
        for line in slog.readlines():
            match_obj = re.search(r"^.*ERROR: (.*) \(.*$", line)
            if match_obj != None:
                if match_obj[1] not in dict.keys():
                    dict[match_obj[1]] = 0
                dict[match_obj[1]] += 1
        return dict

def usage_stats (in_log):
    """Receives a syslog and exports the number of ERROR and INFO instances belonging to each user."""
    
    if type(in_log) != str or not os.path.exists(in_log):
        print("Please provide a valid file path.")
        raise(FileNotFoundError)
    
    dict = {}
    
    with open(in_log, 'r') as slog:
        for line in slog.readlines():
            match_obj = re.search(r"^.*(ERROR|INFO).*\((.*)\)$", line)
            if match_obj != None:
                if match_obj[2] == "":
                    continue
                if match_obj[2] not in dict.keys():
                    dict[match_obj[2]] = {"INFO":0,"ERROR":0}
                dict[match_obj[2]][match_obj[1]] += 1
        return dict

def ef2csv (in_log):
    """Receives a syslog and exports errors and their occurance frequencies as a CSV."""
    
    try:
        dict = error_freqs(in_log)
    except:
        return None
    
    # Convert the [unsortable] dictionary to a sorted list and add a header
    dict2list = [("Error", "Count")] + sorted(dict.items(), key = operator.itemgetter(1), reverse=True)
    
    file_path = os.path.join(os.getcwd(),"error_freqs.csv")
    
    if os.path.exists(file_path):
        if input("There is already a file at this path. Do you wish to overwrite it? (Y/N) ").lower() != "y":
            return None
    
    with open(file_path, "w") as f:
        for row in dict2list: # For each tuple in sorted list
            f.write("{}, {}\n".format(row[0], row[1])) # Write the 1st and 2nd elements and go to next row of csv
        f.close()
    
    print("Printing was successful.")
    
def us2csv (in_log):
    """Receives a syslog and exports the number of ERROR and INFO instances belonging to each user as a CSV."""
    
    try:
        dict = usage_stats(in_log)
    except:
        return None
    
    # Convert the [unsortable] dictionary to a sorted list and add a header
    dict2list = [("User", "Info", "Error")] + sorted(dict.items())
    
    file_path = os.path.join(os.getcwd(),"usage_stats.csv")
    
    if os.path.exists(file_path):
        if input("There is already a file at this path. Do you wish to overwrite it? (Y/N) ").lower() != "y":
            return None
    
    with open(file_path, "w") as f:
        for row in dict2list: # For each tuple in sorted list
            if row[0:] == ("User", "Info", "Error"):
                f.write("{}, {}, {}\n".format(dict2list[0][0], dict2list[0][1], dict2list[0][2])) # Write header
                continue
            str2temp_dict = (eval(str(row[1]))) # sorted() turns nested dictionaries into strings; we need to convert it back to access
            f.write("{}, {}, {}\n".format(row[0], str2temp_dict["INFO"], str2temp_dict["ERROR"])) # Write all three elements and go to next row of csv
        f.close()
    
    print("Printing was successful.")


def csv2html ():
    pass
    
def main():
    log = r"C:\Users\Benjamin\Documents\111 Education\888 Coursera\AUT Google IT Automation with Python Professional Certificate\222 Using Python to Interact with the Operating System\proj_ticky\syslog.txt"
    csv_path = r"C:\Users\Benjamin\Documents\111 Education\888 Coursera\AUT Google IT Automation with Python Professional Certificate\222 Using Python to Interact with the Operating System\proj_ticky\syslog.csv"
    #print(error_freqs(log))
    #print(usage_stats(log))
    #ef2csv(log)
    us2csv(log)
    return 0
    
main()