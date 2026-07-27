stew = int(input("How many students on the course?"))
group = int(input("Desired group size?"))
cool = stew // group
cool3 = (stew + group - 1) // group
print("Number of groups formed:", cool3)
