#!/usr/bin/env python
# ^_^ coding=utf-8 ^_^
#
import numpy as np
import math
import matplotlib.pyplot as plt
# scipy 
#import seaborn as sns

import tf
import copy
from geometry_msgs.msg import Pose
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from planning_msgs.msg import ADCTrajectory

# set seaborn plot style
#sns.set_style()

hxmsf = np.array([[],[],[],[],[],[]])         #history position data
hxgnss = np.array([[],[],[],[],[],[]])
hxafusn = np.array([[],[],[],[],[],[]])
hxlo = np.array([[],[],[],[],[],[]])
planpoint = np.array([[],[]])
gnss_time =  0.0
msf_time =  0.0
msfPmartix = np.eye(6)          #covariance martix of msf
locFlag = 0

#取/msf_core/pose
#convariance:(x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
def MsfCallBack(msf_pose):
    global msf_time, msfPmartix, hxmsf, locFlag
    time_msf = msf_pose.header.stamp
    msfP = np.array([[msf_pose.pose.pose.position.x], [msf_pose.pose.pose.position.y], [msf_pose.pose.pose.position.z]])
    msfQ = np.array(tf.transformations.euler_from_quaternion([msf_pose.pose.pose.orientation.x,
                                                    msf_pose.pose.pose.orientation.y, 
                                                    msf_pose.pose.pose.orientation.z,
                                                    msf_pose.pose.pose.orientation.w])).reshape((3,1))   
    msfPmartix = np.array(msf_pose.pose.covariance).reshape(6,6)
    if msfP.any()!=0 or msfQ.any()!=0:
        locFlag = 1
    if locFlag == 1:
        hxmsf = np.hstack((hxmsf, np.vstack((msfP, msfQ))))
    
  
def GnssCallBack(gnss_pose):
    global gnss_time, hxgnss, locFlag
 # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    gnssP = np.array([[gnss_pose.pose.position.x], [gnss_pose.pose.position.y], [gnss_pose.pose.position.z]])
    gnssQ = np.array(tf.transformations.euler_from_quaternion([gnss_pose.pose.orientation.x,
                                                    gnss_pose.pose.orientation.y, 
                                                    gnss_pose.pose.orientation.z,
                                                    gnss_pose.pose.orientation.w])).reshape((3,1))
    if gnssP.any()!=0 or gnssQ.any()!=0:
        locFlag = 1
    if locFlag == 1:
        hxgnss = np.hstack((hxgnss, np.vstack((gnssP, gnssQ))))


def AfusnCallBack(gnss_pose):
    global hxafusn, locFlag
 # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    afusP = np.array([[gnss_pose.pose.position.x], [gnss_pose.pose.position.y], [gnss_pose.pose.position.z]])
    afusQ = np.array(tf.transformations.euler_from_quaternion([gnss_pose.pose.orientation.x,
                                                    gnss_pose.pose.orientation.y, 
                                                    gnss_pose.pose.orientation.z,
                                                    gnss_pose.pose.orientation.w])).reshape((3,1))
    if afusP.any()!=0 or afusQ.any()!=0:
        locFlag = 1
    if locFlag == 1:
        hxafusn = np.hstack((hxafusn, np.vstack((afusP, afusQ))))


def  LoCallBack(lo_pose):
    global hxlo, locFlag
    loP = np.array([[lo_pose.pose.pose.position.x], [lo_pose.pose.pose.position.y], [lo_pose.pose.pose.position.z]])
    loQ = np.array(tf.transformations.euler_from_quaternion([lo_pose.pose.pose.orientation.x,
                                                    lo_pose.pose.pose.orientation.y, 
                                                    lo_pose.pose.pose.orientation.z,
                                                    lo_pose.pose.pose.orientation.w])).reshape((3,1))
    if loP.any()!=0 or loQ.any()!=0:
        locFlag = 1
    if locFlag == 1:
        hxlo = np.hstack((hxlo, np.vstack((loP, loQ))))
   

