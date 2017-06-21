import sys

def filsdeputs(o):
    print o

def checkfile(rules, facts, queries):
    if (facts[0] != '=' and queries[0] != '?'):
        print "error\n"
        sys.exit()
    for r in rules:
        tab = r.replace("  ", " ")
        tab = tab.split(" ")
        print tab
        i = 0
        while (i < len(tab) and tab[i] != "=>"):
            print "h"
            if (i < len(tab) and tab[i][0] == '!'):
                if (tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                    print "error 1\n"
                    sys.exit()
            elif (i < len(tab) and tab[i].isalpha() == False or tab[i].isupper() == False):
                print "error 2\n"
                sys.exit()
            i += 1
            if (i < len(tab) and tab[i] == "=>"):
                break
            elif (i < len(tab) and tab[i] != "+" and tab[i] != "|" and tab[i] != "^"):
                print "error 3\n"
                sys.exit()
            i += 1
            print (tab[i])
            if (i < len(tab) and tab[i] == "=>"):
                print "error 3\n"
                sys.exit()
        if i >= len(tab):
            print "error 4\n"
            sys.exit()
        print tab

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.readlines()
    rules = []
    for s in content:
        s = s.strip()
        if len(s) > 0:
            rules.append(s)
    rules = [x.strip() for x in rules]
    queries = rules[-1]
    facts = rules[-2]
    del rules[-1]
    del rules[-1]
    filsdeputs(rules)
    filsdeputs(facts)
    filsdeputs(queries)
    checkfile(rules, facts, queries)
