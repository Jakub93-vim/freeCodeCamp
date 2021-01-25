def arithmetic_arranger(problems):
    import re

    prvniradek = ''
    druhyradek = ''
    znamenko = ''
    podtrzeni= ''
    delka=(len(problems))

    #zjisteni delky cisla v listu (delkacisla)
    delkacis=len(max([re.search('(\d+)\s', x).group(1) for x in problems if re.search(r'(\d)*\s', x)], key=len))


    #overeni pritomnosti znamenka
    znam= True
    for i in range(delka):
        znamenko = re.search("\s.\s", problems[i]).group()
        if znamenko == "+" or "-":
            znam= True
        else:
            znam= False

    #overeni jestli jsou vsechny prvky cislice
    def over(list):
        str=""
        dig=False
        for ele in list:
            str+=ele
        for ele in str:
            if re.search('\d|\s|\+|\-',ele):
                dig=True
            else:
                dig=False
                break
        return dig

    #overeni vsech podminek

    if delka>4:
        print('Error: Too many problems.')
    elif delkacis>4:
        print('Error: Numbers cannot be more than four digits.')
    elif znam == False:
        print('Error: Operator must be + or -.')
    elif over(problems)==False:
        print('Error: Numbers must only contain digits.')
    else:
        pass

    for i in range (delka):
        de1 = 6 - (len(re.search("\d*\s", problems[i]).group())-1)
        de2 = 4 - (len(re.search("\s\d+", problems[i]).group())-1)
        pod1 = len(re.search("\d*\s", problems[i]).group())
        pod2 = len(re.search("\s\d+", problems[i]).group())+2
        #print(de1,de2)
        znamenko = re.search("[-|+]", problems[i]).group()
        prvniradek = prvniradek + de1*" " + 2*" " + (re.search("\d*", problems[i]).group())
        druhyradek = druhyradek + de2*" " + 2*" " + znamenko + (re.search("\s\d+", problems[i]).group())
        podtrzeni = podtrzeni + 4*' ' + (max(pod1,pod2)-1)*'-'
    print(prvniradek + '\n' + druhyradek + '\n' + podtrzeni)
    #return (prvniradek + '\n' + druhyradek + '\n' + podtrzeni)
    return delka

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
