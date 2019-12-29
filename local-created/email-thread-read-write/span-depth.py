import os, fnmatch

# /Volumes/LaCie/Documents CC Schedule/bbedit/Semantic Web/document-texts/texts-extract-01

directory_path = "/Volumes/LaCie/Documents CC Schedule/bbedit/Semantic Web/"
document_texts = "document-texts/texts-extract-01"  # copies of originals
panels = "/panels"

# files
file1 = "1.9.2018-19-52-01.gmt.txt"
file2 = "panel-01-19-52-01.gmt.txt"

path = directory_path + document_texts + panels
path1 = path + panels


def read_files(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            print(filename)




import re

p = re.compile('[.]*[>]+')
p1 = re.compile('[\s]*[\n]+') # clean line break
p2 = re.compile('[\s]*[On]')
p3 = re.compile('text-01')
p4 = re.compile('[\s]*[>]+[\n]+') # dirty line break
p5 = re.compile('[\s]*[>]+')


test = False

test_lines = True

if test_lines:
    line_match = ' >> On 4 Sep 2018' #'>\n'#'   >>>> some text here with a tag here <open / >'
    m = p5.match(line_match)
    # m = p3.search(line_match) # first occurance should be what's needed
    # all = p3.findall(line_match)
    # m = p4.match(line_match)
    print("test 1")
    print(m)
    print(m.group())
    print(m.span())


    line_match = ">>> On 9/2/18 6:04 AM, Henry Story wrote:"
    m = p5.match(line_match)
    print("test 2")
    print(m)
    print(m.group())
    print(m.span())

    line_match = ">>>> I changed the title to emphasize the new importance of modal"
    m = p5.match(line_match)
    print("test 3")
    print(m)
    print(m.group())
    print(m.span())

    line_match = ">>>> logic in the discussion in this thread."
    m = p5.match(line_match)
    print("test 4")
    print(m)
    print(m.group())
    print(m.span())

    line_match = "        >>>>> my test line one."
    m = p5.match(line_match)
    print("test 5")
    print(m)
    print(m.group())
    print(m.span())

    # This one
    line_match = "        >>>>> my test line two."
    m = p5.match(line_match.lstrip())
    print("test 6")
    print(m)
    print(m.group())
    print(m.span())
    print(m.span()[1]-m.span()[0])

# Let's find the deapest level

# line_match1 = "> It's so odd that RDF is entirely about relations just as CT is ( except that RDF is one to many whereas CT arrows are functions). So I really look forward to understanding how these two domains fit together, and perhaps how they complement each other.\nNew line"

line_match1 = "   \n >\n > So if this still needs to be proven\n"
# print(line_match1)
# m = p1.search(line_match1)
# print("before group")
# print(m.group())
# print("after group")


file_dict = {}  # Create an empty dict


def __deepest_quotation_level(entry):
    depth = 0
    span = 0
    matched_line = ''
    last_line = ''
    next_last_line = ''
    extracted_line = ''
    formatted_line = ''
    email = ''
    full_depth = 0
    line_enumeration = __create_line_enumeration(entry)
    # lines = __create_lines_list(entry)
    # print(line_enumeration)
    if line_enumeration == None:
        return
    for linenum, line in line_enumeration:
        # print(line)
        if depth == span:
            next_last_line = (line, linenum)
        if p.match(line):
            m = p.match(line)
            span = m.span()[1] - m.span()[0]
            if depth == span:
                # print(last_line)
                last_line = (line, linenum)
                continue
            elif span > depth:
                depth = span
                # full_depth = depth
                matched_line = (line, linenum)  # removed from here
            line_array = matched_line[0].split(",")
            # line_array[0] = line_array[0].lstrip(" ")
            if p2.search(line_array[0]): # p2 *search* ...On
                # print(line_array[0])
                m = p2.search(line_array[0])
                if p5.match(line_array[0]):
                    # print(m.group())
                    extracted_line = line_array[0]#.split(m.group())[1]
                    print(extracted_line.split(m.group())[0])
                    try:
                        if extracted_line.index("On "):
                            extracted_line = extracted_line.split("On ")[1]
                            print(extracted_line)
                            formatted_line = extracted_line #.split("On ")[1]
                            formatted_line = formatted_line + ":" + line_array[1].split(" at ")[1]
                            formatted_line = line_array[2].split(" <")[0] + " " + line_array[len(line_array) - 1].split("<")[
                                0].lstrip(" ") + "" + formatted_line
                            formatted_line = formatted_line.lstrip(" ")
                            email = line_array[len(line_array) - 1].split("<")[1]
                            email = email.split(">")[0]
                    except ValueError as e:
                        print(e)
        # print("last last line:")
        # print(last_line)
        file_dict[entry.name] = (depth, next_last_line, last_line, matched_line)
        # print(file_dict)
        # lines.insert(matched_line[1], formatted_line)
        # __modify_lines(file_dict, entry, formatted_line, email, line_enumeration)
    try:
        # file_dict[entry.name]
        __modify_lines(file_dict, entry, formatted_line, email, line_enumeration)  # can't be for each line
    except KeyError as ke:
        print(ke)

def __create_line_enumeration(entry):
    # in each file find line at matched term greatest depth
    if entry.is_file():
        # print(entry.name)
        rwfh = open(entry, 'r')
        lines = rwfh.readlines()
        rwfh.close()
        return enumerate(lines)


def __create_lines_list(entry):
    # in each file find line at matched term greatest depth
    if entry.is_file():
        # print(entry.name)
        rwfh = open(entry, 'r')
        return rwfh.readlines()

# line_enumeration not used
# cleans all dirty lines
# does not clean multile clean (empty) lines
# span ?
def __modify_lines(file_dict, entry, formatted_line, email, line_enumeration):
    line_number = 0
    span = 0
    rwfh = open(entry, 'r')
    lines = rwfh.readlines()
    block = False
    for line in lines:
        if line_number == file_dict[entry.name][3][1]:
            begin_block = "Begin: line " + str(line_number + 1) # + "/n"
            print(begin_block)  # line number
            # print("TODO seems to be blank -- need email too") # OK
            print(formatted_line)  # reformatted line DONE TODO seems to be blank -- need email too OK
            # line_enumeration[line_number] = begin_block
            lines.insert(line_number, begin_block)
            lines.insert(line_number + 1, formatted_line)
            print(lines[line_number]) # OK
            block = True
            line_number += 1
            continue
        if block: #p 1-many >
            if p.match(line):
                m = p.match(line)
                span = m.span()[1] - m.span()[0]
                clean_line = line.lstrip(m.group())
                if not p1.match(clean_line): # p1 0 - many space + \n
                    clean_line = " " * span * 2 + clean_line
                    lines.remove(line)
                    lines.insert(line_number, clean_line)
        if line_number == file_dict[entry.name][2][1]:
            end_block = "End: " + email + ", line " + str(line_number + 1) # + "/n"
            print(end_block)
            lines.insert(line_number, end_block)
            line_number += 1
            break
        line_number += 1
    # previous_line = None # ?
    # previous_line1 = None # ?
    count = 0 # ?
    break_number = 1
    line_number = 0
    # number = 0 # ?
    for line in lines: # TODO 1. multiple blank lines OK -- 2. indentation -- 3. ascribe
        # print(line)
        if p1.match(line):
            line_number += 1
            continue
        if p4.match(line): # dirty line break
            clean_lines = __clean_lines(lines)
    for line in clean_lines:
        print(line)
    # rwfh.writelines(lines)
    rwfh.close()

def __clean_lines(lines):
    break_number = 1
    line_number = 0
    clean_line1 = "\n"  # line.lstrip(m.group())
    # print(break_number)
    for line in lines:
        if break_number == 1:
            # print("p0")
            # print(line_number)
            lines.pop(line_number)
            lines.insert(line_number, clean_line1)
            # number = line_number # ?
            break_number += 1
            line_number += 1
            continue
        if p4.match(line):
            # print("p1")
            # print(line_number)
            lines.pop(line_number)
        if len(lines) > line_number + 1:
            if p4.match(lines[line_number + 1]):
                # print("p2")
                # print("match")
                # print(lines[line_number - 1])
                lines.pop(line_number + 1)
                if p4.match(lines[line_number + 2]):
                    lines.pop(line_number + 2)
                    if p4.match(lines[line_number + 3]):
                        lines.pop(line_number + 3)
                        line_number += 1
                        continue
                    else:
                        line_number += 1
                        continue
                else:
                    line_number += 1
                    continue
            else:
                line_number += 1
                continue
        line_number += 1
    return lines




def __create_quoted_block(entry):
    # in each file find line at matched term greatest depth
    if entry.is_file():
        # print(entry.name)
        rwfh = open(entry, 'r')
        lines = rwfh.readlines()
        rwfh.close()
        return list(enumerate(lines))

## read the entries
# test-text-01.txt or test-text-02.txt
def extract_first_line_level_one():
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            # print all entries that are files
            if entry.is_file():
                # print(entry.name)
                if p3.search(entry.name): # filter: chose which file or all
                    print(entry.name)
                    # rfh = open(entry, 'r')
                    # wfh = open(path1 + entry.name, 'w')
                    # extract_message_firstline(rfh, wfh)
                    # print(rfh.readline())
                    __deepest_quotation_level(entry)
if test:
    extract_first_line_level_one() #TODO

