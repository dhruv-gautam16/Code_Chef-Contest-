# cook your dish here
t=input()
t=int(t)
while t:
    A=input()
    A=list(A)
    B=input()
    B=list(B)
#    print(A,B)
    A=list(map(int,A))
    B=list(map(int,B))
    larger_7_in_A=0
    seven_in_A=0
    four_in_A=0
    smaller_4_in_A=0
    in_between_A=0
    for i in A:
        if i<4: smaller_4_in_A=smaller_4_in_A+1
        elif i==4: four_in_A=four_in_A+1
        elif i<7: in_between_A=in_between_A+1
        elif i==7:seven_in_A=seven_in_A+1
        else: larger_7_in_A=larger_7_in_A+1

    larger_7_in_B=0
    seven_in_B=0
    four_in_B=0
    smaller_4_in_B=0
    in_between_B=0
    for i in B:
        if i<4: smaller_4_in_B=smaller_4_in_B+1
        elif i==4: four_in_B=four_in_B+1
        elif i<7: in_between_B=in_between_B+1
        elif i==7:seven_in_B=seven_in_B+1
        else: larger_7_in_B=larger_7_in_B+1

    answer=[]
    if seven_in_A<=in_between_B:
        answer.extend("7"*seven_in_A)
        in_between_B=in_between_B - seven_in_A
        seven_in_A=0
    if seven_in_A>in_between_B:
        answer.extend("7"*in_between_B)
        seven_in_A=seven_in_A - in_between_B
        in_between_B=0

    if seven_in_A<=smaller_4_in_B:
        answer.extend("7"*seven_in_A)
        smaller_4_in_B=smaller_4_in_B - seven_in_A
        seven_in_A=0
    if seven_in_A>smaller_4_in_B:
        answer.extend("7"*smaller_4_in_B)
        seven_in_A=seven_in_A - smaller_4_in_B
        smaller_4_in_B=0

    if seven_in_A<=four_in_B:
        answer.extend("7"*seven_in_A)
        four_in_B=four_in_B - seven_in_A
        seven_in_A=0
    if seven_in_A>four_in_B:
        answer.extend("7"*four_in_B)
        seven_in_A=seven_in_A - four_in_B
        four_in_B=0

    if seven_in_A<=seven_in_B:
        answer.extend("7"*seven_in_A)
        seven_in_B=seven_in_B - seven_in_A
        seven_in_A=0
    if seven_in_A>seven_in_B:
        answer.extend("7"*seven_in_B)
        seven_in_A=seven_in_A - seven_in_B
        seven_in_B=0

    if seven_in_B<=in_between_A:
        answer.extend("7"*seven_in_B)
        in_between_A=in_between_A - seven_in_B
        seven_in_B=0
    if seven_in_B>in_between_A:
        answer.extend("7"*in_between_A)
        seven_in_B=seven_in_B - in_between_A
        in_between_A=0

    if seven_in_B<=smaller_4_in_A:
        answer.extend("7"*seven_in_B)
        smaller_4_in_A=smaller_4_in_A - seven_in_B
        seven_in_B=0
    if seven_in_B>smaller_4_in_A:
        answer.extend("7"*smaller_4_in_A)
        seven_in_B=seven_in_B - smaller_4_in_A
        smaller_4_in_A=0

    if seven_in_B<=four_in_A:
        answer.extend("7"*seven_in_B)
        four_in_A=four_in_A - seven_in_B
        seven_in_B=0
    if seven_in_B>four_in_A:
        answer.extend("7"*four_in_A)
        seven_in_B=seven_in_B - four_in_A
        four_in_A=0

    if seven_in_B<=seven_in_A:
        answer.extend("7"*seven_in_B)
        seven_in_A=seven_in_A - seven_in_B
        seven_in_B=0
    if seven_in_B>seven_in_A:
        answer.extend("7"*seven_in_A)
        seven_in_B=seven_in_B - seven_in_A
        seven_in_A=0

    if four_in_B<=smaller_4_in_A:
        answer.extend("4"*four_in_B)
        smaller_4_in_A=smaller_4_in_A - four_in_B
        four_in_B=0
    if four_in_B>smaller_4_in_A:
        answer.extend("4"*smaller_4_in_A)
        four_in_B=four_in_B - smaller_4_in_A
        smaller_4_in_A=0

    if four_in_B<=four_in_A:
        answer.extend("4"*four_in_B)
        four_in_A=four_in_A - four_in_B
        four_in_B=0
    if four_in_B>four_in_A:
        answer.extend("4"*four_in_A)
        four_in_B=four_in_B - four_in_A
        four_in_A=0


    if four_in_A<=smaller_4_in_B:
        answer.extend("4"*four_in_A)
        smaller_4_in_B=smaller_4_in_B - four_in_A
        four_in_A=0
    if four_in_A>smaller_4_in_B:
        answer.extend("4"*smaller_4_in_B)
        four_in_A=four_in_A - smaller_4_in_A
        smaller_4_in_B=0

    if four_in_A<=four_in_B:
        answer.extend("4"*four_in_A)
        four_in_B=four_in_B - four_in_A
        four_in_A=0
    if four_in_A>four_in_B:
        answer.extend("4"*four_in_B)
        four_in_A=four_in_A - four_in_A
        four_in_B=0




#    print(answer)
    k=""
    for i in answer:
        k=k+i
    t=t-1
    print(k)
