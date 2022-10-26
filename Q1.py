x = 0
y = 0
def robot_movement(x,y,movement): 
    for i in movement: 
        if i == 'UP':
            y = y + int(up)
        elif i == 'DOWN':
            y = y - int(down)
        elif i == 'LEFT':
            x = x - int(left)
        elif i == 'RIGHT':
            x = x + int(right)
    
    return (x,y)

def distance():

    output = robot_movement(x,y,movement)
    #print(output[0])
    final_distance = (((output[0])**2 + (output[1])**2)**(1/2))
    return int(final_distance)

up = input('up:')
down = input('down:')
left = input('left:')
right = input('right:')
movement = ['UP','DOWN','LEFT','RIGHT']
result = robot_movement(x,y,movement) 
print('Final position of robot is {}'.format(result))

f2 = distance()
print('Final Distance between the origin and the robot is: {}'.format(f2)) 
        

