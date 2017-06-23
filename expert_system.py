#!/usr/bin/python

import sys

def checkstring(r):
    i = 0
    u = 0
    check = 0
    while (i < len(r)):
        if (r[i] == "="):
            break
        if (r[i] == "("):
            check += 1
            u = 1
            while (r[i + u] == " "):
                u += 1
            if (r[i + u] == ")" or r[i + u] == "+" or r[i + u] == "^" or r[i + u] == "|"):
                print "Parentheses error\n"
                sys.exit()
        if (r[i] == ")"):
            check -= 1
            u = -1
            while (r[i + u] == " "):
                u -= 1
            if (r[i + u] == "(" or r[i + u] == "+" or r[i + u] == "^" or r[i + u] == "|"):
                print "Parentheses error\n"
                sys.exit()
        if (check < 0):
            print "Parentheses error\n"
            sys.exit()
        i += 1
    if (check != 0):
        print "Parentheses error\n"
        sys.exit()



def checkfile(rules, facts, queries):
    if (facts[0] != '=' or queries[0] != '?' or facts[1:].isalpha() != True or facts[1:].isupper() != True or queries[1:].isalpha() != True or queries[1:].isupper() != True):
        print "error queries or fact\n"
        sys.exit()
    for r in rules:
        while (r.find("  ") != -1):
            r = r.replace("  ", " ")
            checkstring(r)
        r = r.replace("(", "")
        r = r.replace(")", "")
        tab = r.split(" ")
        print tab, "hey"
        i = 0
        while (i < len(tab) and tab[i] != "=>"):
            print "h"
            if (i < len(tab) and tab[i][0] == '!'):
                if (len(tab[i]) != 2 or tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
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
        elif (tab[i] == "=>"):
            i += 1
            if (i < len(tab)):
                if (tab[i][0] == '!'):
                    if (len(tab[i]) != 2 or tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                        print "error 5\n"
                        sys.exit()
                elif (tab[i].isalpha() == False or tab[i].isupper() == False):
                    print "error 6\n"
                    sys.exit()
                i += 1
            else:
                print "error 6\n"
                sys.exit()
            if (i < len(tab)):
                print tab[i], "heho"
                print str(i + 1), "and", str(len(tab))
                if (tab[i] != "+" or i + 1 >= len(tab)):
                    print "error 7\n"
                    sys.exit()
                i += 1
                if (i < len(tab)):
                    if (tab[i][0] == '!'):
                        if (tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                            print "error 8\n"
                            sys.exit()
                    elif (tab[i].isalpha() == False or tab[i].isupper() == False):
                        print "error 9\n"
                        sys.exit()
                    i += 1
                    if (i < len(tab)):
                        print "error 10\n"
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
    print (rules)
    print (facts)
    print (queries)
    checkfile(rules, facts, queries)
