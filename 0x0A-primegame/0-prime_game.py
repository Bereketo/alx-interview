#!/usr/bin/python3


def isWinner(x, nums):
    # Function to check if a number is prime
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def determineWinner(num):
        if num == 1:
            return "Ben"
        elif num % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    mariaWins = 0
    benWins = 0

    # Determine the winner for each round
    for num in nums:
        winner = determineWinner(num)
        if winner == "Maria":
            mariaWins += 1
        elif winner == "Ben":
            benWins += 1

    # Determine the overall winner
    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
