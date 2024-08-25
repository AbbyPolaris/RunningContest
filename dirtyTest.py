from datetime import datetime
import contestant
import time
import contest

contestant = contestant.contestant
contest = contest.contest


contest1 = contest(1,100,4)
for i in range(10):
    con = contestant("ali",1,1,34534)
    contest1.add_contestant(contestant=con)

for i in contest1.contestants:
    del i
del contest1
