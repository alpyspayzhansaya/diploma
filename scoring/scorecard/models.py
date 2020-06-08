from django.db import models


GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)

MARRIAGE_CHOICES = (
    ('single', 'single'),
    ('married', 'married'),
)

EDUCATION_CHOICES = (
    ('associate', 'associate'),
    ('bachelor', 'bachelor'),
    ('master', 'master'),
    ('doctor', 'doctor'),
)


class RequestDetails(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    iin = models.IntegerField()
    marriage = models.CharField(max_length=20, choices=MARRIAGE_CHOICES)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    home_address = models.CharField(max_length=200)
    workplace = models.CharField(max_length=200)
    income = models.IntegerField()
    additional_income = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class ScoreCard(models.Model):
    request = models.ForeignKey(RequestDetails, on_delete=models.CASCADE)
    age = models.IntegerField()
    limit_bal = models.IntegerField()
    pay_0 = models.IntegerField()
    pay_2 = models.IntegerField()
    pay_6 = models.IntegerField()
    bill_amt5 = models.IntegerField()
    pay_amt1 = models.IntegerField()
    pay_amt2 = models.IntegerField()
    pay_amt3 = models.IntegerField()
    pay_amt4 = models.IntegerField()
    pay_amt5 = models.IntegerField()
    pay_amt6 = models.IntegerField()
    proba = models.FloatField()
    score = models.IntegerField()
    is_approved = models.BooleanField(default=False)
