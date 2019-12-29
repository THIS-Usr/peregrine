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


# read_files(path)


listOfFiles = os.listdir(path)
pattern = "*"


# for entry in listOfFiles:
#     if fnmatch.fnmatch(entry, pattern):
#             print (entry)

# detect the current working directory
# path = os.getcwd()

def extract_message_firstline(rfh, wfh):
    x = 0
    for line in rfh:
        if not line.startswith(' > '):
            line0 = line
            next
        else:
            if x < 1:
                array1 = line0.split(',')
                timestamp = array1[0].split('On ')[1]
                name = array1[1].split(' wrote:')[0]
                wfh.write(timestamp)
                wfh.write(name)
                x += 1
            line = line.split(' > ')[1]
            wfh.writelines('\n      ' + line)
    rfh.close()
    wfh.close()

import re

p = re.compile('[.]*[>]+')
p1 = re.compile('[\s]*[\n]+') # clean line break
p2 = re.compile('[\s]*[On]')
p3 = re.compile('text-02')
p4 = re.compile('[\s]*[>]+[\n]+') # dirty line break




line_match = '>\n'#'   >>>> some text here with a tag here <open / >'
# m = p3.search(line_match) # first occurance should be what's needed
# all = p3.findall(line_match)
# m = p4.match(line_match)
# print(m)
# print(m.group())
# print(m.span())
# Let's find the deapest level

# line_match1 = "> It's so odd that RDF is entirely about relations just as CT is ( except that RDF is one to many whereas CT arrows are functions). So I really look forward to understanding how these two domains fit together, and perhaps how they complement each other.\nNew line"

line_match1 = "   \n >\n > So if this still needs to be proven\n"
# print(line_match1)
# m = p1.search(line_match1)
# print("before group")
# print(m.group())
# print("after group")


file_dict = {}  # Create an empty dict


# def deapest_quotation_level():
#     depth = 0
#     matched_line = ''
#     previous_line = ''
#     previous_previous_line = ''
#     full_depth = 0
#     with os.scandir(path) as listOfEntries:
#         for entry in listOfEntries:
#             # in each file find line at matched term greatest depth
#             if entry.is_file():
#                 # print(entry.name)
#                 rwfh = open(entry, 'r+')
#                 lines = rwfh.readlines()
#                 for line in lines:
#                     if p.match(line):
#                         m = p.match(line)
#                         span = m.span()[1] - m.span()[0]
#                         if depth == span-1:
#                             previous_previous_line = line
#                         if depth == span:
#                             previous_line = line
#                             continue
#                         elif span > depth:
#                             depth = span
#                             full_depth = depth
#                             matched_line = line
#                 # for line in lines:
#                 #     if depth == full_depth - 1:
#                 #         print(depth)
#                 #         print(full_depth)
#                 #         print(line)
#                 # TBD
#                 # At the moment this is picking out the last occurance in the file - good, but we also want the first
#                 # print(previous_previous_line)
#                 # print(previous_line)
#                 file_dict[entry.name] = (depth, matched_line)
#                 line_array = matched_line.split(",")
#                 new_line = line_array[0].split("On ")[1]
#                 new_line = new_line + ":" + line_array[1].split(" at ")[1]
#                 new_line = line_array[2].split(" <")[0] + " " + line_array[3].split("<")[0].lstrip(" ") + "" + new_line
#                 new_line = new_line.lstrip(" ")
#                 email = line_array[3].split("<")[1]
#                 email = email.split(">")[0]
#                 print(new_line)
#                 print(email)


def __extract(entry):
    depth = 0
    span = 0
    matched_line = ''
    last_line = ''
    next_last_line = ''
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
                print(line_array[0])
                formatted_line = line_array[0].split("On ")[1]
                formatted_line = formatted_line + ":" + line_array[1].split(" at ")[1]
                formatted_line = line_array[2].split(" <")[0] + " " + line_array[len(line_array) - 1].split("<")[
                    0].lstrip(" ") + "" + formatted_line
                formatted_line = formatted_line.lstrip(" ")
                email = line_array[len(line_array) - 1].split("<")[1]
                email = email.split(">")[0]
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


# def deepest_quotation_level():
#     depth = 0
#     span = 0
#     matched_line = ''
#     last_line = ''
#     next_last_line = ''
#     formatted_line = ''
#     email = ''
#     full_depth = 0
#     line_enumeration = None
#     with os.scandir(path) as listOfEntries:
#         for entry in listOfEntries:
#             # in each file find line at matched term greatest depth
#             line_enumeration = __create_line_enumeration(entry)
#             # lines = __create_lines_list(entry)
#             # print(line_enumeration)
#             if line_enumeration == None:
#                 continue
#             for linenum, line in line_enumeration:
#                 if depth == span:
#                     next_last_line = (line, linenum)
#                 if p.match(line):
#                     m = p.match(line)
#                     span = m.span()[1] - m.span()[0]
#                     if depth == span:
#                         last_line = (line, linenum)
#                         continue
#                     elif span > depth:
#                         depth = span
#                         # full_depth = depth
#                         matched_line = (line, linenum) # removed from here
#                     line_array = matched_line[0].split(",")
#                     # line_array[0] = line_array[0].lstrip(" ")
#                     # print(line_array[0])
#                     if p2.match(line_array[0]):
#                         formatted_line = line_array[0].split("On ")[1]
#                         formatted_line = formatted_line + ":" + line_array[1].split(" at ")[1]
#                         formatted_line = line_array[2].split(" <")[0] + " " + line_array[len(line_array) - 1].split("<")[
#                             0].lstrip(" ") + "" + formatted_line
#                         formatted_line = formatted_line.lstrip(" ")
#                         email = line_array[len(line_array) - 1].split("<")[1]
#                         email = email.split(">")[0]
#                 file_dict[entry.name] = (depth, next_last_line, last_line, matched_line)
#                         # lines.insert(matched_line[1], formatted_line)
#                         # __modify_lines(file_dict, entry, formatted_line, email, line_enumeration)
#             try:
#                 file_dict[entry.name]
#                 __modify_lines(file_dict, entry, formatted_line, email, line_enumeration) # can't be for each line
#             except KeyError as ke:
#                 print(ke)
#
#                 # print(entry.name)
#                 # print(file_dict[entry.name])
#                 # print(formatted_line)
#                 # print(email)

