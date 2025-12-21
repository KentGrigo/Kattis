def orderPreservingDifference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference = set1.difference(set2)
    result = []
    for element in list1:
        if element in difference:
            result.append(element)

    return result


_ = input()
studentsAttendingMonday = list(input().split())
studentsAttendingTuesday = list(input().split())
studentsOnlyAttendingMonday = orderPreservingDifference(studentsAttendingMonday, studentsAttendingTuesday)
studentsOnlyAttendingTuesday = orderPreservingDifference(studentsAttendingTuesday, studentsAttendingMonday)
studentsOnlyAttendingMondayFormatted = ' '.join(studentsOnlyAttendingMonday)
studentsOnlyAttendingTuesdayFormatted = ' '.join(studentsOnlyAttendingTuesday)
print(studentsOnlyAttendingMondayFormatted)
print(studentsOnlyAttendingTuesdayFormatted)
