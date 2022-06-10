def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_quoted(s):
    return (s[0] == '\"' and s[len(s)-1] == '\"')

class CSVUnQuotePlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')
        print(filename)

    def run(self):
        pass

    def output(self, filename):
        outfile = open(filename, 'w')

        for line in self.infile:
            contents = line.strip().split(',')
            for i in range(len(contents)):
                if (contents[i] == '\"\"'):
                    contents[i] = 'ID'
                elif (contents[i][0] == '\"' and contents[i][len(contents[i])-1] == '\"'):
                    contents[i] = contents[i][1:len(contents[i])-1]
                outfile.write(contents[i])
                if (i != len(contents)-1):
                    outfile.write(',')
                else:
                    outfile.write('\n')
        # Old version, just quoted header and first column
        # New version above more flexible, checks if quoted already and if number
        #firstline = self.infile.readline()
        #contents = firstline.strip().split(',')
        #outfile.write(contents[0])
        #outfile.write(',')
        #for i in range(1, len(contents)):
        #    outfile.write("\""+contents[i]+"\"")
        #    if (i != len(contents)-1):
        #        outfile.write(',')
        #    else:
        #        outfile.write('\n')
        #
        #for line in self.infile:
        #    outline = "\"" + line[:line.find(',')] + "\"" + line[line.find(','):]
        #    outfile.write(outline)

