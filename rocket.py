import time

rocket = ">>======[INDIA]==👩‍🚀>>"
fire = "/-\\|"

for i in range(30):
	time.sleep(0.4)
	distance = " "*i
	print(distance + fire[i%len(fire)] + rocket)