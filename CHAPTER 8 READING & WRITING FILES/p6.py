#A company stores daily sales totals in sales_log.txt, one number per line.
# Write read_sales(filename) that opens the file with with 
# open() as f, reads all lines, and returns them as a list of floats.

def read_sales(filename):
    sales = []
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        number = float(line)
        sales.append(number)
    return sales

result = read_sales('sales_log.txt')
print(result)