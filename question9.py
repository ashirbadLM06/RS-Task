detections = [

{"object": "box", "confidence": 78, "mode":

"infrared", "distance": 2.5}, {"object": "human", "confidence": 95, "mode":

"camera", "distance": 1.2},

{"object": "ball", "confidence": 82, "mode":

"ultrasonic", "distance": 3.0},

{"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},

{"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}

]

Valid_detection=list(filter(lambda x:x["object"] == "human" and   x["mode"] == "camera" and  x["confidence"]>85,detections))
print("Valid Human Detections:",Valid_detection)

distance=list(map(lambda d:d["distance"],Valid_detection))
print("Distances:",distance)
def message(distance):
    for i in distance:
        if i<1.0:
            print("ALERT: Human very close!")
        else:
             print("Human detected at safe distance.") 
    return          
message(distance)       