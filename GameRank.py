import operator
    
def getOutDegree(matchOutcomes):
    matchGraph = {}
    for match in matchOutcomes:
        matchGraph[match[0]] = []
    
    for match in matchOutcomes:
        if ( int(match[1]) >= int(match[2]) ):
            matchGraph[match[0]].append(match[3])
        if ( int(match[1]) <= int(match[2]) ):
            matchGraph[match[3]].append(match[0])
    return matchGraph
    
def getInDegree(matchOutcomes):
    matchGraph = {}
    for match in matchOutcomes:
        matchGraph[match[3]] = []
    
    for match in matchOutcomes:
        if ( int(match[1]) >= int(match[2]) ):
            matchGraph[match[3]].append(match[0])
        if ( int(match[1]) <= int(match[2]) ):
            matchGraph[match[0]].append(match[3])
    return matchGraph
    
    

def getPageranks(outDegree, inDegree, numIter):
    numVerts = float(len(outDegree))
    pageranks = {}
    pageranksNext = {}
    sumSinks = 0.0
    sumSinksNext = 0.0

    for outVertex in outDegree:
        pageranks[outVertex] = 1.0 / numVerts
        if (len(outDegree[outVertex]) == 1):
            sumSinks = sumSinks + pageranks[outVertex]
            
    for i in range(numIter):
        for outVertex in outDegree:
            pageranksNext[outVertex] = sumSinks / numVerts
            for inVertex in inDegree[outVertex]:
                pageranksNext[outVertex] += pageranks[inVertex] / len(outDegree[inVertex])
            pageranksNext[outVertex] *= DAMPING_FACTOR;
            pageranksNext[outVertex] += (1.0 - DAMPING_FACTOR) / numVerts

            if (len(outDegree[outVertex]) == 1):
                sumSinksNext += pageranksNext[outVertex]

        pageranks, pageranksNext = pageranksNext, pageranks
        sumSinks = sumSinksNext
        sumSinksNext = 0.0
    return pageranks

def dispPageranks(pageranks):
    sortedPageranks = sorted(pageranks.items(), key=operator.itemgetter(1))
    for each in sortedPageranks:
        print each

            
with open ("Month1.csv", "r") as data:
    Month1 = data.readlines()

DAMPING_FACTOR = .85

matchOutcomes = []
            
for match in Month1:
    #Remove newlines and read matches into array
     matchOutcomes.append(match.rstrip().split(','))
     
outDegree = getOutDegree(matchOutcomes)
inDegree = getInDegree(matchOutcomes)
dispPageranks(getPageranks(outDegree, inDegree, 10000))
