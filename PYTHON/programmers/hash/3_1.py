phone_book = ["12","123","1235","567","88"]
phone_book.sort()
def soultion():
    # for i in range(len(phone_book)-1):
    #     if(len(phone_book[i]))<len(phone_book[i+1]):
    #         if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
    #             return False
        
    # return True
    for p1,p2 in zip(phone_book,phone_book[1:]):
        return not(p2.startswith(p1))
print(soultion())
