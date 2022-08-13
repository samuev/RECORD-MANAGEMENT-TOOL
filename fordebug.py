def power(x,y):
	 temp = 0
	 if( y == 0):
	  	return 1
	 temp = power(x, int(y / 2))
	 print(f"1: {temp}")
	 if (y % 2 == 0):
		  print(f"2: {temp}")
		  return temp * temp
	 else:
		 print(f"3: {temp}")
		 return x * temp * temp

print(power(2,3))