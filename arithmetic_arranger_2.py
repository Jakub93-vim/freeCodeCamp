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

    pro_list = []
    problems_poc = problems.copy()#kopirovani problems,aby se neovlivnila promena dale v kodu
    for elem in range(len(problems_poc)):#vytvori list v tomto formatu [['32', '8'], ['1', '3801'], ['9999', '9999'], ['523', '49']]
        if "+" in problems_poc[elem]:
            problems_poc[elem] = problems_poc[elem].split(" + ")#pokud narazi na plus, tak rozdeli string v listu
            pro_list.append(problems_poc[elem])#prida rozdelenou cast do listu pro_list
        if "-" in problems_poc[elem]:
            problems_poc[elem] = problems_poc[elem].split(" - ")
            pro_list.append(problems_poc[elem])
    print(pro_list)

    frs_line = ''
    for example_nr in range(len(problems)):#priradi do promene problem poradove cislo prikladu
        frs_line += "  " #prida dve mezery pred prvni radek
        for each_nr in problems[example_nr]:#projde vsechny prvky z kazdeho prikladu
            frs_line += each_nr
            if each_nr == " ":
                frs_line += "    "
                break
    print(frs_line)

    sec_line = ''
    for example_nr in range(len(problems)):  # priradi do promene problem poradove cislo prikladu
        space_count = 0
        if example_nr >= 1:# za prvnim a dalsim cislem udela mezeru
            sec_line += "    "
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
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
'''




print(arithmetic_arranger_2(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))