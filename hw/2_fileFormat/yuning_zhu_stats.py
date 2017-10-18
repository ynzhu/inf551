import json
import sys
def stats(tfile):
    '''
    Take a json file and count different types of quesionts.
    Return json file
    '''
    how = 0
    howmany = 0
    howmuch = 0
    what = 0
    when = 0
    where = 0
    which = 0
    who = 0
    whom = 0
    with open(tfile, 'r') as f:
        data = json.load(f) #json to dict
    for i in data['data']:
        for m in i['paragraphs']:
            for l in m['qas']:
                l = l['question'].strip() #
                if l[0:8].lower() == "How many".lower():
                    howmany += 1
                elif l[0:8].lower() == "How much".lower():
                    howmuch += 1
                elif l[0:3].lower() == "How".lower():
                    how += 1               
                elif l[0:4].lower() == "What".lower():
                    what += 1                
                elif l[0:4].lower() == "When".lower():
                    when += 1                
                elif l[0:5].lower() == "Where".lower():
                    where += 1                
                elif l[0:5].lower() == "Which".lower():
                    which += 1
                elif l[0:3].lower() == "Who".lower():
                    who += 1
                elif l[0:4].lower() == "Whom".lower():
                    whom += 1
    output = {"how":how, "how many":howmany, "how much":howmuch, "what":what, 
    "when":when, "where":where, "which":which, "who":who, "whom":whom}
    output = json.dumps(output)
    with open ("1a.json", 'w') as f2:
        f2.write(output)    
    #print output
if __name__ == "__main__":
    stats(sys.argv[1])
