def enforce(types: list[list]):
    for i in range(len(types)):
        if type(types[i][0]) != types[i][1]:
            raise TypeError("Unexpected type. expected " + str(types[i][1]) + " got " + str(type(types[i][0])))
