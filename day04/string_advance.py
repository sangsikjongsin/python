#string_advance

# print(), input()[str], variable
# int(), str(), float(), bool(), list()
# datatype[int,float,str,list, ...]
# operator
# 산술: + - * / % // **, 논리 : and, or, not
# 비교 : <, >, !=, ==



coffee = "americano" #str
#내장 함수[int(), str(), float(), bool(), list(), print(), input()]
#len() : 길이를 알려주는 기능
print(len(coffee))
print(coffee.upper()) # AMERICANO
print(coffee.lower()) # americano
print(coffee.capitalize()) # Americano
print(coffee.strip()) # 빈공간 americano 빈공간 [빈공간 없애기]
print(coffee.find('c')) # 몇번째에 'c'가 있니? 5 #없으면 -1
print(coffee.replace('cano', 'can')) # 왼쪽에서 오른쪽으로 바꾸기
print(coffee.count('a')) # 'a' 몇개니? # 없으면 -1


#퀴즈 1: 대소문자 변환 프로그램
small = (input("소문자를 입력하세요:"))
print(small.upper())

#퀴즈 2: 노래 가사에서 단어 카운트
Puth = ("""Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
ever since the da day y-you went away
no I don't know how
how to erase your body from out my brain
whatcha gon do now
maybe I should just focus on me instead
But all I think about
are the nights we were tangled up in your bed
oh no (oh no)
oh no (oh no)
you're going round in circles got you stuck up in my head (yeah)
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
your love stays with me day and night
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
ever since the da da day y-you went away
someone tell me how
how much more do I gotta drink for the pain
whatcha gon do now
you did things to me that I just can't forget
now all I think about
are the nights we were tangled up in your bed
oh no (oh no)
oh no (oh no)
you're going round in circles got ya stuck up in my head
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
your love stays with me day and night
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
did ya know you're the one that got away
and even now baby i'm still not ok
did ya know that my dreams they're are the same
everytime I close my eyes
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
your love stays with me day and night
I can feel you over here i can feel you over here
you take up every corner of my mind
whatcha gon do now
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now """)

print(f"가사에서 left는 {Puth.count('left')}개, right는 {Puth.count('right')}개")
print(f"가사의 길이는 {len(Puth)}")


a = "mega"
b = "study"
c = a + b # + 문자열 연결 연산자 결과 : megastudy,
d = a * 3 # * 문자열 반복 연산자 결과 : megamegamega
f = a[0] # [] 문자열 인덱싱 결과 : m
f = b[0:3] #[start:end] 문자열 슬라이싱(end 제외) 결과 : stu
g = 'g' in a # "mega"에서 'g'가 있니? 결과 :  True or False


# split
title = "megastudy pthon programming"
print(title.split()) #빈공간 기준으로 str에서 list 만들어주기
title1 = "orange,apple,banna"
print(title1.split(','))

# user한테 이메일 주소를 입력받고 -> ['유저아이디', '도메인']
# ex) python@megastudy.com ['python', 'megastudy.com']

email = (input("이메일 주소를 입력하세요:"))
a = email.split("@") # ['python', 'megastudy.com']
b = a[1].split('.') # ['megastudy','com']
a[1] = b[0] # ['python', 'megastudy']
# a[2] = b[1] a[2]가 없으므로 안됨
a. append(b[1])
print(a)

# join
word = ' '.join(['ice', 'cream']) #'ice cream'
id = input("아이디 입력:")
domain = input("도메인 입력:")
print('@'.join([id,domain]))


article = """Arsenal lack cutting edge
Arsenal could and should have held a healthy advantage when this FA Cup tie reached half-time but they were let down by what is looking increasingly like a major flaw in Arteta's team.

The Gunners' approach work was to be admired as they made Liverpool suffer by moving the ball around but it all fell down at the crucial moment when chances were not taken.

It led to increasing frustration inside the Emirates as the game wore on, accompanied by the growing feeling that Arsenal would pay the price for their failures in front of goal.

Gabriel Jesus was missing with a knee injury but he is not a regular, reliable source of goals while Eddie Nketiah has yet to suggest he is the permanent answer to a growing problem for Arteta.

So much is good about this Arsenal team but there is always the danger they will fall short if all their eye-catching passing play is not accompanied by end product.

It is something Arteta must address as a matter of urgency - something the manager and the club may well agree with given the constant links with Brentford's Ivan Toney. Whether they can do business in the difficult January market remains to be seen.

This is Arsenal's third successive defeat since their creditable draw at Anfield on 23 December - and the feeling of positivity around Arteta's team after that result must be restored swiftly.

Liverpool make light of missing superstars
Liverpool were missing two of their best players in the meeting of the Premier League title challengers in this FA Cup tie - but they impressively overcame the absence of the ill Virgil van Dijk and Mohamed Salah, who is at the Africa Cup of Nations.

They were grateful for Arsenal's poor finishing in the first half but Klopp's side were always in the game and, even without Salah, they possess menace in their forward line and that was increasingly in evidence as the game went on.

Ibrahima Konate in particular stood out - proving he can produce commanding performances even without Van Dijk alongside him - while young defender Jarell Quansah continues to impress in the absence of Joel Matip.

Nunez was again inefficient with his efforts at goal but Jota was lively as he continues his return from injury.

Overall, finding a way to win without Van Dijk and Salah will send a surge of self-belief through Liverpool and their supporters that Klopp's new-look side can go on to achieve special things this season.

Liverpool lead the Premier League, play an EFL Cup semi-final against Fulham on Wednesday, are into the knockout stage of the Europa League and can now look forward to the FA Cup fourth-round draw with optimism."""

newArticle = article.replace('Liverpool', 'joat').replace('is','😀').split()
print(newArticle)