from django.shortcuts import render, HttpResponseRedirect
from models import Company, Task
import json, integers, strings
from datetime import datetime

def index(request):
  response = None
  print request.session.keys()
  if 'response' in request.session.keys():
    response = request.session['response']
    datediff = int(datetime.now().strftime('%s')) - int(response['created'])
    if datediff > integers.SESSION_TIME_TO_LIVE:
      response = request.session['response'] = None
  return render(request, 'index.html', {'response':json.dumps(response)})

def login(request):
  return render(request, 'login.html')

def process(request):
  current_epoch = datetime.now().strftime('%s')
  request.session['response'] = {'code':integers.CODE_SUCCESS,
  'message':strings.MESSAGE_SUCCESS, 'created':current_epoch}

  if request.method != 'POST':
    request.session['response'] = {'code':integers.CODE_INVALID_REQUEST_METHOD,
    'message':strings.MESSAGE_INVALID_REQUEST_METHOD, 'created':current_epoch}
    return HttpResponseRedirect('/')
  try:
    company_name = request.POST['company']
    task_description = request.POST['task']

    print task_description

    company = Company.objects.filter(name=company_name)
    if not company.exists():
      request.session['response'] = {'code':integers.CODE_INVALID_COMPANY_NAME,
      'message':strings.MESSAGE_INVALID_COMPANY_NAME, 'created':current_epoch}
      return HttpResponseRedirect('/')

    new_task = Task(description=task_description, company_id=company['id'])
    new_task_id = new_task.save()
    print new_task_id
    if not new_task_id:
      request.session['response'] = {'code':integers.CODE_SAVE_ERROR_TASK,
      'message':strings.MESSAGE_SAVE_ERROR_TASK, 'created':current_epoch}
      return HttpResponseRedirect('/')

  except Exception, e:
    print 'Exception occured: ' + str(e)
  return HttpResponseRedirect('/')
  
