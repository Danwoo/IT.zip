# IT.zip - 비전공자들을 위한 IT 뉴스 요약 서비스
 진행 : 스마트인재개발원 실전역량프로젝트

### - 기   간
 2023.05.31 ~ 2023.06.16

### - 담당역할
 팀원(데이터 수집, 전처리, 딥러닝 모델 구현, Flask 서버 구축, 용어사전 게시판(Spring Framework)기능 구현)

### - 개   요
 IT관련 기사 원문을 입력하고 카테고리를 설정해주면 키워드를 추출하고 이를 활용해 관리자는 KDT 교육 수강생을 평가하는 빈칸 문제로 출제가능

#### 언어
 Python, Spring(Gradle), NoSQL
#### 딥러닝 모델
 HuggingFace-Transformers(T5, BART)
#### 형태소 분석기
 Kiwipiepy

### - 개발내용
#### [역할]
1. Ke-T5 모델 학습(전이학습, Fine-Tuning), RDASS 점수로 평가
2. Flask 서버 Spring 연동
3. 관리자 화면의 퀴즈생성 및 용어사전 기능

#### [성과]
 클라우드에 모델을 업로드하여 서비스시간을 위해 T5 모델의 small버전을 사용했습니다.(30초 ->10초 이하)
 키워드 추출에서 알고리즘을 통해 KeyBert 모델보다 더 좋은 결과를 얻을 수 있었습니다.

#### [느낀점]
 생성형 AI 모델을 처음으로 튜닝하면서 관련 논문을 읽으며 새로운 모델을 학습하는 방법을 배웠습니다. 그리고 모델 특성에 따라 T5 모델이 BART 모델보다 더 긴 문장에 대해서 높은 RDASS값을 갖는 요약문을 출력하는 것을 확인하면서 다른 팀원과 각자 맡은 모델에 대한 리뷰를 할 수 있었습니다. 전체 서비스를 위해 네이버 클라우드에 모델과 Flask 파일을 파이썬 실행환경을 똑같이 복사해 CentOS로 올리는데 큰 어려움이 있었습니다. 원래 있던 파이썬3.6로 인해 충돌, numpy 버전 충돌 등 많은 어려움이 있었지만 기본 내장 파이썬을 제외한 관련 라이브러리를 수동삭제함으로써 모델과 Flask 파일을 올렸습니다. 또한 용어사전 페이지를 제작함으로써 Spring Framework에서 CRUD 기능을 구현해봤습니다.
 
##### [아쉬웠던 점]
 모델과 Flask 서버를 클라우드에 올렸지만 최종적으로 Spring과 연동을 못하여 아쉽습니다. 같은 네이버 드라이브에 포트번호 5000번으로 Spring에 연결했지만 MariaDB와 연동되지 않아서 실제로 서비스부분에 대해서는 관리자 페이지에 한해서만 가능하도록 전환하게 되었습니다. 

#### [시연영상]
[![Video Label](http://img.youtube.com/vi/MPy5yRgFTFM/0.jpg)](https://youtu.be/MPy5yRgFTFM)

#### [15인 전체 소스코드]
https://github.com/ppq0203/DCX-Final_Project