def PlanCallBack(plan):
    global planpoint
    planpoint = np.array([[],[]])
    path_point = np.array(plan.path_point)
    for i in np.arange(0, 9):
        planpoint = np.hstack((planpoint, np.array([[path_point[i].x], [path_point[i].y]])))
    for i in np.arange(9, path_point.shape[0],10):
        planpoint = np.hstack((planpoint, np.array([[path_point[i].x], [path_point[i].y]])))


def plot_covariance_ellipse(PX, PY, RXYmartix, Yaw, RYaw):
    '''
    plot covariance ellipse and yaw arrow
    '''
    eigval, eigvec = np.linalg.eig(RXYmartix)

    if eigval[0] >= eigval[1]:
        bigind = 0
        smallind = 1
    else:
        bigind = 1
        smallind = 0

    t = np.arange(0, 2 * math.pi + 0.1, 0.1)
    a = math.sqrt(eigval[bigind]) #long axis
    b = math.sqrt(eigval[smallind]) # short axis
    x = [a * math.cos(it) for it in t]
    y = [b * math.sin(it) for it in t]
    angle = math.atan2(eigvec[bigind, 1], eigvec[bigind, 0])
    R = np.matrix([[math.cos(angle), math.sin(angle)],
                   [-math.sin(angle), math.cos(angle)]])
    fx = R * np.matrix([x, y])
    px = np.array(fx[0, :] + PX).flatten()
    py = np.array(fx[1, :] + PY).flatten()
    plt.plot(px, py, "--r")

    #TODO(lujie.di):rarrow , rarrow_cov
    Yawbias =  0 
    arrowxy = np.array([[PX, PY], [abs(a)*math.cos(Yaw+Yawbias), abs(a)*math.sin(Yaw+Yawbias)]])
    plt.arrow(arrowxy[0][0], arrowxy[0][1], arrowxy[1][0], arrowxy[1][1], length_includes_head=True, head_width=0.7*abs(a), head_length=abs(a), alpha = RYaw*100)
    plt.text(PX+abs(a), PY+abs(a), str(round(Yaw*57.3,1)))




