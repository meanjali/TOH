def main():
    print "***Tower of Hanoi***"
    print
    n=int(raw_input("Enter number of disks"))
    print
    move_disks(n,"A","C","B")

def move_disks(n,src,dest,temp):
    if n==0:
        return
    else:
        move_disks(n-1,src,temp,dest)
        print "Move disk "+str(n)+" from "+src+" to "+dest
        move_disks(n-1,temp,dest,src)
if __name__=="__main__":
    main()