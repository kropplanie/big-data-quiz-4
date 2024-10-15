import sys, re
import random

def main(argv):
    total_words = 0
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            for word in pattern.findall(line):
                print ("LongValueSum:" + word.lower() + "\t" + "1")
                total_words += 1
                # x = 1 / random.randint(0,99)
            line = sys.stdin.readline()
    except EOFError as error:
        return None
    print(f"__TOTAL__\t{total_words}")

if __name__ == "__main__":
    main(sys.argv)
