import os
import sys

def main():
        lines=[]
        numofline=0
        fname=""
        #print(len(sys.argv))
        if (len(sys.argv) == 2):
                numofline=10
                fname=sys.argv[1]
        elif len(sys.argv) == 4:
                #print(sys.argv[2])
                if (sys.argv[1]=="-n"):
                        numofline=int(sys.argv[2])
                        #print(type(numofline))
                        fname=sys.argv[3]
                        #print(fname," ",sys.argv[3])
        else:
                print("wrong format")
                sys.exit()
        # for arg in sys.argv[1]:
        #       print(arg)
        #print(fname)
        if (os.path.isfile(fname)==False):
                print("file is incorrect")
                sys.exit()

        fp = open(fname,'r')
        line = fp.readline()
        while (line):
                #print(line)
                if(len(lines)==numofline):
                        lines.pop(0)
                lines.append(line.strip())
                line = fp.readline()
        fp.close()

        for i in lines:
                print(i)





if __name__ == "__main__":
        main()