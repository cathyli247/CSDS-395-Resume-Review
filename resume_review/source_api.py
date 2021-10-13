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
        text = texts[1].lower().title()
        t = (text, text)
        result.append(t)
    return result
