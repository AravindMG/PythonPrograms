ipAddress = input("Please enter an Ip Address: ")

segment = 0
segmentLength = 0
character = ''
for character in ipAddress:
    if character == '.':
        print("Segment {} has {} characters".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1
if character != '.':
    print("segment {} has {} characters".format(segment, segmentLength))

if character == '':
    print("Please enter something")
