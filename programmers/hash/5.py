from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop","hiphop"]
plays =[500, 600, 150, 800, 2500,4500]	
idx = 0
playlist = defaultdict(list)
result = []
play =defaultdict(list)
for i, j in zip(genres, plays):
    playlist[i].append([idx, j])
    idx += 1
    
for key,value in playlist.items():
    print(value)
    play[key].append(sorted(value,key = lambda x:x[1],reverse=True))
    print(play)
# play = [sorted(plays, key=lambda x: x[1], reverse=True) for genre, plays in playlist.items()]
# print(play)
# # 각 장르의 합계를 계산하여 정렬
sorted_playlist = {genre: sorted(plays, key=lambda x: x[1], reverse=True) for genre, plays in playlist.items()}
# # 합계를 기준으로 정렬한 결과에서 장르 순서를 재조정
# sorted_result = sorted(sorted_playlist.items(), key=lambda x: sum(y[1] for y in x[1]), reverse=True)

# for i in range(len(sorted_result)):


#     if(len(sorted_result[i][1])<2):
#         result.append(sorted_result[i][1][0][0])
#     else:   
#         result.append(sorted_result[i][1][0][0])
#         result.append(sorted_result[i][1][1][0])
# print(result)
