# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


# # 시간 복잡도 에러
# from collections import deque
# participant = deque(participant)
# completion = deque(completion)
# for i in completion:
#     if (i in participant):
#         del participant[participant.index(i)]
# print(participant[0])

# # 시간 복잡도 에러 x -counter 풀이
# from collections import Counter

# list1= Counter(participant)
# list2 = Counter(completion)
# result = list1 - list2
# print(''.join(result.keys()))


# 시간 복잡도 에러 x - sort 로 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if(participant[i]!=completion[i]):
            return participant[i]
    return participant[-1]

print(solution(participant,completion))

