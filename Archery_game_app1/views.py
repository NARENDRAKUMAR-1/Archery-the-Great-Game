from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

def home(request):
    return render(request,'home.html')

def compute_scores(request):
    nation1 = (request.GET['nation1'])
    nation2 = (request.GET['nation2'])
    nation3 = (request.GET['nation3'])

    nation1_score=0
    nation2_score=0
    nation3_score=0  

    if_anyone_not_won=True
    start=1
    end=5
    round_=0

    while(if_anyone_not_won):
      
        round_number=round_
        
        nation1_player1=random.randint(start,end)
        nation1_player2=random.randint(start,end)

        nation2_player1=random.randint(start,end)
        nation2_player2=random.randint(start,end)

        nation3_player1=random.randint(start,end)
        nation3_player2=random.randint(start,end)

        #code here for the bonus points
        if(nation1_player1==nation1_player2):
            nation1_score+=2
        if(nation2_player1==nation2_player2):
            nation2_score+=2
        if(nation3_player1==nation3_player2):
            nation3_score+=2

        nation1_score+=nation1_player1+nation1_player2
        nation2_score+=nation2_player1+nation2_player2
        nation3_score+=nation3_player1+nation3_player2

        max_of_all=max(nation1_score,nation2_score,nation3_score)

        if(nation1_score==nation2_score and nation1_score>=60 and nation2_score>=60 ):
            if (nation1_score>nation2_score):                
                winner=nation1
            else:               
                winner=nation2
            if_anyone_not_won=False
        
        if(nation1_score==nation3_score and nation1_score>=60 and nation2_score>=60 ):
            if (nation1_score>nation3_score):                 
                winner=nation1
            else:               
                winner=nation3
            if_anyone_not_won=False

        if(nation2_score==nation3_score and nation2_score>=60 and nation3_score>=60 ):
            if (nation2_score>nation3_score):                
                winner=nation2
            else:
                winner=nation3
            if_anyone_not_won=False
            
        if(max_of_all==nation1_score and nation1_score>=60): 
            
            winner=nation1
            if_anyone_not_won=False 
            
        if(max_of_all==nation2_score and nation2_score>=60): 
            
            winner=nation2
            if_anyone_not_won=False
         
        if(max_of_all==nation3_score and nation3_score>=60): 
           
            winner=nation3
            if_anyone_not_won=False 
                
        start+=1
        end+=1
        round_ += 1

    dict_final={
        'winner':winner,
        'round_number':round_number,
        'nation3_score':nation3_score,
        'nation2_score':nation2_score,
        'nation1_score':nation1_score,
        'nation1':nation1,
        'nation2':nation2,
        'nation3':nation3,
    }

    return render(request,'final_scoreboard.html',context=dict_final)

# def add(request):
#     val1 = int(request.GET['num1'])
#     val2 = int(request.GET['num2'])
#     res = val1 + val2

#     return render(request, "result.html", {'result1': res})