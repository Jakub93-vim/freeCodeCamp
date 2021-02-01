def arithmetic_arranger_2(problems, result=True):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        if "+" in problem or "-" in problem:
            pass
        else:
            return 'Error: Operator must be + or -.'

    for example_nr in range(len(problems)):#priradi do promene problem poradove cislo prikladu
        for each_nr in problems[example_nr]:#projde vsechny prvky z kazdeho prikladu
            if each_nr.isdigit()== True or each_nr == "+" \
                or each_nr == "-" or each_nr == " ":#overi jestli obsahuje pouze povolene znaky a cislice
                pass
            else:
                return 'Error: Numbers must only contain digits.'

    for example_nr in range(len(problems)):#priradi do promene problem poradove cislo prikladu
        dig_count = 0
        for each_nr in problems[example_nr]:#projde vsechny prvky z kazdeho prikladu
            if each_nr.isdigit() == True:#pokud najde digid pricte k dig_count jedna
                dig_count += 1
                if dig_count > 4:
                    return 'Error: Numbers cannot be more than four digits.'
            else:
                dig_count = 0

#-------- zobrazeni rovnice ----------------

    #vytvori listy v listu pouze s cisly
    pro_list = []
    problems_poc = problems.copy()#kopirovani problems,aby se neovlivnila promena dale v kodu
    for elem in range(len(problems_poc)):#vytvori list v tomto formatu [['32', '8'], ['1', '3801'], ['9999', '9999'], ['523', '49']]
        if "+" in problems_poc[elem]:
            problems_poc[elem] = problems_poc[elem].split(" + ")#pokud narazi na plus, tak rozdeli string v listu
            pro_list.append(problems_poc[elem])#prida rozdelenou cast do listu pro_list
        if "-" in problems_poc[elem]:
            problems_poc[elem] = problems_poc[elem].split(" - ")
            pro_list.append(problems_poc[elem])

    def longer(ls_ele):#funkce vyhodnocujici ktery z prvku pro listu je delsi a vrati hodnotu delky
        print(ls_ele[0],ls_ele[1], 'uvnitr funkce')
        if ls_ele[0] > ls_ele[1]:
            return len(ls_ele[0])
        if ls_ele[0] < ls_ele[1]:
            return len(ls_ele[1])
        if ls_ele[0] == ls_ele[1]:
            return len(ls_ele[0])

    print(pro_list[0])

    #vytvori list mezer
    frs_space = []
    sec_space = []
    underline = ''#retezec s podtrzenim pod cisly
    for elem in range(len(pro_list)):#vytvori list s mezerama pro prvni a druhou radku
        print(pro_list[elem])
        print(longer(pro_list[elem]))
        underline += longer(pro_list[elem])*'-' + '--'
        underline += '    '
        print(underline)
        diff = abs(len(pro_list[elem][0])-len(pro_list[elem][1]))#rozdil delky prvku v jednotlivych elementech
        if len(pro_list[elem][0]) > len(pro_list[elem][1]):#pokud jeden prvek delsi prida mezeru do druheho space listu
            sec_space.append(diff * " ")
        else:
            sec_space.append("")
        if len(pro_list[elem][0]) < len(pro_list[elem][1]):
            frs_space.append(diff * " ")
        else:
            frs_space.append("")
    print(underline)


    frs_line = ''#vyvtoreni prvniho radku
    for example_nr in range(len(problems)):#priradi do promene problem poradove cislo prikladu
        frs_line += "  " #prida dve mezery pred prvni radek u kazdeho prvku - kompenzace znamenka
        frs_line += frs_space[example_nr]
        for each_nr in problems[example_nr]:#projde vsechny prvky z kazdeho prikladu
            frs_line += each_nr
            if each_nr == " ":
                frs_line += "   "
                break
    print(frs_line)

    sec_line = ''#vytvoreni druheho radku
    for example_nr in range(len(problems)):  # priradi do promene problem poradove cislo prikladu
        space_count = 0
        if example_nr >= 1:# za prvnim a dalsim cislem udela mezeru
            sec_line += "    "
        sec_line += sec_space[example_nr]
        for each_nr in problems[example_nr]:  # projde vsechny prvky z kazdeho prikladu
            if each_nr == "+":#pokud nalezne znamenko, prida ho pred cisla
                sec_line += "+ "
            if each_nr == "-":
                sec_line += "- "
            if each_nr == " ":# pokud nalezne dve mezery tak prida cisla do sec_line
                space_count += 1
            elif space_count == 2:
                sec_line += each_nr
    print(sec_line)

#vzorova rovnice
'''
  32         1      9999      523
 + 8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
'''




print(arithmetic_arranger_2(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))