import contextlib
def find_between(filepath,first_word, second_word, occurrence):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    first_line_number = None
    second_line_number = None
    count = 0

    for i, line in enumerate(lines):
        if first_word in line:
            count += 1
            if count == occurrence:
                first_line_number = i
        if second_word in line and count == occurrence:
            second_line_number = i
            break

    if first_line_number is not None and second_line_number is not None:
        words_between = []
        for i in range(first_line_number + 1, second_line_number):
            line = lines[i].strip()
            words_between.append(lines[i])
        return words_between
    else:
        return []  # If either first_word or second_word is not found in the file or occurrence is not found

def find_between2(code:str,first_word, second_word, occurrence):
    lines = code.strip().split("\n")
    first_line_number = None
    second_line_number = None
    count = 0

    for i, line in enumerate(lines):
        if first_word in line:
            count += 1
            if count == occurrence:
                first_line_number = i
        if second_word in line and count == occurrence:
            second_line_number = i
            break

    if first_line_number is not None and second_line_number is not None:
        words_between = []
        for i in range(first_line_number + 1, second_line_number):
            line = lines[i].strip()
            words_between.append(lines[i])
        return words_between
    else:
        return []  # If either first_word or second_word is not found in the file or occurrence is not found
def find_between2_2(code:str,first_word, second_word, occurrence):
    lines = code.split("\n")
    first_line_number = None
    second_line_number = None
    count = 0

    for i, line in enumerate(lines):
        if first_word in line:
            count += 1
            if count == occurrence:
                first_line_number = i
        if second_word in line and count == occurrence:
            second_line_number = i
            break

    if first_line_number is not None and second_line_number is not None:
        words_between = []
        for i in range(first_line_number + 1, second_line_number):
            line = lines[i].strip()
            words_between.append(lines[i])
        return words_between
    else:
        return []  # If either first_word or second_word is not found in the file or occurrence is not found

def find_between3(text, firstword, secondword):
    start_index = text.find(firstword) + len(firstword)
    end_index = text.find(secondword)
    if start_index == -1 or end_index == -1:
        return None
    return text[start_index:end_index]

def list_to_string(lst):
    string = ''.join(lst)
    return string.replace('\\n', '\n')
def list_to_string2(lst):
    string = '\n'.join(lst)
    return string.replace('\\n', '\n')
class system():
    def __init__(self):
        pass
    def createDB(self,filename:str):
        with contextlib.suppress(FileExistsError):
            open(f'{filename}.TDB', 'x').close()
    def opencontainer(self,filename:str,container:str,containernumber:int):
        try:
            self.read = open(filename,'r')
            self.x = self.read.read()
            self.datalist = self.x.strip().split("\n")
            self.read.close()
            return find_between2(self.x,f'<{container} s data>{containernumber}',f'<{container} e data>{containernumber}',1)
        except FileNotFoundError:
            print('file not found error')
    def amount(self, sub, word):
        return sum(word[i:i+len(sub)] == sub for i in range(len(word)))
    def openall(self,filename:str):
        try:
            self.read = open(filename,'r')
            self.x = self.read.read()
            self.datalist = self.x.strip().split("\n")
            self.read.close()
            self.amountvar = self.amount('data>',self.x)
            self.realamount = self.amountvar / 2
            self.finlist = []
            for i in range(int(self.realamount)):
                i += 1
                self.finlist.append(find_between2(self.x,f's data>{i}',f'e data>{i}',1))
            return self.finlist
        except FileNotFoundError:
            print('file not found error')
TurtleDB = system()