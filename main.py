def arithmetic_arranger(problems):
    import re
    '''
    prvni = re.search("\d*\s", problems[0]).group()
    znamenko = re.search("[-|+]", problems[0]).group()
    druhy = re.search("\s\d+", problems[0]).group()
    arranged_problems= print(prvni + '\n' + znamenko + druhy + '\n' + '----')
    '''
    prvniradek = ''
    druhyradek = ''
    znamenko = ''
    for i in range (len(problems)):
        znamenko = re.search("[-|+]", problems[i]).group()
        prvniradek=prvniradek + (re.search("\d*\s", problems[i]).group())
        druhyradek= druhyradek + znamenko + (re.search("\s\d+", problems[i]).group())
    print(prvniradek + '\n' + druhyradek)
    #return arranged_problems,rada



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
