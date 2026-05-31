angles=[30,-15,45,200,60,90,]
def valid_angle(angle):
    return angle>0 and angle<=180
valid_angles=list(filter(valid_angle,angles))
print("Valid Angles:",valid_angles)
def servo_command(angle):
    return angle*10
servo_commands=list(map(servo_command,valid_angles))
print("Servo Commands:",servo_commands)