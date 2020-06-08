import math

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

from . import forms
from . import models


def index(request):
    if request.method == 'POST':
        form = forms.ScoreForm(request.POST)
        if form.is_valid():
            limit_bal = form.cleaned_data['limit_bal']
            pay_0 = form.cleaned_data['pay_0']
            pay_2 = form.cleaned_data['pay_2']
            pay_6 = form.cleaned_data['pay_6']
            bill_amt5 = form.cleaned_data['bill_amt5']
            pay_amt1 = form.cleaned_data['pay_amt1']
            pay_amt2 = form.cleaned_data['pay_amt2']
            pay_amt3 = form.cleaned_data['pay_amt3']
            pay_amt4 = form.cleaned_data['pay_amt4']
            pay_amt5 = form.cleaned_data['pay_amt5']
            pay_amt6 = form.cleaned_data['pay_amt6']
            age = form.cleaned_data['age']

            is_approved = False
            sql = None
            with open('scorecard.sql', 'r') as f:
                sql = f.read()

                sql = sql.replace('LIMIT_BAL', str(limit_bal))
                sql = sql.replace('PAY_0', str(pay_0))
                sql = sql.replace('PAY_2', str(pay_2))
                sql = sql.replace('PAY_6', str(pay_6))
                sql = sql.replace('BILL_AMT5', str(bill_amt5))
                sql = sql.replace('PAY_AMT1', str(pay_amt1))
                sql = sql.replace('PAY_AMT2', str(pay_amt2))
                sql = sql.replace('PAY_AMT3', str(pay_amt3))
                sql = sql.replace('PAY_AMT4', str(pay_amt4))
                sql = sql.replace('PAY_AMT5', str(pay_amt5))
                sql = sql.replace('PAY_AMT6', str(pay_amt6))
                sql = sql.replace('AGE', str(age))

            with connection.cursor() as cursor:
                value = cursor.execute('SELECT ' + sql)
                proba = cursor.fetchone()[0]

            score = int(math.trunc((1 - proba)*1000))

            if score >= 830:
                is_approved = True

            rq = models.RequestDetails(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                gender=form.cleaned_data['gender'],
                iin=form.cleaned_data['iin'],
                marriage=form.cleaned_data['marriage'],
                education=form.cleaned_data['education'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                home_adress=form.cleaned_data['home_adress'],
                workplace=form.cleaned_data['workplace'],
                income=form.cleaned_data['income'],
                additional_income=form.cleaned_data['additional_income']
            )
            rq.save()

            sc = models.ScoreCard(
                request=rq,
                limit_bal=limit_bal,
                pay_0=pay_0,
                pay_2=pay_2,
                pay_6=pay_6,
                bill_amt5=bill_amt5,
                pay_amt1=pay_amt1,
                pay_amt2=pay_amt2,
                pay_amt3=pay_amt3,
                pay_amt4=pay_amt4,
                pay_amt5=pay_amt5,
                pay_amt6=pay_amt6,
                age=age,
                proba=proba,
                score=score,
                is_approved=is_approved
            )
            sc.save()

            if is_approved:
                return redirect('/approved')
            else:
                return redirect('/declined')
    else:
        form = forms.ScoreForm()
        return render(request, 'scorecard/index.html', {'form': form})


def approved(request):
    return render(request, 'scorecard/approved.html')


def declined(request):
    return render(request, 'scorecard/declined.html')
