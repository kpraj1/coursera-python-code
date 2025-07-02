with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    testwritefile.seek(0, 0)
    data = testwritefile.read()
    if not data:  # empty strings return false in python
        print('Read nothing')
    else:
        print(data)
        testwritefile.write("This is new information\n")
        testwritefile.seek(0, 0)  # move 0 bytes from beginning.
        print("\nNew Location : {}".format(testwritefile.tell()))
        new_data = testwritefile.read()
        if not new_data:
            print('Read nothing')
        else:
            print(new_data)

        print("Location after read: {}".format(testwritefile.tell()))
