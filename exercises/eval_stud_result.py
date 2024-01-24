from os import strerror, path

class StudentDataValueException(Exception):
    pass

class IncorrectLineException(Exception):
    pass

class EmptyFileException(Exception):
    pass

def getDict(src):
    try:
        file = open(src)
        if not path.getsize(src):
            raise EmptyFileException
    except IOError as e:
        print("Unable to open source file: ", strerror(e.errno))
        exit(e.errno)
    except EmptyFileException:
        print("Empty file")

    result = dict()

    try:
        for line in file.readlines():
            line_arr = line.split(' ')
            if len(line_arr) != 3:
                raise IncorrectLineException
            try:
                value = float(line_arr[2].strip())
            except:
                raise StudentDataValueException
            full_name = line_arr[0] + ' ' + line_arr[1]

            if result.get(full_name):
                result[full_name] = result[full_name] + float(line_arr[2].strip())
                continue

            result[full_name] = float(line_arr[2].strip())
    except IncorrectLineException:
        print("Line does not have correct format of: 'name surname value'")
    except StudentDataValueException:
        print("Error in value of student data, possible data corruption or wrong format (f.e. value is not a number)")

    return result
 
def sortDict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))


src = 'students.txt'
studentGradeDict = getDict(src)
studentGradeDict = sortDict(studentGradeDict)

for k,v in studentGradeDict.items():
    print(str(k) + ' -> ' + str(v))