def read_file(input_file_name):
    in_handle = open(input_file_name, 'r')
    lines = in_handle.readlines()
    in_handle.close()
    return lines

def exercise1(lines, output_file_name):
    # open the file for writing
    out_handle = open(output_file_name, 'w')
    # for line in lines:
    #     write the line to the file
    for line in lines:
        out_handle.write(line)
    # close the output file
    out_handle.close()
    return

def exercise2(lines, output_file_name):
    # Instead of just writing the line,
    #  - strip the trailing '\n' : line = line.rstrip('\n\r')
    #  - split it: fields = line.split(',')
    #  - for field in fields:
    #  -    write the field, plus a comma
    #  - write a '\n'

    out_handle = open(output_file_name, 'w')
    for line in lines:
        line = line.rstrip('\n\r')
        fields = line.split(',')
        for field in fields:
            out_handle.write(field + ',')
            out_handle.write('\n')
    out_handle.close()
    return

def exercise3(lines, output_file_name):
    # - first, write a new header line
    # - for line in lines[1:]:    (don't process the header line)
    # -  process each field as in exercise 2
    out_handle = open(output_file_name, 'w')
    out_handle.write('Year,Balance,Explanation\n')
    for line in lines[1:]:
        fields = line.split(',')
    for line in lines:
        line = line.rstrip('\n\r')
        fields = line.split(',')
        for field in fields:
            out_handle.write(field + ',')
            out_handle.write('\n')
    out_handle.close()
    return

def exercise4(lines, output_file_name):
    # - replace
    #      fields = line.split(',')
    #   with
    #      (year, balance, explanation) = line.split(',')
    # - convert year into an int
    # - convert balance into a float
    # - write each field separately:
    #      out_handle.write(year + ',')
    #      out_handle.write(balance + ',')
    #      out_handle.write(explanation + ',')
    # - and don't forget to write('\n')
    out_handle = open(output_file_name, 'w')
    out_handle.write('Year,Balance,Explanation\n')
    for line in lines[1:]:
        (year, balance, explanation) = line.split(',')
        year = int(year)
        balance = float(balance)
    for line in lines:
        line = line.rstrip('\n\r')
        fields = line.split(',')
        out_handle.write(str(year) + ',')
        out_handle.write(str(balance) + ',')
        out_handle.write(explanation + ',')
    out_handle.close()
    return

def exercise5(lines, output_file_name):
    # - before the "for line in" loop, initialize prev_balance = 0
    # - also, change the header line: 'Year,Balance,Income,Explanation'
    # - in the loop, compute income as balance - prev_balance
    # - and write() the income as the THIRD output field (before explanation).
    out_handle = open(output_file_name, 'w')
    out_handle.write('Year,Balance,Income,Explanation\n')
    prev_balance = 0
    for line in lines[1:]:
        (year, balance, explanation) = line.split(',')
        year = int(year)
        balance = float(balance)
        income = balance - prev_balance
        prev_balance = balance
    for line in lines:
        line = line.rstrip('\n\r')
        fields = line.split(',')
        out_handle.write(str(year) + ',')
        out_handle.write(str(balance) + ',')
        out_handle.write(str(income) + ',')
        out_handle.write(explanation + ',')
    out_handle.close()
    return

def main():
    lines = read_file('growth.txt')

    exercise1(lines, 'money1.txt')
    exercise2(lines, 'money2.txt')
    exercise3(lines, 'money3.txt')
    exercise4(lines, 'money4.txt')
    exercise5(lines, 'money5.txt')

if __name__ == '__main__':
    main()

#RS
