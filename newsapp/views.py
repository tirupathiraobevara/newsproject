from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')
def moviesinfo(request):
    head_msg='Latest Movie Information'
    msg1='samantha slowley getting cured'
    msg2='RRR movie got oscar award'
    msg3='Prabhas going to marriage soon'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def sportsinfo(request):
    head_msg = 'Latest sports Information'
    msg1 = 'virat kohili is an indian international'
    msg2 = 'cristiano ronaldo is a football player'
    msg3 = 'hockey is a national game of india'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'newsapp/news.html', context=my_dict)
def politicsinfo(request):
    head_msg = 'Latest politics Information'
    msg1 = 'Narendra modi is a prime minister of india'
    msg2 = 'Jagan mohan reddy is a cm of Andhra pradesh'
    msg3 = 'Vijayasri reddy is a mp'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'newsapp/news.html', context=my_dict)