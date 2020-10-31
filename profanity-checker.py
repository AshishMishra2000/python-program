from profanityfilter import ProfanityFilter
import time
pf = ProfanityFilter()
start_time = time.time()
profanity = []
total = 370283
openFile = open("script.js", "r")
i = openFile
j = 0
for words in i.read().split():
    if(pf.is_clean(words) != True):
        profanity.append(words)
        with open("profanity.txt", "a") as a_file:
            a_file.write("\n")
            a_file.write(words)
    # if(pf.is_clean(words) == True and len(words) > 8):
    #     with open("words.txt", "a") as a_file:
    #         a_file.write("\n")
    #         a_file.write(words)
    print(words)
    print(j, end=" ")
    print("of 370283          ", end=" ")
    percentage = (j/370283)*100
    print(round(percentage, 4), end=" ")
    print("%", end="                ")
    j = j+1
    end_time = time.time()
    time_elapsed = (end_time - start_time)
    time_elapsed_second = int(time_elapsed % 60)
    time_elapsed_minute = int((time_elapsed/60) % 60)
    time_elapsed_hour = int((time_elapsed/3600))
    print("Time Elapsed :", end=" ")
    print('%01d' % time_elapsed_hour, end=":")
    print('%02d' % time_elapsed_minute, end=":")
    print('%02d' % time_elapsed_second, end="          ")
    time_left = ((total-j)/j)*time_elapsed
    time_left_second = int(time_left % 60)
    time_left_minute = int((time_left/60) % 60)
    time_left_hour = int(time_left/3600)
    print("Time Left :", end=" ")
    print(time_left_hour, end=":")
    print(time_left_minute, end=":")
    print('%02d' % time_left_second)

for x in profanity:
    print(x)
