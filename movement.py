def robot_action(sensors):
    if sensors == "001100":
        print("Robot Action: Move Forward")
    elif sensors in ["011000", "010000"]:
        print("Robot Action: Turn Left")
    elif sensors in ["000110", "000010"]:
        return"Robot Action: Turn Right"
    elif sensors == "000000":
        print("Robot Action: Stop the Robot.")
    elif sensors =="111111":
        print("Robot Action: Junction Detected.")    
    else:
         print("Invaild Input.")
    return 
    
