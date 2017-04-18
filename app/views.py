from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django.db import connection,transaction
import json

# Create your views here.
def index(request):
    return render(request,"index.html")

def input(request):
    return render(request,"input.html")

def add(request):
    cursor = connection.cursor()
    sql = 'insert into app_ccbz(code,name,train,start_time,stop_time,work_time,work_bonus,in_time,out_time,rest_time,rest_bonus,sum_bonus) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    data = request.POST['html_data'].rstrip(u',删除').split(",")[12:]
    data=",".join(data)
    data = data.split(u'删除')
    for d in data:
        d=d.strip(",")
        sql_d = d.split(",")
        cursor.execute(sql,sql_d)
    transaction.commit()

    return HttpResponse(json.dumps({"html_data":data}))