numberOfRequests = int(input())

requests = {}
for _ in range(numberOfRequests):
    request = input().split()
    courseName = request[2]
    studentName = "{} {}".format(request[0], request[1])
    studentNames = requests.get(courseName, set())
    studentNames.add(studentName)
    requests[courseName] = studentNames
    
sortedCourseNames = sorted(requests.items())
for courseName, studentNames in sortedCourseNames:
    numberOfCourseRequests = len(studentNames)
    print("{} {}".format(courseName, numberOfCourseRequests))
