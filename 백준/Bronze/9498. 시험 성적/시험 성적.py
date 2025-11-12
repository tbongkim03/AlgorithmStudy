# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
score = int(input())
cut = score // 10
if (cut >= 9):
    print("A")
elif (cut == 8):
    print("B")
elif (cut == 7):
    print("C")
elif (cut == 6):
    print("D")
else:
    print("F")