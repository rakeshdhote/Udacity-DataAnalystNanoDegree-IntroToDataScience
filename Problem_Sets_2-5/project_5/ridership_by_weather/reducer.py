import sys


def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''

    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    for line in sys.stdin:
        # your code here
        data = line.strip().split("\t")
        
        if len(data) != 2:
            continue
        else:
            this_key, count = data
            
#        if old_key and old_key != this key:
        if old_key and old_key != this_key: # new key           
            print "{0}\t{1}".format(old_key, riders/num_hours)
            num_hours = 0
            riders = 0
            
        old_key = this_key
        riders += float(count)  
        num_hours += 1
       
    if old_key != None:
        print "{0}\t{1}".format(old_key, riders/num_hours)
reducer()
