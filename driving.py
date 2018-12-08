country = input("請輸入你的國家：")
age = int(input("請輸入你的年齡"))
if country == "台灣" or "臺灣" or "中華民國":
	if age >= 18:
		print("你可以開車")
	else:
		print("你還不能開車")
elif country == "美國" or "USA":
	if age >= 16:
		print("你可以開車")
	else:
		print("你還不能開車")
#不知道為什麼，美國的部分，輸入16，會進入到else的你還不能開車
else:
	print("抱歉，只能輸入台灣或美國")