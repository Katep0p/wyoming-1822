import ConfigParser

listOne = [1,2,3]
print listOne[2]
myDictionary = {"one":"hej"} #key to the left of the value
print myDictionary

print myDictionary["one"]

config = ConfigParser.ConfigParser()
config.read('texter.cfg')
#always add section and key
print config.get('Section1', 'question1')
