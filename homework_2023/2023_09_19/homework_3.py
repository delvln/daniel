print ("Enter seconds : ")
seconds = int(input())
hours = seconds //3600
minutes = (seconds %3600)//60
seconds_1 = (seconds %3600)%60
# print ( hours, minutes, seconds_1)
print (seconds,"seconds is", hours, "hours", minutes, "minutes", seconds_1, "seconds" )