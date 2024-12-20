from django.shortcuts import render, redirect
from runcardapp.forms import DateForm
from datetime import datetime, timedelta

def runcardpage(request):
    today = (datetime.today() - timedelta(hours=5)).strftime('%Y-%m-%d')

    date_form = DateForm(request.GET)
    selected_date = today

    if date_form.is_valid():
        selected_date = date_form.cleaned_data['selected_date']

    if not selected_date:
        selected_date = today
        return redirect(f'/?selected_date={selected_date}')

    selected_date = selected_date.strftime('%Y-%m-%d')
    print(selected_date)
    return render(request, 'runcardapp/index.html', locals())