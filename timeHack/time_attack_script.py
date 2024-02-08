# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password
from statistics import mode, median, mean, stdev


class solution:
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""  # This is where your guessed password is store

    # To average out the noise we take a large number of trials and find the median of that
    def median_time_diff(self, sequence, trials=10000):
        temp = []
        for i in range(trials):
            T1 = time.perf_counter()
            result = check_password(sequence)
            T2 = time.perf_counter()
            temp.append(T2 - T1)
        return median(temp)

    def bruteForce(self, sequence):
        alphabet = [chr(i) for i in range(32, 127)]
        for letter in alphabet:
            result = check_password(sequence + letter)
            if result == "Correct":
                self.password = letter
                return True
        return False

    def getPassword(self):
        alphabet = [chr(i) for i in range(32, 127)]
        # For one character passwords we just bruteforce and check

        if self.bruteForce(""):
            return self.password

        right_letters = []
        while True:
            time_collection = []
            # For each letter calculate the median time of 10,000 trials, then select the character that had the largest median time
            for letter in alphabet:
                median_time = self.median_time_diff("".join(right_letters) + letter)
                time_collection.append((median_time, letter))
            # Find the letter that made the highest median time
            bestLetter = max(time_collection, key=lambda x: x[0])[1]
            right_letters.append(bestLetter)
            if check_password("".join(right_letters)) == "Correct":
                self.password = "".join(right_letters)
                return self.password
            # Brute Force to check if we stop here
            if self.bruteForce("".join(right_letters)):
                return self.password

            # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        pass


sol = solution()
print(sol.getPassword())
# Write Up
# Please explain your solution
