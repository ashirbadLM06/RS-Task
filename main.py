from line_follower_robot import component_details, robot_action
sensors = input("Enter 6-bit sensor data: ")
print(" Active Component:",component_details(sensors))
print(robot_action(sensors))
