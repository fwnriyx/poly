import sys
auth=[]
resp = input("Enter y to clear database: ")
if resp is 'y':
    print("Clearing database...")
    f=open("authlist.txt","r+")
    auth=f.read() #read list of UID's
    num=auth.count('\n') #count how many UID's in list
    for n in range(0, num): #print "Deleted entry #1.. etc
        print("Deleted entry #", n)
    f=open("authlist.txt", "w")
            #this recreates an empty authlist.txt file
    f.close()
    print("Database cleared.")