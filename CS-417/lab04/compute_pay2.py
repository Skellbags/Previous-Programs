import sys

TAX_RATE = 0.20

def safe_open(filename, mode):
    '''Tries to open the given file.
    If successful, returns the file handle.
    If not, complains and exits'''

    try:
        handle = open(filename, mode)
    except Exception as e:
        sys.stderr.write('Can\'t open ' + filename + ':' + str(e) + '\n')
        sys.exit(1)
    return handle
    

def get_hourly_rates(filename):
    # ITEM 2: read the employee file and get the hourly rates,
    # keyed by employee ID
    print(filename)
    hourly_rates = dict()

    
    
    while True:
        file = open(filename, 'r')
        line = file.readlines()
        line = filename.rstrip("\n\r")
        if len(line) == 0:
            break
        fields = line.split(":")
        employee_id = fields[0]
        rate = fields[1]
        hourly_rates[employee_id] = rate
        
    filename.close()

    return hourly_rates


def compute_pay(timesheet_filename, employee_filename, payroll_filename):
    # ITEM 1: compute_pay() has THREE arguments now:
    #         timesheet_filename, employee_filename, payroll_filename
    timesheet = safe_open(timesheet_filename, 'r')
    employee = safe_open(employee_filename, 'r')
    payroll = safe_open(payroll_filename, 'w')

    while True:
        line = timesheet.readline()
        if len(line) == 0:
            break
        fields = line.split(':')

        # ITEM 3: only fields 0 and 1 have data in the new file format
        hourly_rates = get_hourly_rates(employee_filename)
        employee_id = fields[0]
        hours_worked = fields[1]
        hourly_rate = hourly_rates[employee]
        try:
            hours_worked = float(fields[0])
            hourly_rate = float(fields[1])
        except ValueError:
            sys.stderr.write('bad number in timesheet file: ' + line)

        if hours_worked <= 40:
            regular_hours = hours_worked
            overtime_hours = 0
        else:
            regular_hours = 40
            overtime_hours = hours_worked - 40
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        gross_pay = regular_pay + overtime_pay
        tax = gross_pay * TAX_RATE
        net_pay = gross_pay - tax

        # ITEM 4: The format for the payroll file has changed too!

        payroll.write("{}:{}:{}:{}\n".format(employee,gross_pay, tax, net_pay))
    employee.close()
    timesheet.close()
    payroll.close()

def main():
    if len(sys.argv) == 4:
        timesheet_file = sys.argv[1]
        employee_file = sys.argv[2]
        payroll_file = sys.argv[3]
    else:
        timesheet_file = input("timesheet file?")
        employee_file = input("employee file?")
        payroll_file = input("payroll file?")
        
    
    compute_pay(timesheet_file, employee_file, payroll_file)

if __name__ == '__main__':
    main()
