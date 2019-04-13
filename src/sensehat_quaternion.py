#!/usr/bin/env python

class Quaternion:

    def __init__(self, quaternion_w, quaternion_x, quaternion_y, quaternion_z):
        self.quaternion_w = quaternion_w
        self.quaternion_x = quaternion_x
        self.quaternion_y = quaternion_y
        self.quaternion_z = quaternion_z

    def log_orientation(self):
        print("w: {0}, x: {1}, y: {2}, z: {3}".format(self.quaternion_w, self.quaternion_x, self.quaternion_y, self.quaternion_z))