def main():
    global hxmsf, hxgnss, hxafusn, hxlo, planpoint, gnss_time, msf_time, msfPmartix, locFlag
    rospy.init_node('plot_covariance_ellipse', anonymous=True)
    mode = rospy.get_param("~mode",1)

    #global
    if( mode == 1 or mode == 2):

        rospy.Subscriber("/changed_msf", PoseWithCovarianceStamped, MsfCallBack)#msf_core/pose, changed_msf
        rospy.Subscriber("/global_vehicle", Odometry, LoCallBack)
        rospy.Subscriber("/zibet/sensor/gnss/init", PoseStamped, GnssCallBack)#/zibet/sensor/gnss/init, init_noise_gnss
        rospy.Subscriber("/AftMsfFusn", PoseStamped, AfusnCallBack)#/zibet/sensor/gnss/init
        rospy.Subscriber("/zibet/planning", ADCTrajectory, PlanCallBack)#/zibet/sensor/gnss/init
      
    #local
    elif( mode == 0):
        rospy.Subscriber("/msf_core/pose", PoseWithCovarianceStamped, MsfCallBack)
        rospy.Subscriber("/global_vehicle", Odometry, LoCallBack)
        # rospy.Subscriber("/changed_gnss", PoseStamped, GnssCallBack)#/zibet/sensor/gnss/init, init_noise_gnss
        rospy.Subscriber("/AftMsfFusn", PoseStamped, AfusnCallBack)#/zibet/sensor/gnss/init
        rospy.Subscriber("/zibet/planning", ADCTrajectory, PlanCallBack)
    # rospy.Subscriber("/changed_noise_gnss", PoseStamped, GnssCallBack)

    #track
    track_url = rospy.get_param("~track_dir", r'/home/lujiedi/zibet_baseline/data/map/try/')
    #track = np.loadtxt(track_url + r'XiXiStr0924mid_ori.txt')
    #plan_track = np.loadtxt(track_url + r'XiXiStr0924mid.txt')
    # plan_track = np.loadtxt(track_url + r'XiXiStr0926.txt')

    plan_track = np.loadtxt(track_url + r'XiXiSLAM0928.txt')
    
    ### plot global and local
    plt.figure(num='global and local', figsize=(20,10)) 
    plt.subplot(121)
    plt.plot(plan_track[:,0], plan_track[:,1], label='plan_track')
    plt.axis('equal')        
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Global')
    plt.grid(True)
    plt.subplot(122)
    plt.plot(plan_track[:,0], plan_track[:,1], label='plan_track')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Local')
    plt.grid(True)
    plt.tight_layout()
    
    
    while not rospy.is_shutdown():
        if locFlag==0:
            plt.pause(0.0001)
            continue
        
        ### plot global and local
        plt.subplot(121)
        plt.cla()
        plt.plot(plan_track[:,0], plan_track[:,1], label='plan_track')
        #plt.plot(hxmsf[0, 1:], hxmsf[1, 1:], markersize=2, marker='*', markerfacecolor='lawngreen', label= "msf:lo+imu")
        if( mode == 1 or mode == 2):
            plt.plot(hxgnss[0, :], hxgnss[1, :], markersize=2, marker='o', markerfacecolor='red', label= "gnss")#, label= "gnss"
        plt.plot(hxafusn[0, :], hxafusn[1, :], markersize=2, marker='o', markerfacecolor='blue', label= "afusn")#, label= "gnss"
        plt.plot(hxlo[0, :], hxlo[1, :], markersize=2, marker='d', markerfacecolor='yellow', label= "lo")
        plt.scatter(planpoint[0], planpoint[1], label = 'planpoint')
        # plot_covariance_ellipse(hxmsf[0,-1], hxmsf[1,-1], msfPmartix[:2,:2]*400000, hxmsf[5,-1], msfPmartix[5,5]*10000)
        # plt.axis([-95, 95, -50, 210], 'equal')
        plt.legend()
        plt.grid(True)
        plt.title('Global')
        plt.subplot(122)
        plt.cla()
        plt.plot(plan_track[:,0], plan_track[:,1], label='plan_track')
        #plt.plot(hxmsf[0, 1:], hxmsf[1, 1:], markersize=2, marker='*', markerfacecolor='lawngreen', label= "msf:lo+imu")
        if( mode == 1 or mode == 2):
            plt.plot(hxgnss[0, :], hxgnss[1, :], markersize=2, marker='o', markerfacecolor='red', label= "gnss")#, label= "gnss"
        plt.plot(hxafusn[0, :], hxafusn[1, :], markersize=2, marker='o', markerfacecolor='blue', label= "afusn")#, label= "gnss"
        plt.plot(hxlo[0, :], hxlo[1, :], markersize=2, marker='d', markerfacecolor='yellow', label= "lo")
        plt.scatter(planpoint[0], planpoint[1], label = 'planpoint')
        #plot_covariance_ellipse(hxmsf[0,-1], hxmsf[1,-1], msfPmartix[:2,:2]*1000, hxmsf[5,-1], msfPmartix[5,5]*10000)
        #plt.axis([hxmsf[0,-1]-15, hxmsf[0,-1]+15, hxmsf[1,-1]-15, hxmsf[1,-1]+15], 'equal')
        #plt.axis([hxgnss[0,-1]-15, hxgnss[0,-1]+15, hxgnss[1,-1]-15, hxgnss[1,-1]+15], 'equal')
        plt.axis([hxafusn[0,-1]-3, hxafusn[0,-1]+3, hxafusn[1,-1]-3, hxafusn[1,-1]+3], 'equal')
        plt.legend()
        plt.grid(True)
        plt.title('Local')

        locFlag = 0
        plt.pause(0.00001)
        
        # rate.sleep()

    rospy.spin()




if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

