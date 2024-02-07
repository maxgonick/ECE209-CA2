# -*- coding: utf-8 -*-
import subprocess


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

    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # You should modify the start_index, end_index and password appropriately to achieve the attack
        # GradeScope will import your class, and call this method to get the password you calculated.

        # All printable ASCII characters that would be inside the password
        alphabet = [chr(i) for i in range(32, 127)]
        rightanswers = []
        i = 1
        while True:
            for letter in alphabet:
                # incrementally block of memory to see if we can get the program to SEG-FAULT
                mem_ctl_exe_result = self.setProtectMem(i, 1000)
                pwd_checker_exe_result = self.checkPassword(
                    "".join(rightanswers) + letter
                )
                # If we segfault then our guess was correct and we can move forward to the next cell
                if pwd_checker_exe_result == "SEG ERROR":
                    i += 1
                    rightanswers.append(letter)
                    break
                # If we reach the end of the alphabet and nothing works that means we reached the end of the password
                if pwd_checker_exe_result == "Correct":
                    rightanswers.append(letter)
                    self.password = "".join(rightanswers)
                    return self.password


# Write Up
# Please explain your solution
# My strategy was that by blocking off all but the first cell of memory, we could tell if the first character of our password was correct. If we simply get "Wrong" then we know that first character was incorrect. However if we seg-fault that means we reached the 2nd cell of the password, thus the first cell was correct. We can simply brute-force this solution using every printable ASCII character and incrementally figure out the correct value for each cell until we have the correct password.
