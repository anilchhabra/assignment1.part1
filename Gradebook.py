last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]

gradebook = list(zip(subjects,grades))
print(gradebook)

subjects.append("computer science")
grades.append(100)

subjects.append("visual arts")
grades.append(93)

gradebook = list(zip(subjects,grades))
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
