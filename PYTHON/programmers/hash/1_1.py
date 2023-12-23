from collections import Counter
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution():
    # participant.sort()
    # completion.sort()
    # for i in range(len(completion)):
    #     if(participant[i] != completion[i]):
    #         return participant[i]
    # return participant[-1]
    counter1 = Counter(participant)
    counter2 = Counter(completion)
    return(list((counter1-counter2).keys())[0])

print(solution())
