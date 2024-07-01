def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    
    return participant[-1]

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))


# counter 사용
import collections


example = ["leo", "kiki", "eden"]
example2 =["eden", "kiki"]
print(collections.Counter(example))
print(collections.Counter(example2))
print((collections.Counter(example)-collections.Counter(example2).keys()))