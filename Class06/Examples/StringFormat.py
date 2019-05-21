s1 = "My name is {0}!".format("Dr. Smith")
print(s1)

name = "Bob"
age = 14
s2 = "I am {1} and I am {0} years old.".format(age, name)
print(s2)

n1 = 4
n2 = 5
s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
print(s3)

c1 = "United States"
c2 = "China"
c3 = "Germany"
c4 = "United Kingdom"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("|{0:<18}|{1:^18}|{2:>18}|{3}|".format(c1,c2,c3,c4))