# How many different ways can £2 be made using any number of coins?

different_ways = 0

for two_pounds in range(2):
    total_value = two_pounds*200
    for one_pound in range(int((200 - total_value)/100) + 1):
        total_value = two_pounds*200 + one_pound*100
        for fifty_pence in range(int((200 - total_value)/50) + 1):
            total_value = two_pounds*200 + one_pound*100 + fifty_pence*50
            for twenty_pence in range(int((200 - total_value)/20) + 1):
                total_value = two_pounds*200 + one_pound*100 + fifty_pence*50 + twenty_pence*20
                for ten_pence in range(int((200 - total_value)/10) + 1):
                    total_value = two_pounds*200 + one_pound*100 + fifty_pence*50 + twenty_pence*20 + ten_pence*10
                    for five_pence in range(int((200 - total_value)/5) + 1):
                        total_value = two_pounds*200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence*10 + five_pence*5
                        for two_pence in range(int((200 - total_value)/2) + 1):
                            total_value = two_pounds * 200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5 + two_pence*2
                            one_penny = 200 - total_value
                            different_ways += 1

print(different_ways)