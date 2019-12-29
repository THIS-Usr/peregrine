import os

directory_path = "/Volumes/LaCie/Documents CC Schedule/bbedit/Semantic Web/"
document_texts = "document-texts/texts-extract-01"
panels = "/panels"

# files
file1 = "1.9.2018-19-52-01.gmt.txt"
file2 = "panel-01-19-52-01.gmt.txt"

rfh=open(directory_path+document_texts+file1)


wfh=open(directory_path+document_texts+panels+file2,mode="w",encoding="utf-8")

# On 9/1/18 5:46 AM, Henry Story wrote:
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
        wfh.writelines('\n      '+line)
rfh.close()
wfh.close()


wfh=open(directory_path+document_texts+panels+file2,mode="r",encoding="utf-8")

# line_array = wfh.readlines()
# print(line_array)
print(wfh.read())


def read_files():
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)