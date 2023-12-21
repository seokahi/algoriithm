n,m=map(int,input().split())
x,y,direction =map(int,input().split())
d=[[0]*m for _ in range(1,n+1)]
d[x][y] = 1
dx =[-1,0,1,0]
dy = [0,-1,0,1]
arr=[list(map(int,input().split())) for _ in range(n)]
def left_turn():
   global direction
   direction += 1
   if(direction == 4):
      direction = 0
count = 1
turn_time = 0
while 1:
   left_turn()
   nx = x+dx[direction]
   ny = y+dy[direction]
   if(d[nx][ny] == 0 and arr[nx][ny]==0):
      x,y=nx,ny
      d[x][y] = 1
      turn_time = 0
      count +=1
   else:
      turn_time += 1
   if(turn_time ==4):
      nx = x-dx[direction]
      ny = y-dy[direction]
      if(arr[nx][ny] ==0):
         x,y=nx,ny 
      else:
         break
      turn_time = 0

print(count)