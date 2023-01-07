def dictify(s):
  if ' ' not in s:
    return s
  key, rest = s.split(' ', 1)
  return {key: dictify(rest)}
  
def getKey(object: dict):
    var = list(object)
    print("3----")
    print(var)
    print(list(object))
    return var[0]


def getNestedValue(object: dict, key: str):
    if (key in object.keys()):
        print("1 --------")
        print(object)
        print(key)
        if type(object[key]) is dict:
            print("2-----")
            print(object[key])
            return getNestedValue(object[key], getKey(object[key]))
        else:
            print("4-----")
            return object[getKey(object)]
    else:
        nestedKey = getKey(object)
        return getNestedValue(object[nestedKey], key)
        
print("enter the object values with space eg a b c d ...so on")
object = dictify(input())
print("enter key")
key= input()
print("object=", object)
print("key=", key)
value = getNestedValue(object, key)
print(value)
