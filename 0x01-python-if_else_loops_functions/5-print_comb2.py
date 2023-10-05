#!/usr/bin/python3
#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print("{:02}".format(number), end=", ")
    else:
        print("{}".format(number), end=", ")
print()
