def airportGate(arrival,dep):
    arrival = sorted(arrival)
    dep = sorted(dep)

    minNoOfGates = 1
    final_res = 1
    i = 1
    j = 0

    while (i < len(arrival)) and (j < len(arrival)):

        if arrival[i] < dep[j]:
            minNoOfGates += 1
            i += 1
            if minNoOfGates > final_res:
                final_res = minNoOfGates
        else:
            minNoOfGates -= 1
            j += 1

    return final_res

arrival = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
#arrival = [570, 675, 990]
#dep = [705, 690, 1005]

print (airportGate(arrival,dep))
