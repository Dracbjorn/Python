#!/usr/bin/python
from __future__ import print_function
from subprocess import *
import sys
import re

EXCLUDE_STUDENTS=[1,2,14,20,22]
NUM_QUESTIONS=14
filesString=check_output(['find', './', '-regex', '.*[Ff]inal-[Ee]xam.txt'])
fileList=filesString.split('\n')[0:-1]
numExams=len(fileList)
errors=[]
expectedFileNum = 22 - len(EXCLUDE_STUDENTS)

def gradeExam(ans):
    ansSplit=ans.split('.')
    num=int(ansSplit[0].strip())
    ans=ansSplit[1].strip()
    #print('Question: '+str(num))
    #print('Answer: '+ans)
    if num == 1:
        if ans.find('a') > -1:
            return 4
    elif num == 2:
        if ans.find('g') > -1 and ans.find('h') > -1:
            return 4
        elif ans.find('g') > -1 or ans.find('h') > -1:
            return 2
    elif num == 3:
        if ans.find('a') > -1:
            return 4
    elif num == 4:
        if ans.find('d') > -1:
            return 8
    elif num == 5:
        if ans.find(' h ') > -1:
            return 8
    elif num == 6:
        if ans.find('d') > -1:
            return 8
    elif num == 7:
        if ans.find('h') > -1:
            return 8
    elif num == 8:
        if ans.find('e') > -1:
            return 8
    elif num == 9:
        if ans.find('j') > -1:
            return 8
    elif num == 10:
        if ans.find('h') > -1:
            return 8
    elif num == 11:
        if ans.find('j') > -1:
            return 8
    elif num == 12:
        if ans.find('b') > -1:
            return 8
    elif num == 13:
        if ans.find('j') > -1:
            return 8
    elif num == 14:

        score=0
        if ans.find('a') > -1:
            score -= 2
        if ans.find('d') > -1:
            score -= 2
        if ans.find('e') > -1:
            score -= 2
        if ans.find('g') > -1:
            score -= 2
        if ans.find('h') > -1:
            score -= 2

        if ans.find('b') > -1 and ans.find('c') > -1 and ans.find('f') > -1:
            return score + 8
        elif ans.find('b') > -1 and (ans.find('c') > -1 or ans.find('f') > -1):
            return score + 6
        elif ans.find('c') > -1 and (ans.find('f') > -1 or ans.find('b') > -1):
            return score + 6
        elif ans.find('f') > -1 and (ans.find('c') > -1 or ans.find('b') > -1):
            return score + 6
        elif ans.find('f') > -1 or ans.find('c') > -1 or ans.find('b') > -1:
            return score + 3
    else:
        print(str(num)+" is not a valid number")

    return 0

if not len(fileList) == expectedFileNum:
    errors.append('Student files are missing!')

num=0
for i in fileList:
    for j in EXCLUDE_STUDENTS:
        pattern=re.compile('\.\/[Ss]tudent'+str(j)+'\/')
        if re.match(pattern,i):
            print("Removing: "+i)
            fileList.remove(fileList[num])
    num += 1

studentDict={}
for stuNum in range(1,23):
    exclude=False
    for i in EXCLUDE_STUDENTS:
        if stuNum == i:
            exclude=True
            break
        else:
            exclude=False
            continue
    if not exclude:
        studentDict['student'+str(stuNum)]=[]
    else:
        continue

print(str(numExams)+" exams being processed...")
for exam in fileList:
    try:
        num=int(exam.split('/')[1][7:])
    except:
        print('ERROR: Invalid directory name '+exam)
        sys.exit()
    #print('student'+str(num)+' file:'+exam) 
    exam=open(exam)
    contents=exam.readlines()
    exam.close()
    for line in contents:
        pattern=re.compile('[0-9]{1,2}.*[a-zA-Z].*')
        if re.match(pattern,line):
            
            studentDict['student'+str(num)].append(line)

for student in studentDict:
    numQuestions=len(studentDict[student])
    if (numQuestions == 0):
        errors.append('INVESTIGATE: '+student+' exam does not exist!')
        continue
    elif (numQuestions < NUM_QUESTIONS):
        errors.append('MANUALLY GRADE: '+student+' does not have '+str(NUM_QUESTIONS)+' questions!')
    print(student+':')
    score=0
    for question in studentDict[student]:
        question=question.strip()
        result=gradeExam(question.lower())
        score += result
        print(question+' score = '+str(result))
    print('\t'+str(numQuestions)+' questions')
    print('\tTotal score: '+str(score))
   
print('\nThe following errors were encountered:\n')
for i in errors:
    print(i)
