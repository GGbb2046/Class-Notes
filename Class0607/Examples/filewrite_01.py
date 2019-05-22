
file = open("fw01_test.txt", "w") # open the file for writing - create if it doesn't exist, overwrite if it does
file.write("This is the first line")
file.close()

file = open("fw01_test.txt", "a") # open the file for writing - create if it doesn't exist, append to existing data if it does
file.write("This is the second line")
file.close()


file = open("fw01_test.txt", "a") # let's append a list of all primes from 2 to 100
primes = [x for x in range(2, 1000) if all(x % y != 0 for y in range(2, x))]
for i in primes:
    file.write(i)
file.close()

