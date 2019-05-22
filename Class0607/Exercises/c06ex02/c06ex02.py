import sys

# define functions

def remove_vowels(s):
    vowels = "AaEeIiOoUu"
    ret_str = ""
    for ch in s:
        if ch not in vowels:
            ret_str += ch
    return ret_str


if len(sys.argv) != 3:
    print("Error: You must provide input and output file arguments")
else:
    with open(sys.argv[1], "r") as fin:
        input_txt = fin.read()
    with open(sys.argv[2], "w") as fout:
        fout.write(remove_vowels(input_txt))
