generes  = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	

def solution():
    from collections import defaultdict
    playlist = defaultdict(list)

    idx = 0
    result = []
    for i,j in zip(generes,plays):
        playlist[i].append([idx,j])
        idx += 1

    playlist ={key:sorted(value, key = lambda x:x[1],reverse=True) for key,value in playlist.items()}
    playlist = dict(sorted(playlist.items(), key = lambda x:(sum(y[1] for y in x[1])),reverse=True))
    for i in playlist.items():
        if len(i[1])<2:
            result.append(i[1][0][0])
        else:
            result.append(i[1][0][0])
            result.append(i[1][1][0])
    return result
print(solution())