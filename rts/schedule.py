class proc:
	def __init__(self,period,exc):
		self.period=period
		self.ex=exc

def main():
	t1=proc(4,1)
	print(t1.period," ",t1.ex)
    
if __name__ == '__main__':
	main()
