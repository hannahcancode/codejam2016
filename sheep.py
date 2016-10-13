# open input and output file
I = open('A-large.in', 'r')
O = open('output.txt', 'w')

# initialise variables
string = ""
L = []
cases = 0

# deal with first line containing number of test cases
N = I.readline()

#iterate through each line
for line in I:
    cases += 1
    digits = set()  # create set to catch digits
    count = 1 # set/reset counter for each line
    line = line.rstrip('\n')
    N = int(line)
    
    # loop until every digit has been caught in set or limit is reached
    while digits != {'0','1','2','3','4','5','6','7','8','9'} and count < 500:
        number = N * count
        for char in str(number):
            digits.add(char)
        if count == 499:
            number = "INSOMNIA" #print if limit is reached
        count += 1
    O.write("Case #"+str(cases)+": "+str(number)+"\n") #write to output

# close input and output file
I.close()
O.close()
    
