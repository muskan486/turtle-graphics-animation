import turtle

turtle.bgcolor('black')
t=turtle.Turtle()
from random import randint

width=5
height=7

dot_distance=25
t.penup()
list=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

t.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    c=randint(0,10)
    t.color(list[c])
    while(k<m and l<n):
        if(f==1):
            t.right(90)
        
        for i in range(l,n):
            #print(a[k][i],end=" ")
            t.dot()
            t.forward(dot_distance)
        k=k+1
        f=1
        
        
        t.right(90)
        c=randint(0,10)
        t.color(list[c])
        for i in range(k,m):
           # print(a[i][n-1],end=" ")
           t.dot()
           t.forward(dot_distance)
        n=n-1
        t.right(90)
        c=randint(0,10)
        t.color(list[c])
        
        
        if(k<m):
            for i in range(n-1,l-1,-1):
                #print(a[m-1][i],end=" ")
                t.dot()
                t.forward(dot_distance)
            m=m-1
        t.right(90)
        c=randint(0,10)
        t.color(list[c])
        
            
        if(l<n):
            for i in range(m-1,k-1,-1):
                t.dot()
                t.forward(dot_distance)
                #print(a[i][l],end=" ")
            l=l+1
            
            



spiral(20,20) 
turtle.done()   