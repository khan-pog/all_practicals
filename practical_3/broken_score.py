"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():  # DONE: ADDED TO MAIN
    """Function docstring"""
    score = float(input("Enter score: "))
    result = processes_score_into_result(score)  # DONE: ADD FUNCTION WHERE OLD CODE WAS
    print(result)
    score = random.randint(0, 100)
    processes_score_into_result(score)  # DONE: ADDED RANDOM SCORE TURNED THAT SCORE INTO A RESULT THEN PRINTED
    print(result)

def processes_score_into_result(score):  # DONE: MADE SCORE PROCESSES FUNCTION
    """ processes a score into a result """
    # statements...
    if 0 < score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"






main()
