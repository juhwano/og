from django.db import models

# Create your models here.
class Question(models.Model):
    STATUS_CHOICES = (
        ('p', 'Pulished'),
        ('e', 'Expired')
    )
    # 설문지명
    question_text = models.CharField(max_length=200, null=True)
    # 설문 진행 상태
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    # 설문 발행일
    created_at = models.DateTimeField(auto_now_add=True)
    # 설문 수정일
    updated_at = models.DateTimeField(auto_now=True)
    # 응답 수
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # 설문지명
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    # 문항명
    choice_text = models.CharField(max_length=200, null=True)
    # 응답 수
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.choice_text

class Select(models.Model):
    # 문항명
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    # 선택지명
    select_text = models.CharField(max_length=100, null=True)
    # 유형
    choice_type = models.CharField(max_length=10, null=True)
    # 응답 수
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.select_text

class User(models.Model):
    # 설문지명
    question_name = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    # 문항명
    select_name = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    # 사용자 선택
    user_select = models.ForeignKey(Select, on_delete=models.CASCADE, null=True)
    # 답변자 전화번호
    user_number = models.CharField(max_length=13, null=True)
    # 참여일
    user_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_number