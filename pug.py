class pugLife:

    def printPug(self):
        file1 = open('p.txt', 'r')
        Lines = file1.readlines()
        count = 0
    # Strips the newline character
        for line in Lines:
            count += 1
            print("{}".format(line.strip()))