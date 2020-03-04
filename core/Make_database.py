#!/usr/bin/python
# -*- coding: utf-8 -*-
from termcolor import colored
username=input(colored('Enter Username', 'grey', attrs=['underline', 'bold', 'dark'])+": ")
with open("login.txt",'w') as newfile:
    newfile.write(username)

