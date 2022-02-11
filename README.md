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

## 파이참 실행시
- 깃 클론 <br/>
   ```
   $git clone https://github.com/juhwano/ogt.git
   ```
- 장고 시크릿키 생성<br/>
https://miniwebtool.com/django-secret-key-generator/

<br/>

- 최상단 디렉토리에 secrets.json 파일 생성 후 생성한 시크릿키 넣기<br/>

```
{
  "SECRET_KEY" : "생성한 시크릿키"
}
```

- 데이터 마이그레이션<br/>
   ```
   python ./manage.py makemigrations
   python ./manage.py migrate
   ```
   
- DB 관리 shell 실행<br/>
   ```
   python ./manage.py shell
   ```
   
- DB 적용<br/>
  poll_data.txt 파일의 내용을 복사 후 붙여넣기 해주시면 됩니다.
  ```
  # 종료 
  exit()
  ```

- 서버 실행(기본 포트 : 8000)<br/>
   ```
   python ./manage.py runserver
   ```

## vsc 실행시
- 깃 클론 <br/>
   ```
   $git clone https://github.com/juhwano/ogt.git
   ```

- 가상환경 구성 <br/>
   ```
   python -m venv 가상환경폴더명
   ```

- 인터프리터 선택<br/>
![image3](https://user-images.githubusercontent.com/77667889/153522194-1fdf14f5-84a0-4fb0-998d-dd5199cebea5.png)

<br/>

- 확장프로그램 설치<br/>
인터프리터가 안 나온다면 확장프로그램 설치를 해줘야한다.<br/>
![image3_1](https://user-images.githubusercontent.com/77667889/153522236-cb5a6950-e27c-4816-b0db-3e9e6c44ac05.png)<br/>


- 장고 설치<br/>
   ```
   python -m pip install django
   ```

- 장고 시크릿키 생성<br/>
https://miniwebtool.com/django-secret-key-generator/

<br/>

- 최상단 디렉토리에 secrets.json 파일 생성 후 생성한 시크릿키 넣기<br/>
   ```
   {
     "SECRET_KEY" : "생성한 시크릿키"
   }
   ```

- 데이터 마이그레이션<br/>
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
   
- DB 관리 shell 실행<br/>
   ```
   python manage.py shell
   ```
   
- DB 적용<br/>
  poll_data.txt 파일의 내용을 복사 후 붙여넣기 해주시면 됩니다.
  ```
  # 종료 
  exit()
  ```

- 서버 실행(기본 포트 : 8000)<br/>
   ```
   python manage.py runserver
   ```
