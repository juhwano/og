from django.db import models

# Create your models here.
class Question(models.Model):
    STATUS_CHOICES = (
        ('p', 'Pulished'),
        ('e', 'Expired')
    )
    # 설문지명
    question_text = models.CharField(max_length=200)
    # 설문 문항 갯수
    choice_count = models.IntegerField(null=True)
    # 설문 진행 상태
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    # 설문 발행일
    create_at = models.DateTimeField(auto_now_add=True)
    # 설문 수정일
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # 설문지명
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택지명
    choice_text = models.CharField(max_length=200)
    # 답변자 전화번호
    user_number = models.CharField(max_length=13)
    # 응답 수
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text