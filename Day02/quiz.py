#quiz

#1) 태어난 년도를 입력받고 현재 만나이 출력하는 프로그램
#ex) 2000 -> 23

year = int(input("태어난 년도를 입력하세요:"))
print(f"{2024 - year - 1}")

#2) 세 개의 숫자를 입력 받고, 총합, 평균(실수) 출력

a = float(input("첫 번째:"))
b = float(input("두 번째:"))
c = float(input("세 번째:"))
sum = a+b+c
avg = (a+b+c) / 3
print(f"총합: {sum}, 평균:{avg}")

#3) 섭씨 온도를 입력받아 화씨 온도로 변환을 출력하는 프로그램 만들기
# F = C * 5.9 + 32입니다.

celsius = float(input("섭씨 온도를 입력하세요:"))
fah = celsius * 5.9 + 32
print(f"화씨 온도는 {fah:.2f}입니다.")
# 변수[실수]:.2f 둘째 자리 출격

#4) 사용자의 키(m)와 몸무게(kg)를 입력받아 BMI를 출력하는 프로그램 만들기
# bmi = weight / (height ** 2)

weight = float(input("몸무게를 입력하세요:"))
height = float(input("키를 입력하세요"))
bmi = weight / (height ** 2)
print(bmi)
print(f"당신의 BMI는 {bmi:.2f}입니다.")

#5) 반지름 입력시 원의 넓이와 둘레를 구하는 프로그램

radius = float(input("반지름을 입력하세요:"))
width = 3.14 * (radius ** 2)
round = 2 * 3.14 * radius
print(f"원의 넓이는 {weight:.2f}이고, 원의 둘레는 {round:.2f}")




