p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}
p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}
p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1}
p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0}
p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}
data = [p1, p2, p3, p4, p5]
for i in data:
    def points():
        result = {}
        if i.get("role") == 'bat':
            point = i.get("runs")/2 +i.get("4")+(i.get("6"))* 2
            if (i.get("runs")) >= 50:
                point = point + 5
            elif (i.get("runs")) >= 100:
                point = point + 10
            elif 80 <= (((i.get("runs")) / (i.get("balls"))) * 100) <= 100:
                    point = point + 2
            elif (((i.get("runs")) / (i.get("balls"))) * 100) > 100:
                point = point + 4
            elif i.get("field")!=0:
                point=point+((i.get("field"))*10)
            result["name"] = i.get("name")
            result["batscore"] = point
            print(result)
        else:
            point=i.get("wkts")*10
            if i.get("wkts") in range(3,5):
                point=point+3
            elif i.get("wkts")>=5:
                point=point+10
            elif 3.5<(i.get("runs")/i.get("overs"))<=4.5:
                point=point+4
            elif 2<=(i.get("runs")/i.get("overs"))<3.5:
                point=point+7
            elif (i.get("runs")/i.get("overs"))<2:
                point=point+10
            elif i.get("field")!=0:
                point=point+((i.get("field"))*10)
            result["name"]=i.get("name")
            result["bowlscore"]=point
            print(result)
    points()
