#!/usr/bin/python
import sys
import os

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
                print "Parentheses error"
                sys.exit()
        if (r[i] == ")"):
            check -= 1
            u = -1
            while (r[i + u] == " "):
                u -= 1
            if (r[i + u] == "(" or r[i + u] == "+" or r[i + u] == "^" or r[i + u] == "|"):
                print "Parentheses error"
                sys.exit()
        if (check < 0):
            print "Parentheses error"
            sys.exit()
        i += 1
    if (check != 0):
        print "Parentheses error"
        sys.exit()



def checkfile(rules, facts, queries):
    if (facts[0] != '=' or queries[0] != '?' or (len(facts) > 1 and (facts[1:].isalpha() != True or facts[1:].isupper() != True)) or queries[1:].isalpha() != True or queries[1:].isupper() != True or len(queries) <= 1):
        print "error queries or fact"
        sys.exit()
    for r in rules:
        while (r.find("  ") != -1):
            r = r.replace("  ", " ")
        checkstring(r)
        r = r.replace("(", "")
        r = r.replace(")", "")
        tab = r.split(" ")
        i = 0
        while (i < len(tab) and tab[i] != "=>"):
            if (i < len(tab) and tab[i][0] == '!'):
                if (len(tab[i]) != 2 or tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                    print "error maj or letter hey"
                    sys.exit() 
            elif (i < len(tab) and len(tab[i]) != 1 or tab[i].isalpha() == False or tab[i].isupper() == False):
                print "error maj or letter hoy"
                sys.exit()
            i += 1
            if (i < len(tab) and tab[i] == "=>"):
                break
            elif (i < len(tab) and tab[i] != "+" and tab[i] != "|" and tab[i] != "^"):
                print "error symbol"
                sys.exit()
            i += 1
            if (i < len(tab) and tab[i] == "=>"):
                print "error missing value"
                sys.exit()
        if i >= len(tab):
            print "error missing value"
            sys.exit()
        elif (tab[i] == "=>"):
            i += 1
            if (i < len(tab)):
                if (tab[i][0] == '!'):
                    if (len(tab[i]) != 2 or tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                        print "error maj or letter after '=>'"
                        sys.exit()
                elif (len(tab[i]) != 1 or tab[i].isalpha() == False or tab[i].isupper() == False):
                    print "error maj or letter after '=>'"
                    sys.exit()
                i += 1
            else:
                print "error missing value"
                sys.exit()
            if (i < len(tab)):
                if (tab[i] != "+" or i + 1 >= len(tab)):
                    print "error symbol after '=>'"
                    sys.exit()
                i += 1
                if (i < len(tab)):
                    if (tab[i][0] == '!'):
                        if (tab[i][1].isalpha() == False or tab[i][1].isupper() == False):
                            print "error maj or letter after '=>'"
                            sys.exit()
                    elif (tab[i].isalpha() == False or tab[i].isupper() == False):
                        print "error maj or letter after '=>'"
                        sys.exit()
                    i += 1
                    if (i < len(tab)):
                        print "error missing value"
                        sys.exit()

def makegraph(rules):
    tmp = []
    tmp2 = []
    graph = {}
    i = 0
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for a in alph:
        graph[a] = []
    for r in rules:
        while (r.find(" ") != -1):
            r = r.replace(" ", "")
        tmp = r.split("=>")
        if (len(tmp[1]) > 2):
            r1 = r
            r2 = r
            tmp2 = tmp[1].split("+")
            if (tmp2[0][0] == "!"):
                tmp2[0] = tmp2[0].replace("!", "")
                r1 = "!(" + tmp[0] + ")" + "=>" + tmp[1]
            if (tmp2[1][0] == "!"):
                tmp2[1] = tmp2[1].replace("!", "")
                r2 = "!(" + tmp[0] + ")" + "=>" + tmp[1]
            graph[tmp2[0]].append(r1)
            graph[tmp2[1]].append(r2)
        else:
            tmp2.append(tmp[1])
            if (tmp2[0][0] == "!"):
                r = "!(" + tmp[0] + ")" + "=>" + tmp[1]
                tmp2[0] = tmp2[0].replace("!", "")
            graph[tmp2[0]].append(r)
        tmp = []
        tmp2 = []
    for a in alph:
        for g in graph[a]:
            str1 = g.split("=>")[0]
            for s in str1:
                if (a == s):
                    print "error value implies the same value"
                    sys.exit()
    return graph

def do_algo(querie, graph, ans, pastletter):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(graph[querie]) == 0:
        return ans
    for g in graph[querie]:
        tmp = g.split("=>")[0]
        for t in tmp:
            if t.isalpha() == True and ans[t][1] == False:
                for p in pastletter:
                    if p == querie:
                        print "error infinite loop"
                        sys.exit()
                pastletter.append(querie)
                ans = do_algo(t, graph, ans, pastletter)
                del pastletter[-1]
        for a in alph:
            if (ans[a][0] == True):
                tmp = tmp.replace(a, "1")
            elif (ans[a][0] == False):
                tmp = tmp.replace(a, "0")
        while (tmp.find("+") != -1):
            tmp = tmp.replace("+", " and ")
        while (tmp.find("|") != -1):
            tmp = tmp.replace("|", " or ")
        while (tmp.find("!") != -1):
            tmp = tmp.replace("!", " not ")
        if (ans[querie][1] == False):
            i = eval(tmp)
            if (i == 1):
                ans[querie][0] = True
            elif (i == 0):
                ans[querie][0] = False
            ans[querie][1] = True
        elif (ans[querie][1] == True and eval(tmp) != ans[querie][0]):
           ans[querie][0] = True 
    return ans

def start_algo(graph, facts, queries):
    ans = {}
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for a in alph:
        ans[a] = [False, False]
    facts = facts.replace("=" , "")
    queries = queries.replace("?", "")
    for f in facts:
        ans[f] = [True, False]
    for a in alph:
        if (len(graph[a]) == 0):
            ans[str(a)][1] = True
    for querie in queries:
        ans = do_algo(querie, graph, ans, [])
    for querie in queries:
        print querie, "is", ans[querie][0]

if __name__ == "__main__":
    i = 0
    if len(sys.argv) != 2:
        print "error parameters"
        sys.exit()
    if os.path.isfile(sys.argv[1]) == False:
        print "Error open"
        sys.exit()

    content = []
    with open(sys.argv[1]) as f:
        for line in f:
            content.append(line)
            i += 1
    if i <= 1:
        print "Error"
        sys.exit()
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
    checkfile(rules, facts, queries)
    graph = makegraph(rules)
    start_algo(graph, facts, queries)
