import random
start = input('請決定隨機數字範圍起始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True :
	count += 1
	num = input('請猜數字: ')
	num =int(num)
	if num == r:
		print('答對了')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('這是你猜的第',count,'次')

