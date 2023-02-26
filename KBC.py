from David import say
say("CAPS LOCK ON TO PLAY KBC AND PRESS ENTER\n")
input("CAPS LOCK ON TO PLAY KBC AND PRESS ENTER\n")

# correct answer rakhnu paro in one place
# verify the answer.

def qna(ans):
    print("")
    ussr = input("Your answer: ")
    if ussr == ans:
        print("Bilkul sahi jawab\n")
        say("Absolutely correct\n")
    else:
        print(f"Incorrect\n")
        say(f"Sorry! your answer is Incorrect\n")
        exit()
        
def question_no(qn):
    if qn==1:
        return qna("A")
    elif qn==2:
        return qna("D")
    elif qn==3:
        return qna("C")
    elif qn==4:
        return qna("D")
    elif qn==5:
        return qna("D")
    elif qn==6:
        return qna("D")
    elif qn==7:
        return qna("B")
    elif qn==8:
        return qna("B")
    elif qn==9:
        return qna("D")
    elif qn==10:
        return qna("D")
    elif qn==11:
        return qna("B")
    elif qn==12:
        return qna("A")
    elif qn==13:
        return qna("B")
    elif qn==14:
        return qna("C")
    elif qn==15:
        return qna("B")
    elif qn==16:
        return qna("B")
    
    
que = ['''1. Leopard Tanks are advanced battle tanks manufactured by
(A) Germany
(B) China
(C) Russia
(D) United States''',
'''2. Which of the following country shares land border with Ukraine?
(A) Germany
(B) Croatia
(C) Estonia
(D) Poland''','''3. International Hockey World Cup 2023 is currently being played in
(A) Australia
(B) England
(C) India
(D) Pakistan''','''4. Which country has won the International Hockey World Cup for a record four times?
(A) Germany
(B) Holland
(C) India
(D) Pakistan''','''5. Kevin McCarthy became the speaker of the United States House of Representatives on 7 January 2023 in which round of the voting?
(A) 3rd
(B) 5th
(C) 10th
(D) 15th''','''6. Who is named as “Person of the Year 2022” by the Time Magazine?
(A) Elon Musk
(B) Vladimir Putin
(C) Lionel Messi
(D) Volodymyr Zelensky''','''7. The “Hundred Years’ War” was a series of armed conflicts between the kingdoms of
(A) China and Japan
(B) England and France
(C) Canada and United States
(D) Spain and Italy''','''8. Three Gorges Dam has world’s largest power station. It is located in
(A) Canada
(B) China
(C) Russia
(D) United States''','''9. The total installed capacity of power station of the “Three Gorges Dam” in China is
(A) 10,500 MW
(B) 14,500 MW
(C) 18,500 MW
(D) 22,500 MW''','''10. The United States’ state of “Alaska” shares maritime border with Canada and
(A) Mexico
(B) Iceland
(C) Greenland
(D) Russia''','''11. The “Hawaii” state of the United States is located about 2000 miles from the US mainland in the
(A) Atlantic ocean
(B) Pacific ocean
(C) Arctic ocean
(D) Mediterranean Sea''','''12. What is the name of the ocean that lies between Europe and the United States?
(A) Atlantic ocean
(B) Pacific ocean
(C) Arctic ocean
(D) Mediterranean Sea''','''13. What height is known as “Death zone” where oxygen is insufficient for human life?
(A) 7500 meter
(B) 8000 meter
(C) 8500 meter
(D) 9000 meter''','''14. By volume of water, the world’s largest freshwater lake is
(A) Caspian Sea
(B) Lake Superior
(C) Lake Baikal
(D) Lake Lucerne''','''15. The International Olympic Committee (IOC) was founded by
(A) Demetrios Vikelas
(B) Pierre de Coubertin
(C) Thomas Bach
(D) Juan Antonio Samaranch''','''16. The headquarters of International Olympic Committee (IOC) is located in
(A) Berlin
(B) Lausanne
(C) London
(D) Zurich''',]

QNO = 0

for i in que:
    print(i)
    QNO += 1
    question_no(QNO)
say("""Congratulations...
    you got it all right! 
    Well done""")
print("Congratulations you got it all right!")
    
    # qna("A")
    
    
       
    