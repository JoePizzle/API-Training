#!/userbin/python3

def main():
    ##Create an empty list
    emptylist = []

    emptylist.extend("192.168.12.55")

    print(emptylist)

    myotherlist = []

    myotherlist.append("192.168.102.55")

    print(myotherlist)

    networklist = ["cisco", "junier"]
    emptylist.extend(networklist)
    print(emptylist)



if __name__== "__main__":
    main()
