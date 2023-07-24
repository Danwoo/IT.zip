text = """
맥을 인텔 프로세서로 전환한 애플은 맥에서 윈도우 및 윈도우 애플리케이션을 네이티브로 실행할 수 있는 길을 닦았고 대다수 기업에서 맥OS용으로 설계되지 않은 애플리케이션을 실행해야 할 필요성이 사라졌다.,클라우드 컴퓨팅은 세상을 다른 쪽으로 변화시켰고 서비스형 소프트웨어는 윈도우 데스크톱 및 애플리케이션 세계를 무너뜨렸다. 구글과 드롭박스 슬랙 및 심지어 마이크로소프트까지도 비즈니스 컴퓨팅이 놀라울 정도로 유연할 수 있고 대부분 작업을 브라우저에서 수행할 수 있음을 보여줬다. 브라우저보다 클라우드 서비스에 훨씬 나은 인터페이스를 제공하는 앱스토어가 있었다. 애플 MDM은 비즈니스에서 관심을 ,맥이 지원 비용에서 상당한 비용을 절감한다는 사실은 IBM과 포레스터의 수치로 알 수 있으며 맥이 지원 비용에서 상당한 비용을 절감한다는 것은 비즈니스에서의 맥 사용에 대한 주장을 강화한다."""
from kiwipiepy import Kiwi
kiwi = Kiwi()

text_list = text.split(' ')
print(text_list)
for t in text_list:
    tokens = kiwi.tokenize(t)
    for token in tokens:
        if token.tag == 'JX' and (token.form == '은' or token.form == '는'):
            print(token.tag)
            keyword_0 = t.replace(token.form,"")
# print(kiwi.tokenize(text))
print(keyword_0)


tokens = kiwi.tokenize(text)
for token in tokens:
    if token.tag == 'JX' and (token.form == '은' or token.form == '는'):
        keyword_0 = text[text.index(" "):text.index(token.form)]

print(keyword_0)

import kiwipiepy

# Kiwi 형태소 분석기 초기화
# kiwi = kiwipiepy.Kiwi()


from kiwipiepy import Kiwi

kiwi = Kiwi()

def extract_words_before_postposition(sentence):
    a = kiwi.tokenize(sentence)  # 문장 형태소 분석
    result = []
    print(a[1][0])
    print(a[1][1])
    print(len(a))
    for i in range(len(a)):
        if a[i][1] == 'JX' and (a[i][0] == '은' or a[i][0] == '는') and a[i-1][1].startswith('N') and not a[i-1][1] == 'NNB':  # 보조사(JX)와 명사(N으로 시작) 조합
            result.append(a[i-1][0])
    return result


# 문장 입력
sentence = "영화는 재미있는 것입니다."

# 앞에 있는 단어 추출
words = extract_words_before_postposition(sentence)

# 출력
print("입력 문장:", sentence)
print("앞에 있는 단어:", words)

print(extract_words_before_postposition(text))

