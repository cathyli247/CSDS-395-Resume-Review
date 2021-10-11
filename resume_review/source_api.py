def get_major_list():
    '''
    get the major list
    :return: list
    '''
    file1 = open('major.txt', 'r')
    lines = file1.readlines()

    result = []
    for line in lines:
        texts = str(line).split('     ')
        texts[1] = texts[1].replace('\n', '')
        t = (texts[0], texts[1].lower())
        result.append(t)
    return result
