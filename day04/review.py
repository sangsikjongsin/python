#1. 정삼각형의 넓이와 둘레를 계산하는 프로그램 문구
height = int(input("높이 입력:"))
side = int(input("한변의 길이 입력::"))
print(f"정삼각형의 넓이는 {height*side*0.5} 둘레는 {side*3}")


#2.
a = input("운동 입력 : ")
b = input("운동 입력 : ")
c = input("운동 입력 : ")
print(f"운동 순서: {a}->{b}->{c}")

#3.
movieList = ['서울의 봄', '위시', '노량']
popcornList = ['팝톤', '치즈 팝콘', '캬라멜 팝콘']
drinksList = ['콜라', '제로 콜라', '스프라이트']

movie = int(input("영화 번호 고르시오[1번: 서울의 봄 2번: 위시 3번: 노량]:")) - 1
popcorn = int(input("팝콘 번호 고르시오[1번: 팝콘 2번: 치즈 팝콘 3번: 캬라멜 팝콘]:")) -1
drink = int(input("음료 번호 고르시오[1번: 콜라 2번: 제로콜라 3번: 스프라이트"]:)) -1
print(f"고르신 영화는 {movieList[movie]}이며 팝콘은 {popcornList[popcorn]} 그리고 음료는 {drinksList[drink]} 주문하셨습니다!")
