#!/usr/bin/python
# -*- coding: utf-8 -*-

username=input("Enter username:")
with open("login.txt",'w') as newfile:
    newfile.write(username)

