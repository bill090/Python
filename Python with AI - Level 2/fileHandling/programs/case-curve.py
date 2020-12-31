import pandas as pd
dataset = "/home/bill/Python/Python with AI - Level 2/fileHandling/files/covid19.csv"
case_threshold = 100
def import_curve_data(province):
    start_day = ""
    curve_data = []
    province_index = 1
    date_index = 3
    numconf_index = 4
    data = open(dataset, "r")
    for aline in data:
        values = aline.split(",")
        if values[province_index] == province:
            numconf = int(values[numconf_index])
            if numconf >= case_threshold and start_day == "":
                start_day = values[date_index]
            if start_day != "":
                curve_data.append(numconf)
    data.close()
    return start_day, curve_data
def main():
    province = "Ontario"
    start_day, curve_data = import_curve_data(province)
    print(province)
    print(f"First day over 100 cases is {start_day}")
    print(len(curve_data))
main()