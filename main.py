def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
        return result
students = [[1, 'Jean Castro', 'V'], [2, 'Lulla Powell', 'V'], [3, 'Brian Howell', 'VI'],[4,'Lyne Foster', 'VI'],[5, 'Zachary Simon','VII']]

print("/nOriginal list of lists:")
print(students)
print("/nConverted liststo a dictionary:")
print(test(students))