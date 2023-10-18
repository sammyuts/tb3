import rospy 
#http://docs.ros.org/en/jade/api/rospy/html/rospy-module.html
#http://docs.ros.org/en/jade/api/rospy/html/rospy.topics.Publisher-class.html
#http://docs.ros.org/en/jade/api/rospy/html/genpy.message.Message-class.html

from geometry_msgs.msg import String, Twist, Vector3 
from geometry_msgs.msg import Twist

rate = rospy.Rate(1) #1 hz = 1 per second 

class testdrive():
  def __init__(self): #__init__ creates a new message, constructor
      rospy.init_node('testdrive' anonymous=False)
      #rospy.init_node('',anonymous=True)
      


  def close(self):
    
