# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password
from statistics import mode, median, mean, stdev
from scipy.stats import ttest_1samp
import pip


class solution:
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""  # This is where your guessed password is store

    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas

        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        temp = []
        for i in range(5000):
            T1 = time.perf_counter()
            result = check_password("8jf&")
            T2 = time.perf_counter()
            temp.append(T2 - T1)

        # You can print the output for debug or test.
        print(result)
        print("time spend: ", median(temp))

    def median_time_diff(self, sequence, trials=10000):
        temp = []
        for i in range(trials):
            T1 = time.perf_counter()
            result = check_password(sequence)
            T2 = time.perf_counter()
            temp.append(T2 - T1)
        return median(temp)

    def getPassword(self):
        right_letters = []
        while True:
            alphabet = [chr(i) for i in range(32, 127)]
            time_collection = []
            # For each letter calculate the median time of 10,000 trials, then select the character that had the largest median time
            for letter in alphabet:
                median_time = self.median_time_diff("".join(right_letters) + letter)
                # print(median_time, letter)
                time_collection.append((median_time, letter))
            # Find the letter that made the highest median time
            right_letters.append(max(time_collection, key=lambda x: x[0])[1])
            mostTime = max(time_collection, key=lambda x: x[0])
            leastTime = min(time_collection, key=lambda x: x[0])
            print(mostTime[0] - leastTime[0], mostTime[1], leastTime[1])
            print(right_letters)

            # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        self.password = "".join(right_letters)
        return self.password
        pass


sol = solution()
print(sol.getPassword())
# Write Up
# Please explain your solution