## read the entries
# test-text-01.txt
def extract_first_line_level_one():
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            # print all entries that are files
            if entry.is_file():
                # print(entry.name)
                if p3.search(entry.name):
                    print(entry.name)
                    # rfh = open(entry, 'r')
                    # wfh = open(path1 + entry.name, 'w')
                    # extract_message_firstline(rfh, wfh)
                    # print(rfh.readline())
                    __extract(entry)

extract_first_line_level_one() #TODO

# for k in file_dict:
#     print(k + ": depth: " + str(file_dict[k]))


# ext = '.txt' # Select your file delimiter

# file_dict = {} # Create an empty dict

# Select only files with the ext extension
# txt_files = [i for i in os.listdir(path1) if os.path.splitext(i)[1] == ext]

# print(p)

# TODO
# Iterate over your txt files
# with os.scandir(path) as listOfEntries:
#     for entry in listOfEntries:
#         # Open them and assign them to file_dict
#         if entry.is_file():
#             with open(os.path.join(path,entry)) as file_object:
#                 # file_dict[entry] = file_object.read()
#                 lines = file_object.readlines()
#                 # print(lines)
#                 for line in lines:
#                     if p.match(line):
#                         m = p.match(line)
#                         position = m.span(m.group())
#                         print(m)

# Iterate over your dict and print the key/val pairs.

def __level():
    depth = 0
    span = 0
    matched_line = ''
    last_line = ''
    next_last_line = ''
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            # in each file find line at matched term greatest depth
            line_enumeration = __create_line_enumeration(entry)
            lines = __create_lines_list(entry)
            lines_index = 0
            if line_enumeration == None:
                break
            for linenum, line in (line_enumeration):
                # print(line_enumeration[linenum][0])
                # line = line_enumeration[linenum][1]
                if p.match(line):
                    m = p.match(line)
                    span = m.span()[1] - m.span()[0]
                    line = line.lstrip(m.group())
                    if depth == span:
                        last_line = (line, linenum)
                        continue
                    elif span > depth:
                        depth = span
                        # full_depth = depth
                        matched_line = (line, linenum)
                    if not p1.match(line):
                        line = " " * span * 2 + line
                    print("line after match")
                    print(line)
                    lines[linenum] = line  # change the line
                    print("line in enumeration")
                    print(line_enumeration[linenum])
                    print("line in lines")
                    print(lines[linenum])
                    print(matched_line)
                    line_array = matched_line[0].split(",")
                    line_array[0] = line_array[0].lstrip(" ")
                    print(line_array)
                    if line_array[0].startswith("On "):
                        formatted_line = line_array[0].split("On ")[1]
                        formatted_line = formatted_line + ":" + line_array[1].split(" at ")[1]
                        formatted_line = line_array[2].split(" <")[0] + " " + line_array[len(line_array)-1].split("<")[0].lstrip(" ") + "" + formatted_line
                        formatted_line = formatted_line.lstrip(" ")
                        email = line_array[len(line_array)-1].split("<")[1]
                        email = email.split(">")[0]
                        lines.insert(matched_line[1], formatted_line)
            # print(len(lines))
            # print(len(line_enumeration))
            # print(lines)
            # if matched_line[1]-2 >= 1:
            #     print(lines[matched_line[1]-2])
            # if matched_line[1] - 1 >= 1:
            #     print(lines[matched_line[1]-1])
            # if matched_line[1] - 1 >= 1:
            #     print(lines[matched_line[1]])
            # print(lines[matched_line[1]+1])

# TODO
# deepest_quotation_level()
# __level()


# for i in file_dict:
#     lines = i.readlines()
#     for line in lines:
#         if p.match(line):
#             m = p.match(line)
#             position = m.span(m.group())
#             print(m)


# print("line in enumeration - 1")
# print(line_enumeration[linenum-1])
# print("line in lines - 1")
# print(lines[linenum - 1])
# print("line in enumeration after insertion")
# print(line_enumeration[linenum][1])
# print("line in lines after insertion")
# lines.insert(linenum, "line in lines after insertion")
# print(lines[linenum])
# print("line in enumeration previous to insertion - 2")
# print(line_enumeration[linenum - 2])
# print("line in lines previous to insertion - 2")
# print(lines[linenum - 2])
# print("line in enumeration previous to insertion - 1")
# print(line_enumeration[linenum - 1])
# print("line in lines previous to insertion - 1")
# print(lines[linenum - 1])
# print("line in enumeration")
# print(line_enumeration[linenum])
# print("line in lines")
# print(lines[linenum])
# ====
