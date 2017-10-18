import json
import sys
from collections import OrderedDict
import re
def search(tfile, tlist):
    output = []
    tl = tlist.split(' ')
    #print tl
    with open(tfile, 'r') as f:
        data = json.load(f)
    for i in data['data']:
        for m in i['paragraphs']:
            for l in m['qas']:
                if all(re.compile(r'\b'+x.lower()+ r'\b').search(l['question'].encode('utf-8').lower()) for x in tl):
                #if all(x.lower() in l['question'].encode('utf-8').lower() for x in tl):
                    question = l['question'].encode('utf-8')
                    iD = l['id'].encode('utf-8')
                    answer = l['answers'][0]["text"]
                    dic = {"question":question, "id":iD}
                    dic["answer"]=answer
                    output.append(dic)
    sort_order = ['id','question','answer',]
    output_ordered = [OrderedDict(sorted(item.iteritems(), key = lambda(k, v): sort_order.index(k)))
                        for item in output]
    output = json.dumps(output_ordered, indent=2, separators=(',', ': '))
    with open ("1b.json", 'w') as f2:
        f2.write(output)
    #print output
    #pprint(output, indent=4) #just a try
    #below is useless
'''    print "["
    for x in output:
        print " "*2+'{"id":'+'"%s",' % (x['id'])
        print " "*2+'"question":'+'"%s",' % (x['question'])
        print " "*2+'"answer":'+'"%r"},' % (x['answer'])
        print ""
    print "]"'''
if __name__ == "__main__":
    search(sys.argv[1], sys.argv[2])