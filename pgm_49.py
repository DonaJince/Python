try:
    n=int(input("enter the position to be deleted:"))
    with open('filesample.txt', 'r') as fr:
        lines = fr.readlines()   # reading line by line
        p = 1                    # pointer for position
        with open('filesample.txt', 'w') as fw:  # opening in writing mode
            for line in lines:
                if p != n:                       # we want to remove 5th line
                    fw.write(line)
                p += 1
    print("Deleted")
except:
    print("Oops! something error")
finally:
    fr.close()
    fw.close()
