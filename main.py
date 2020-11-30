def arithmetic_arranger(problems):
    import re

    prvniradek = ''
    druhyradek = ''
    znamenko = ''
    podtrzeni=''
    delka=(len(problems))
    for i in range (delka):
        de1 = 6 - len(re.search("\d*\s", problems[i]).group())
        de2 = 4 - len(re.search("\s\d+", problems[i]).group())
        #print(de1,de2)
        znamenko = re.search("[-|+]", problems[i]).group()
        prvniradek=prvniradek + de1*" " + 3*" " + (re.search("\d*\s", problems[i]).group())
        druhyradek= druhyradek + de2*" " + 3*" " + znamenko +  (re.search("\s\d+", problems[i]).group())
        podtrzeni = podtrzeni + 1*" " +max(de1,de2)*' ' + (max(de1,de2)+2)*'-'
    print(prvniradek + '\n' + druhyradek + '\n' + podtrzeni)
    #return arranged_problems,rada

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
