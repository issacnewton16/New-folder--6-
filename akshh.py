def squareontime(n):
    itertion=0
    for i in range(0,n):
      for j in range(0,n):
       print("*",end="")
      iteration+=1
      print("")
    print("\nwhen n is",n,"iteration=",iteration,"\n") 

squareontime(4)
squareontime(9)
squareontime(6)