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

    def getHeuristic(self, prev):
        heuristic = []
        alphabet = [chr(i) for i in range(32, 127)]
        for letter in alphabet:
            letter_time = self.median_time_diff("".join(prev) + letter)
            heuristic.append(letter_time)
        return heuristic

    def getPassword(self):
        right_letters = []
        while True:
            heuristic = self.getHeuristic(right_letters)
            if "prevHeuristic" in locals():
                if abs(median(heuristic) - prevHeuristic) < 1e-6:
                    break
            prevHeuristic = median(heuristic)
            alphabet = [chr(i) for i in range(32, 127)]
            for letter in alphabet:
                median_time = self.median_time_diff("".join(right_letters) + letter)
                print(median_time, median(heuristic), letter)
                t_test, p_test = ttest_1samp(heuristic, median_time)
                if p_test < 0.01 and (median_time > median(heuristic)):
                    right_letters.append(letter)
                    print(right_letters, median_time)
                    break
        # Now brute force the last letter
        for letter in alphabet:
            result = check_password("".join(right_letters) + letter)
            print(result, letter)
            if result == "Correct":
                self.password = "".join(right_letters) + letter
                return "".join(right_letters) + letter
            # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        pass


sol = solution()
print(sol.getPassword())
# Write Up
# Please explain your solution
