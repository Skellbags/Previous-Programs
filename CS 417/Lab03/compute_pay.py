import sys
payroll = open('payroll.txt','w')
# ITEM 6 follows this line
# ITEM 9 follows this line

timesheet = open('timesheet.txt', 'r')

#ITEM 12 follows this line

while True:
    line = timesheet.readline().rstrip("\n\r")
    if len(line) == 0:
        break
# ITEM 1 follows this line
    fields = line.split(":")
    

# ITEMS 2, 3 follow this line

# ITEMS 4, 5 follow this line
    hours_worked = 0
    hourly_pay = 0
    last_name = fields[0]
    first_name = fields[1]
    TAX_RATE = 0.20
    try:
        hours_worked = float(fields[2])
        hourly_pay = float(fields[3])
    except ValueError:
        sys.stderr.write("Bad number in timesheet.txt." + line + "\n")
# ITEM 7 follows this line
    
    total = 0
    hours_x = 0
    hours_over_x = 0    
    if hours_worked > 40:
        total = ((hours_worked) * hourly_pay) + ((hours_worked-40) * (hourly_pay * 1.5))
    else:
        total = ((hours_worked) * hourly_pay)
    gross_pay = total
# ITEM 8 follows this line
    tax = gross_pay * TAX_RATE
    net_pay = gross_pay - tax
    payroll.write("{}:{}:{}:{}:{}\n".format(last_name, first_name, gross_pay, tax, net_pay))
# ITEMS 10, 11, 12, 13 follow this line

timesheet.close()

# ITEM 14 follows this line
