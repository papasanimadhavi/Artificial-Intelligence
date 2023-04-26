#MISSIONARIES AND CANNIBALS
def bfsmc(n,m):

    open=[]
    open.append([[n,m,1],[0,0,0]])
    close=[]
    path=[]

    while(open):
        s=open.pop()
        n1=s[0][0]
        m1=s[0][1]
        bl=s[0][2]
        n2=s[1][0]
        m2=s[1][1]
        br=s[1][2]

        path.append(s)
        if n2==n and m2==m and br==1:
            print("Moved all the missionaries and cannibals to other side")
            return path

        close.append(s)

        if(n1!=0 and n2!=0 and n1>=m1 and n2>=m2 and n1+n2==n and m1+m2==m):
            if bl==1:
                #1
                if([[n1-2,m1,0],[n2+2,m2,1]] not in close):
                  open.append([[n1-2,m1,0],[n2+2,m2,1]])
                  close.append([[n1-2,m1,0],[n2+2,m2,1]])
                #2
                if([[n1-1,m1-1,0],[n2+1,m2+1,1]] not in close):
                  open.append([[n1-1,m1-1,0],[n2+1,m2+1,1]])
                  close.append([[n1-1,m1-1,0],[n2+1,m2+1,1]])
                #3
                if([[n1,m1-2,0],[n2,m2+2,1]] not in close):
                  open.append([[n1,m1-2,0],[n2,m2+2,1]])
                  close.append([[n1,m1-2,0],[n2,m2+2,1]])
                #4
                if([[n1-1,m1,0],[n2+1,m2,1]] not in close):
                  open.append([[n1-1,m1,0],[n2+1,m2,1]])
                  close.append([[n1-1,m1,0],[n2+1,m2,1]])
                #5
                if([[n1,m1-1,0],[n2,m2+1,1]] not in close):
                  open.append([[n1,m1-1,0],[n2,m2+1,1]])
                  close.append([[n1,m1-1,0],[n2,m2+1,1]])
            elif br==1:
                #6
                if([[n1+2,m1,1],[n2-2,m2,0]] not in close):
                  open.append([[n1+2,m1,1],[n2-2,m2,0]])
                  close.append([[n1+2,m1,1],[n2-2,m2,0]])
                #7
                if([[n1+1,m1+1,1],[n2-1,m2-1,0]] not in close):
                  open.append([[n1+1,m1+1,1],[n2-1,m2-1,0]])
                  close.append([[n1+1,m1+1,1],[n2-1,m2-1,0]])
                #8
                if([[n1,m1+2,1],[n2,m2-2,0]] not in close):
                  open.append([[n1,m1+2,1],[n2,m2-2,0]])
                  close.append([[n1,m1+2,1],[n2,m2-2,0]])
                #9
                if([[n1+1,m1,1],[n2-1,m2,0]] not in close):
                  open.append([[n1+1,m1,1],[n2-1,m2,0]])
                  close.append([[n1+1,m1,1],[n2-1,m2,0]])
                #10
                if([[n1,m1+1,1],[n2,m2-1,0]] not in close):
                  open.append([[n1,m1+1,1],[n2,m2-1,0]])
                  close.append([[n1,m1+1,1],[n2,m2-1,0]])
            

    return "NONE"


n=int(input("enter no.of missionaries:"))
m=int(input("enter no.of cannibals:"))
print(bfsmc(n,m))
