#!/usr/bin/python
import pprint
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
        #print tab, "hey"
        i = 0
        while (i < len(tab) and tab[i] != "=>"):
            #print "h"
            if (i < len(tab) and tab[i][0] == '!'):
                if (len(tab[i]) != 2 or tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                    print "error maj or letter\n"
                    sys.exit()
            elif (i < len(tab) and tab[i].isalpha() == False or tab[i].isupper() == False):
                print "error maj or letter\n"
                sys.exit()
            i += 1
            if (i < len(tab) and tab[i] == "=>"):
                break
            elif (i < len(tab) and tab[i] != "+" and tab[i] != "|" and tab[i] != "^"):
                print tab[i]
                print "error symbol\n"
                sys.exit()
            i += 1
            #print (tab[i])
            if (i < len(tab) and tab[i] == "=>"):
                print "error missing value\n"
                sys.exit()
        if i >= len(tab):
            print "error missing value\n"
            sys.exit()
        elif (tab[i] == "=>"):
            i += 1
            if (i < len(tab)):
                if (tab[i][0] == '!'):
                    if (len(tab[i]) != 2 or tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                        print "error maj or letter after '=>'\n"
                        sys.exit()
                elif (tab[i].isalpha() == False or tab[i].isupper() == False):
                    print "error maj or letter after '=>'\n"
                    sys.exit()
                i += 1
            else:
                print "error missing value\n"
                sys.exit()
            if (i < len(tab)):
                #print tab[i], "heho"
                #print str(i + 1), "and", str(len(tab))
                if (tab[i] != "+" or i + 1 >= len(tab)):
                    print "error symbol after '=>'\n"
                    sys.exit()
                i += 1
                if (i < len(tab)):
                    if (tab[i][0] == '!'):
                        if (tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                            print "error maj or letter after '=>'\n"
                            sys.exit()
                    elif (tab[i].isalpha() == False or tab[i].isupper() == False):
                        print "error maj or letter after '=>'\n"
                        sys.exit()
                    i += 1
                    if (i < len(tab)):
                        print "error missing value\n"
                        sys.exit()
        #print tab

def makegraph(rules):
    tmp = []
    tmp2 = []
    graph = {}
    i = 0
    alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for a in alph:
        graph[a] = []
    for r in rules:
        while (r.find("  ") != -1):
            r = r.replace(" ", "")
        tmp = r.split("=>")
        print r
        print len(tmp[1])
        print tmp[1]
        if (len(tmp[1]) > 2):
            print 'hey'
            tmp2 = tmp[1].split("+")
            if (tmp2[0][0] == "!"):
                tmp2[0].replace("!", "")
            if (tmp2[1][0] == "!"):
                tmp2[1].replace("!", "")
            graph[tmp2[0]].append(r)
            graph[tmp2[1]].append(r)
        else:
            tmp2.append(tmp[1])
            if (tmp2[0][0] == "!"):
                tmp2[0] = tmp2[0].replace("!", "")
            graph[tmp2[0]].append(r)
        #else if (tmp[1][0] == "!"):
            #print tmp
            #gerer le cas des !A + !B, et inverser le not sur la regle
        #if (tmp[1] in graph):
            #graph[tmp[1]][].append(tmp[0])
        #graph[tmp[1]] = tmp[0]
        #i += 1;
        tmp = []
        tmp2 = []
    #print(graph)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(graph)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.readlines()
    rules = []
    for s in content:
        s = s.split("#", 1)[0]
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
    makegraph(rules)
