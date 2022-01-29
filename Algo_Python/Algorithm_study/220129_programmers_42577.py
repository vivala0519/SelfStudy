# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]	
phone_book = ["12","123","1235","567","88"]	

phone_book.sort()
try:
    for i in range(len(phone_book)):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            print(False)
except:
    pass
print(True)