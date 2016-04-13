from sys import argv


def get_sales_report(filename):
    """Generates sales report with salesperson name and melons sold and prints to console.
        Takes the name of a file as a string, returns None.

        >>>get_sales_report('sales-report.txt')
        Anna Parker sold 13 melons.
        Janice West sold 13 melons.
        None
    """
    # Key is salesperson name, Value is number of melons sold
    sales_report = {}
    # open up file and split each line into a separate entry
    with open(filename) as input_file:
        for line in input_file:
            # clean up any whitespace
            line = line.rstrip()
            # entries is a list of each clean line, so one per salesperson info
            entries = line.split("|")
            salesperson = entries[0]
            # change melons sold from string to int in case of math
            melons = int(entries[2])
            # check to see if the salesperson's name is already a key
            if salesperson in sales_report:
                # add to their sold melon total
                sales_report[salesperson] += melons
            else:
                # create a new element in the dict
                sales_report[salesperson] = melons

    for sales_record in sales_report:
        print "{} sold {} melons.".format(sales_record, sales_report[salesperson])

# take the text file name entered as the second command line argument
sales_file = argv[1]
# call the get_sales_report function using the second command line argument as the function argument.
get_sales_report(sales_file)
