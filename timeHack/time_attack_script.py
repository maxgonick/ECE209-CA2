# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password

class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
    
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)
        
        
    
    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        pass
    
    
# Write Up
# Please explain your solution