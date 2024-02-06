# -*- coding: utf-8 -*-
import subprocess
import string


class solution:
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXITED PROPERTIES
        # You can add as many properties as you need
        self.mem_ctl_exe = "./mem_ctl.exe"  # This is the path of mem_ctl.exe file
        self.pwd_checker_exe = "./mem_password_checker.exe"  # This is the path of password_checker.exe file
        self.password = ""  # This is where your guessed password is store

    def setProtectMem(self, start_index, end_index):
        # DO NOT MODIFY THIS METHOD

        # This method used to set a range of memory can not be accessed starting from start_index, ending with end_index (included).
        # After set [start_index, end_index] as can not be accessed, any read or write operations will
        # If this operation successfully executed, this method will return some output from the mem_ctl.exe
        # Otherwise, this method will return -1
        if (
            start_index <= end_index
            and start_index >= 0
            and start_index < 1024
            and end_index >= 0
            and end_index < 1024
        ):
            p1 = subprocess.Popen(
                [self.mem_ctl_exe, str(start_index), str(end_index)],
                stdout=subprocess.PIPE,
            )
            mem_ctl_exe_result = p1.communicate()[0].decode()
            return mem_ctl_exe_result
        else:
            return -1

    def checkPassword(self, password):
        # DO NOT MODIFY THIS METHOD

        # This method will pass your password to mem_password_checker.exe to verify the correctness
        # The return value is a string which is the output of mem_password_checker.exe
        # If password is correct, this method will return Correct
        # If password is wrong, this method will return Wrong
        # If mem_password_checker accessed an can not be accessed memory, this method will return SEG ERROR

        p2 = subprocess.Popen([self.pwd_checker_exe, password], stdout=subprocess.PIPE)
        pwd_checker_exe_result = p2.communicate()[0].decode()
        return pwd_checker_exe_result

    def example(self):
        # The following shows how to call a executable file in python and capture its output
        # You can modify it to test your ideas
        alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
        rightanswers = []
        i = 1 
        # You can print the output for debug or test.
        while i != -1:
            for letter in alphabet:
                mem_ctl_exe_result = self.setProtectMem(i, 1000)
                # print(mem_ctl_exe_result)
                pwd_checker_exe_result = self.checkPassword(
                    "".join(rightanswers) + letter
                )
                #If we hit a SEG ERROR 
                if pwd_checker_exe_result == "SEG ERROR":
                    i += 1
                    rightanswers.append(letter)
                    break
                #If we reach the end of the alphabet and nothing works that means we reached the end of the password
                if letter == "Z":
                    i = -1
        self.password = "".join(rightanswers)
        print(self.password)
        # print(pwd_checker_exe_result)
        # After mem_ctl.exe executed, the memory in range [start_index, end_index] will be set to can not be accessed.
        # That means, password_check.exe will not accessible this section of memory.
        # Any read or write from password_check.exe to this range will cause an "SEG ERROR"

        # You can print the output for debug or test.

        # For password_checker.exe, the password you input will be stored from the beginning of the memory.
        # Take the above parameters as input, the memory structure is shown below:

        # index:        0--------------------100----------------------------------1000----------1023
        # access type:  |-----accessible------|---------cannot be accessed----------|--accessible--|
        # value:        guess\0#####################################################################

        print(self.password)

    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # You should modify the start_index, end_index and password appropriately to achieve the attack
        # GradeScope will import your class, and call this method to get the password you calculated.
        pass


sol = solution()
sol.example()

# Write Up
# Please explain your solution
