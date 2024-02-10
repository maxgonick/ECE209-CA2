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
    def median_time_diff(self, sequence, trials=1000):
        temp = []
        for i in range(trials):
            T1 = time.perf_counter()
            result = check_password(sequence)
            T2 = time.perf_counter()
            temp.append(T2 - T1)
        return median((temp))

    # Brute force checks sequence + ascii
    def bruteForce(self, sequence):
        alphabet = [chr(i) for i in range(32, 127)]
        for letter in alphabet:
            result = check_password(sequence + letter)
            if result == "Correct":
                sequence.append(letter)
                self.password = "".join(sequence)
                return True
        return False

    def getPassword(self):
        alphabet = [chr(i) for i in range(32, 127)]
        right_letters = []
        while True:
            # Sanity Check if we guessed wrong then restart
            if len(right_letters) > 11:
                right_letters = []
            time_collection = []
            # Brute Force to see if we stop here
            if self.bruteForce("".join(right_letters)):
                return self.password
            # For each letter calculate the median time of 10,000 trials, then select the character that had the largest median time
            for letter in alphabet:
                median_time = self.median_time_diff("".join(right_letters) + letter)
                time_collection.append((median_time, letter))
            # Find the letter that made the highest median time
            bestLetter = max(time_collection, key=lambda x: x[0])[1]
            right_letters.append(bestLetter)
            # print(right_letters)
            if check_password("".join(right_letters)) == "Correct":
                self.password = "".join(right_letters)
                return self.password

            # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        pass


# sol = solution()
# print(sol.getPassword())
# Write Up
# Please explain your solution
# My idea was to take a large sample of each character (~1000 by heuristics) and then find the median of that sample to average out the noise. I would compute this on each character and select the character that had the largest median time. I would then bruteforce check every ascii character on my sequence, as there isn't any obvious way of checking the last letter of the alphabet. I continue to do this until my guesses reach over 11 characters in which I restart, as we likely made a mistake
