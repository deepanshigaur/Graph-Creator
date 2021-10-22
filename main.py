import turtle
def seq3np1(n):
	"""
	Print the 3n+1 sequence from n, terminating when it reaches 1.
	args: n (int) starting value for 3n+1 sequence
	return: None
	"""
	count = 0
	while(n != 1):
	#print(n)
		if(n % 2) == 0:        # n is even
			n = n // 2
			count += 1
		else:                 # n is odd
			n = n * 3 + 1
			count += 1
	return count
    #print(n)                  # the last print is 1

def graph(start):
	""" 
	creates the graph for the function seq3np1
	args: (turtle),turtle
	return: none
	"""
	write = turtle.Turtle()
	wn = turtle.Screen()
	draw = turtle.Turtle()
	wn.setworldcoordinates(0,0,10,10)
	max_so_far = 0
	for i in range (1, start+1):
		result = seq3np1(i)
		if (result > max_so_far):
			max_so_far = result
			write.goto(0,max_so_far)
			write.clear()
			write.write({"maximum so far", i , max_so_far},font = {"Arial", 8, "normal"})
		wn.setworldcoordinates(0,0,i+10, max_so_far+10)
		draw.goto(i, result)
		draw.dot(10,"cyan")
	wn.exitonclick()


def main():
	seq3np1(3)
	start = int(input("Number for upper bound: "))
	for i in range(1, start+1):
    		count = seq3np1(i)
    		print("Number of", i, "iterations:", count)
	graph(start)
	
main()
