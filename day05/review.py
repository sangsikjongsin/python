# 1. 일본여행 계획 프로그램
plan = input("일본 여행 계획표를 입력하세요(쉼표 기준):")
planList = plan.split(",")
print(f"일본여행 계획표는 {planList} 입니다!")

# 2. 뉴스 기사 단어 찾기 프로그램
news = ("""Wigan 0-2 Manchester United: Pressure eases on Erik ten Hag as visitors progress to FA Cup fourth round
Report as Manchester United book their place in the FA Cup fourth round after defeating Wigan Athletic 2-0 at the DW Stadium; Diogo Dalot opener added to by Bruno Fernandes' second-half penalty against League One neighbours. Manchester United returned to winning ways to book their place in the FA Cup fourth round as goals in either half from Diogo Dalot and Bruno Fernandes secured a routine 2-0 success over League One Wigan Athletic at the DW Stadium. Having ended 2023 with defeat at Nottingham Forest, Dalot put United on the front foot with a sublime finish (22) for his second goal of the season - and after Fernandes was fouled inside the box by Liam Shaw, he converted his own spot-kick to ease any lingering nerves (74). United, after recording only their third win in their last 10 outings, will face a trip to either League Two Newport County or Eastleigh of the National League in the fourth round. It is United's first away win in any competition since the end of November at Everton, ending a run of five games on the road without a victory. Eleven years on from lifting the FA Cup against all the odds against Manchester City, Wigan entered the game 53 places below United in the English football pyramid. No Premier League side had exited the competition to a side in a lower division over the weekend. "They have to have a belief they can win the game," said manager Shaun Maloney, who provided the cup-winning corner and scored the winner in the only time Wigan have ever beaten United in a competitive fixture back in 2012. Nine of his starting line-up came through the youth team, were loan players or cost the club nothing due to financial irregularities and the impact of being placed in administration three-and-a-half years ago - and the hosts had the first chance inside three minutes.""")
word = input("찾고 싶은 단어를 입력하세요:")
countword = news.count(word)
print(f"{word}의 개수는 {countword}개 입니다.")


# 3. 스타벅스 메뉴 선택 프로그램
coffee = [4000, 5000, 5500]
cake = [5000, 6000, 5500]
choice_coffee = int(input("커피 메뉴[1.아메리카노 : 4000 2.라떼 : 5000 3.바닐라라떼 : 5500]:")) - 1
choice_cake = int(input("케익 메뉴[1.치즈케익 : 5000 2.딸기케익 : 6000 3.우유케익 : 5500]:")) - 1
print(f"고르신 커피와 케익의 값은 {coffee[choice_coffee] + cake[choice_cake]}입니다.")

# 4. 좋아하는 커피 브랜드 저장 프로그램
brands = input("좋아하는 커피 브랜드 입력(쉼표 기준):").split(',')
brands[0] = brands[0].capitalize()
brands[1] = brands[1].capitalize()
brands[2] = brands[2].capitalize()
print(brands)