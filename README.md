# api 구성

> /admin/
> <br/>
> 관리자 기본페이지

> /admin/polls/
> <br/>
> 전체 설문 페이지

> /admin/polls/5
> <br/>
> 특정 설문 페이지

> /admin/polls/5/update
> <br/>
> 특정 설문 수정 페이지

> /admin/polls/create
> <br/>
> 설문 추가 페이지

> /admin/a
> <br/>
> 관리자 분석 페이지

<br/>

# 실행 방법

1. 깃 클론 <br/>
   `$git clone https://github.com/juhwano/ogt.git`

2. 데이터 마이그레이션<br/>
   `python ./manage.py makemigrations`

3. DB 적용<br/>
   `python ./manage.py migrate`

4. 서버 실행(기본 포트 : 8000)<br/>
   `python ./manage.py runserver`
