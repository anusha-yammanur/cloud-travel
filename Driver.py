from CloudTravel import CloudTravel

ct = CloudTravel()

ct.shortestCouriertrip(((0,0,70)), ((90,0,45)), (("2","0 2","0 1")), 0, 1)

ct.shortestCouriertrip(((0,0,70)), ((90,0,45)), (("1 2","0 2","0 1")), 0, 1)

ct.shortestCouriertrip(((0,30,60)), ((25,-130,78)), (("1 2","0 2","1 2")), 0, 0)

ct.shortestCouriertrip(((0,20,55)), ((-20,85,42)), (("1","0","0")), 0, 2)

ct.shortestCouriertrip(((20,25,29,47)),((-70,67,-52, -78)),(("2 1","2","3","1 2 0")),0, 1)

ct.shortestCouriertrip(((20,20,29,47)),((-70,-70,-52, -78)),(("2 1","2","3","1 2 0")),0, 1)

ct.shortestCouriertrip(((20,20,29,47)),((-70,-75,-52, -78)),(("2 1","2","3","1 2 0")),0, 1)

ct.shortestCouriertrip(((20,25,29,47)),((-70,-70,-52, -78)),(("2 1","2","3","1 2 0")),0, 1)