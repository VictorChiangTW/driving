country = input("請輸入你的國家：")
age = int(input("請輸入你的年齡"))
if country == "台灣" or "臺灣" or "中華民國":
	if age >= 18:
		print("你可以開車")
	else:
		print("你還不能開車")