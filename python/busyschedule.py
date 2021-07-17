def printAppointment(appointments, period):
    for hours, minutes in appointments:
        print("{}:{} {}".format(hours, minutes, period))


isFirstTest = True
while True:
    numberOfAppointments = int(input())
    if numberOfAppointments == 0:
        break

    if isFirstTest:
        isFirstTest = False
    else:
        print("")

    midnightAppointments = []
    morningAppointments = []
    middayAppointments = []
    eveningAppointments = []
    for _ in range(numberOfAppointments):
        time, period = input().split()
        hours, minutes = time.split(":")
        if period == "a.m.":
            if hours == "12":
                midnightAppointments.append((hours, minutes))
            else:
                morningAppointments.append((hours, minutes))
        else: # p.m.
            if hours == "12":
                middayAppointments.append((hours, minutes))
            else:
                eveningAppointments.append((hours, minutes))

    midnightAppointments.sort(key = lambda appointment: (int(appointment[0]), int(appointment[1])))
    morningAppointments.sort(key = lambda appointment: (int(appointment[0]), int(appointment[1])))
    middayAppointments.sort(key = lambda appointment: (int(appointment[0]), int(appointment[1])))
    eveningAppointments.sort(key = lambda appointment: (int(appointment[0]), int(appointment[1])))

    printAppointment(midnightAppointments, "a.m.")
    printAppointment(morningAppointments, "a.m.")
    printAppointment(middayAppointments, "p.m.")
    printAppointment(eveningAppointments, "p.m.")
