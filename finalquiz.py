print("welcome to the quiz world")
usename=input("enter your name")
ques1_ans='2'
ques2_ans='20'
ques3_ans='100'
score=0
ques1="1. which of the following is even? \n (a)2 \n (b)3 \n (c)1 \n (d)0"
ques2="2. which one of the following is not a multiple of 8? \n (a)16 \n (b)64 \n (c) 80 \n (d) 20"
ques3="3. which is a multiple of 10? \n (a)25 \n (b)35 \n (c)100 \n (d) 58"
print(ques1)
ans1=input("enter your ans")
if ans1==ques1_ans:
    ans=print("correct answer")
    score+=1
    print(ques2)
else:
    print("try again")
while ans1!=ques1_ans:
    print("incorrect answer")
    ans1=input("enter your ans")
if ans1==ques1_ans:
    print("correct answer")
    print(ques2)
ans2=input("enter your ans")
if ans2==ques2_ans:
    ans=print("correct answer")
    score+=1
    print(ques3)
else:
    print("try again")
while ans2!=ques2_ans:
    print("incorrect answer")
    ans2=input("enter your ans")
    print(ques3)
if ans2==ques2_ans:
    print("correct answer")
    print(ques3)
ans3=input("enter your ans")
if ans3==ques3_ans:
    ans=print("correct answer")
    score+=1
else:
    print("try again")
while ans3!=ques3_ans:
    print("incorrect answer")
    ans3=input("enter your ans")
if ans3==ques3_ans:
    print("correct answer")
print("your final score is" + str(score) )
print ("thankyou")
            
