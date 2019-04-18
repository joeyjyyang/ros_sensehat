#!/usr/bin/env python

class Quaternion:

    def __init__(self, quaternion_x, quaternion_y, quaternion_z, quaternion_w):
        self.quaternion_x = quaternion_x
        self.quaternion_y = quaternion_y
        self.quaternion_z = quaternion_z
        self.quaternion_w = quaternion_w
     
    def log_orientation(self):
        print("q_x: {0}, q_y: {1}, q_z: {2}, q_w: {3}".format(self.quaternion_x, self.quaternion_y, self.quaternion_z, self.quaternion_w))
