#!/usr/bin/python
# vim: set expandtab:

import os
def get_ec2_conf():
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    return {'AWS_ACCESS_KEY_ID' : AWS_ACCESS_KEY_ID, 'AWS_SECRET_ACCESS_KEY' : AWS_SECRET_ACCESS_KEY}

def region_list():
    region_list = ['us-east-1','us-west-1','us-west-2','sa-east-1']
    #region_list = ['sa-east-1']
    return region_list
