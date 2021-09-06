driving = input('請問你有開過車嗎？ ')
age = input('請問你的年齡是？ ')
age = int(age)
if driving == ('有'):
	if age >= 18:
		print('你通過測驗了！！ 恭喜')
	else:
		print('吓！點解你未夠秤 但係揸過車既？')
else:
	print('只能輸入 有/沒有')