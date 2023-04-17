from datetime import datetime
import time, random

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

odds2 = []
x = 1
while x < 60:
    if x%2 ==1:
        odds2.append(x)
    x += 2

# print(odds)
# print(odds2)

right_this_minute = datetime.today().minute

for i in range(5):
    if right_this_minute%2==1:
        print("This minute seems a little odd.", right_this_minute)
    else:
        print("Not an odd minute.", right_this_minute)
    wait_time = random.randint(1,10)
    print('Wait time is: ', wait_time)
    time.sleep(wait_time)