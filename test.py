s = '/usr/local/bin/python'
l = s.split("/")

for i in l[1:]:
    print("'{0}'".format(i), end=" ")

print(" ")
