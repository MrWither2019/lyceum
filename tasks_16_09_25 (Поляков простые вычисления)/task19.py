num = int(input())
pause = 10 * num
lesson = 45 * num

hours = 8 + ((30 + pause + lesson) // 60)
minutes =(30 + pause + lesson)% 60

print(hours, minutes, sep = ":")

