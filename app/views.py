from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django.db import connection,transaction
from app.models import CCBZ
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


def grid(request):
    ccbz_data = CCBZ.objects.all()
    print(ccbz_data.query)
    return render_to_response("grid.html",{"data":ccbz_data})

def chart(request):
    cursor = connection.cursor()
    sql = "select name,sum(work_time) as s from app_ccbz group by name order by s desc;"
    cursor.execute(sql)
    ccqk_data = cursor.fetchall()
    k=[]
    v=[]
    for cc in ccqk_data:
        k.append(cc[0])
        v.append(cc[1])
    return render_to_response("chart.html",{"key":k,"value":v})