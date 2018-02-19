import csv, math, sys

# return array that include course name ,weight and grade in each term
# record[term_start0][coursename0 or weight1 or grade2][order of information]
def getRecord(file):
    course = []
    weight = []
    grade = []
    record = []
    section = []
    term = -1 # exam 0 mean year 1 term 1 ,1 mean year 1 term 2 and so on
    status = 0 # o mean data is not necessary 
    with open(file,'r', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            # phase for check that is no more course in that term
            if row[0] == '' and status == 1:
                status = 0
                record.append([course[term],weight[term],grade[term],section[term]])
            # phase for add course and weight grade to that term
            if status == 1:
                course[term].append(row[0])
                weight[term].append(row[4])
                grade[term].append(row[6])
                section[term].append(row[5])
            # phase for enable to add course to new term
            if row[0] == 'ชื่อวิชา':
                status = 1
                course.append([])
                weight.append([])
                grade.append([])
                section.append([])
                term += 1
    return record
    
# get imforation with course , weight and grade then 
# print gpa in each term and sum term 
def showGPA(record):
    count = 0
    total_marks = 0 #sum of (weight*grade) 
    totol_weight = 0 # sum of weight in every term
    value_grade = { 'A':4, 'B+':3.5, 'B':3, 'C+':2.5, 'C':2, 'D+':1.5, 'D':1, 'I':0, 'F':0 }
    for info in record:
        print('..................')
        year = math.floor(count/2) + 1
        term = count%2 + 1 # term = 1 if that is term 1
        print('.Year '+str(year)+'  .Term '+str(term)+' .')
        # loop for check in each course in this term
        gpa = 0
        sum_weight = 0
        for i in range(len(info[0])):
            print(info[0][i] + ' weight : ' + info[1][i] + ' grade : ' + info[2][i])
            sum_weight += int(info[1][i])
            gpa += int(info[1][i]) * value_grade[info[2][i]]
        # update for next term calculate gpax
        total_marks += gpa
        totol_weight += sum_weight
        # cal gpa and gpax
        gpax = str(round(total_marks / totol_weight, 2))
        gpa = str(round(gpa / sum_weight, 2)) 
        # show in console
        print('GPA : '+gpa)
        print('GPAX : '+gpax)
        count += 1

#export to default format csv file 
def exportCSV(record):
    termCount = 0
    with open('export.csv', 'w' ,newline='') as f:
        fieldnames = ['SubjectID','SubjectName','Weight','Section','Grade','Term']
        file = csv.DictWriter(f,fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        #writeHead
        file.writeheader()
        for term in record:
            termCount += 1
            #split SubjectID and SubjectName
            countSubject = 0
            for i in term[0]:
                subj = i.split('   ') # subj = i.split('  ') = [SubjectID[], SubjectName[]]
                w = term[1][countSubject] # w = weight
                g = term[2][countSubject] # g = grade
                s = term[3][countSubject] # s = section
                countSubject += 1
                #write data
                file.writerow({'SubjectID': subj[0],
                               'SubjectName': subj[1],
                               'Weight': w,
                               'Section': s,
                               'Grade': g,
                               'Term': termCount})
            
record = getRecord(sys.argv[1])
showGPA(record)
exportCSV(record)