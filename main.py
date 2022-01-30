def mainFunction(numOfStars):
    if numOfStars >= 0:
        outStr = ''
        for i in range(numOfStars):
            outStr += '*'
        print(outStr)
        return outStr
    else:
        return False
