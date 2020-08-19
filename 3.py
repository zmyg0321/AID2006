def find_word(word):
    """
    :param word: 要查询的单词
    :return: 查询结果
    """
    file = open("dict.txt")
    for line in file:
        # 每次获取一行，分割单词和解释
        tmp = line.split(" ", 1)
        if tmp[0] > word:
            break
        if word == tmp[0]:
            return tmp[1].strip()

    file.close()


print("%s : %s" % ("abc", find_word("abc")))
