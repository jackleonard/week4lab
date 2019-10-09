
charsPressed = {"a":0, "b":0, "c":0, "d":0,}
print(charsPressed["a"])
charsPressed["a"] =+ 1
print(charsPressed)

dictList = {"a":1, "b":9, "c":9, "d":0,}

for item in dictlist.items():
    key = item[0]
    value = item[1]
    print(key, value)
    if value > highestvalue:
        highestvalue = value
        print(f"Highest Value: {highestvalue}")
        # find the chars with highest value
        for k, v in dictlist.items():
            if v == highestvalue:
                highestValueList.append((k, v))
                print(highestValueList)
return highestValueList
