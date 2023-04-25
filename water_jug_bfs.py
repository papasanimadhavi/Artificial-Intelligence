#WATER JUG USING BFS
def bfs(a,b,c):
    open_list=[]
    open_list.append([0,0])
    close_list=[]
    p=[]
    while open_list:
        s=open_list.pop()
        #x=s[0]
        #y=s[1] 
        
        p.append(s)
        
        if s[0]==c:
            print("Path found")
            return p

        
        
        close_list.append(s)
        
        if s[0]<a and ([a,s[1]] not in close_list):
            open_list.append([a,s[1]])
            close_list.append([a,s[1]])
            
            
        if s[1]<b and ([s[0],b] not in close_list):
            open_list.append([s[0],b])
            close_list.append([s[0],b])
            
        if s[0]>0 and ([0,s[1]] not in close_list):
            open_list.append([0,s[1]])
            close_list.append([0,s[1]])
            
        if s[1]>0 and([s[0],0] not in close_list):
            open_list.append([s[0],0])
            close_list.append([s[0],0])
            
        if s[0]+s[1]<=a and s[1]>=0 and ([s[0]+s[1],0] not in close_list):
            open_list.append([s[0]+s[1],0])
            close_list.append([s[0]+s[1],0])
            
        if s[0]+s[1]<=b and s[0]>0 and ([0,s[0]+s[1]] not in close_list):
            open_list.append([0,s[0]+s[1]])
            close_list.append([0,s[0]+s[1]])
            
        if s[0]+s[1]>=a and s[1]>=0 and ([a,s[1]-(a-s[0])] not in close_list):
            open_list.append([a,s[1]-(a-s[0])])
            close_list.append([a,s[1]-(a-s[0])])
            
        if s[0]+s[1]>=b and s[0]>0 and ([s[0]-(b-s[1]),b] not in close_list):
            open_list.append([s[0]-(b-s[1]),b])
            close_list.append([s[0]-(b-s[1]),b])
            
    return "No path"
    

    
            
        
a=int(input("enter capacity of jug1:"))
b=int(input("enter capacity of jug2:"))
c=int(input("enter the target capacity:"))
print(bfs(a,b,c))
