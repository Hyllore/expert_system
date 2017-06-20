import sys

def filsdeputs(o):
    print o

def checkfile(rules, facts, queries):
    if (facts[0] != '=' and queries[0] != '?'):
        print "error\n"

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
    del rules[1]
    del rules[2]
    filsdeputs(rules)
    filsdeputs(facts)
    filsdeputs(queries)
    checkfile(rules, facts, queries)
