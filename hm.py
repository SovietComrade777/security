"""Creating a password saver mechanism
    The Steps of it are as follows-
    <1>Creating three type of entries member,student,teacher
    <2>for any entry we will check the name but we will match the name only in student one.
    <3>we will ask for password from three where we will verify password for two one for member and one for teacher.student id is dummy now it will display a random output file page
    <4>we will ask two questions then 1>your favorite animal? 2>your money entry total?
    <5>for teacher id is dummy now and he will be diverted
    <6>now for member this time name of admin will be asked!
    <7>*All the mindmap execution will be done through file handling"""
#input of member,student,teacher role
S_name=['Aman','Aditya','Rishabh','Aadarsh','Vivek']
pswwd=open("C:\\Users\\DELL\\Desktop\\agnes\\pswd.txt","r")
p_read=pswwd.readline()
a=input("Enter Your Role .1>M)Membeer.2>S)Student>.3>T)Teacher\n")
name=input("Enter Your Name")
c=0
q=open("C:\\Users\\DELL\\Desktop\\agnes\\lol.txt",'r')
q_read=q.read()
i=open("C:\\Users\\DELL\\Desktop\\agnes\\imp.txt","r")
i_read=i.read()
ui=("C:\\Users\\DELL\\Desktop\\agnes\\dat.txt","a")
if(a=='S'):
    for i in range(0,len(S_name)):
        if(name==S_name[i]):
            print("You are selected")
            c=0
            break
        else:
            c=1
    if c==1:
        print("We are off today.Sorry for the inconvienience")
        exit
    else:
        print("Read this"+q_read)
elif a=='M'or a=='T':
    print("You're Selected")
    pswd=input("Enter password")
    for i in range(0,len(p_read)):
        if pswd==p_read[i]:
            print("Confirmed about your selection")
            q1=input("Who is your favorite animal?\n")
            if q1=="Human" or q1=="Man":
                q2=input("Who is The daddy of this system?\n")
                if q2=="Akshat":
                    if a=="T":
                        print("You Got right till here see this:",q_read)
                    elif a=="M":
                        iq=input("what we love to see in sky?\n")
                        if(iq=="Duke"):
                            print(i_read)
                            str="Name:"+name+"Position"+a
                            ui.write(str)
                        else:
                            print(q_read)
        else:
            print("Server is Busy please Try again Later")
            print(p_read)
elif a=='OTTE SIR':
    print("Welcome Akshat Bhai")