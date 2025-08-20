#this is program to suggest student carrier
sub1=input("enter first subject name you like: ")
sub2=input("enter the second subject you like: ")
if((sub1=="programming"and sub2=="maths")or(sub1=="maths"and sub2=="programming")):
   print("suggest computer engineering")
   
elif(sub1=="programming"and sub2=="statistic") or (sub1=="statistic" and sub2=="programming"):   
   print("suggest AI and DS Engineering")
   
elif(sub1=="programming"and sub2=="AI concept") or (sub1=="AI concept" and sub2=="programming"):   
   print("suggest AI and ML Engineering")
   
elif(sub1=="circuit"and sub2=="maths") or (sub1=="maths" and sub2=="circuit"):   
   print("suggest Electronics Engineering")
   
elif(sub1=="physics"and sub2=="maths") or (sub1=="maths" and sub2=="physics"):   
   print("suggest Mechanical Engineering")
   
elif(sub1=="biology"and sub2=="chemistry") or (sub1=="chemistry" and sub2=="biology"):   
   print("suggest BIOTECHNOLOGY")  
else:
   print("STREAM NOT FOUND..")
