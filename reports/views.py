from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def report_issue(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def report_list(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/report_list.html', {'reports': reports})
