#Question Link: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=false&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
Length_AB = int(input())
Length_BC = int(input())

from math import sqrt, pow, acos, pi, degrees

Length_AC = sqrt(pow(Length_AB, 2) + pow(Length_BC, 2))

Length_AM, Length_MC = float(Length_AC/2), float(Length_AC/2)

Length_BM = sqrt(abs(pow(Length_BC, 2) - pow(Length_MC, 2)))
Length_BM = sqrt((2 * pow(Length_AB, 2) + 2 * pow(Length_BC, 2) - pow(Length_AC, 2))/4)

angle = acos((pow(Length_BM, 2) + pow(Length_BC, 2) - pow(Length_MC, 2))/(2 * Length_BM * Length_BC))

angle_In_Degree = degrees(angle)

print(str(round(angle_In_Degree)) + u"\N{DEGREE SIGN}")
