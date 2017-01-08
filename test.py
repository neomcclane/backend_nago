def comprobar(*args, **kwargs):
	print('len(args)--> '+str(len(kwargs)))

def main():
	comprobar('a', 'b', cuatro=4)

if __name__ == '__main__':
	main()