import os
import sys

# Add the parent directory (e:\NUMPY) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can use an absolute import
from line_follower_robot.sensor import component_details
from line_follower_robot.movement import robot_action