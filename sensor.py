def component_details(sensors):    
    int_data=list(map(int,sensors))
    print("Sensor Values:",int_data)
    detected=list(filter(lambda x:x=='1',sensors))
    return len(detected) 

