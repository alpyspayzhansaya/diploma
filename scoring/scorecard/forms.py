from django import forms


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


class ScoreForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    age = forms.IntegerField(label='Age', min_value = 18)
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, initial='male')
    iin = forms.IntegerField(label='Unique identification number')
    marriage = forms.ChoiceField(label='Marriage status', choices=MARRIAGE_CHOICES, initial='single')
    education = forms.ChoiceField(label='Education', choices=EDUCATION_CHOICES, initial='associate')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone number', max_length=100)
    home_address = forms.CharField(label='Address', max_length=200)
    workplace = forms.CharField(label='Workplace', max_length=200)
    income = forms.IntegerField(label='Income')
    additional_income = forms.IntegerField(label='Additional income')
    limit_bal = forms.IntegerField(label='Credit amount')
    pay_0 = forms.IntegerField(label='1st Payment status')
    pay_2 = forms.IntegerField(label='2nd Payment status')
    pay_6 = forms.IntegerField(label='3rd Payment status')
    bill_amt5 = forms.IntegerField(label='Amount of bill statement')
    pay_amt1 = forms.IntegerField(label='1st amount of previous payment')
    pay_amt2 = forms.IntegerField(label='2nd amount of previous payment')
    pay_amt3 = forms.IntegerField(label='3rd amount of previous payment')
    pay_amt4 = forms.IntegerField(label='4th amount of previous payment')
    pay_amt5 = forms.IntegerField(label='5th amount of previous payment')
    pay_amt6 = forms.IntegerField(label='6th amount of previous payment')
