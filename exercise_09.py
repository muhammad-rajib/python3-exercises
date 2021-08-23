# find the list average by function
#this funtion for find the average of list

def calculate_avg(li):
	n = len(li)
	tottal = 0

	for x in li:
		tottal=tottal+x
		average =tottal/n
		return average
