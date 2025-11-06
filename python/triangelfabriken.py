angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
maxAngle = max(angle1, angle2, angle3)
if maxAngle < 90:
    print('Spetsig Triangel')
elif maxAngle == 90:
    print('Ratvinklig Triangel')
else:
    print('Trubbig Triangel')
