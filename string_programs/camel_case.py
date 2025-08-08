def split_camel_case(InString):
    Result = " "
    for n in range(0, len(InString)):
        NextChar = InString[n]
        if NextChar == NextChar.upper():
            if n > 1:
                Result = Result + " "
            NextChar = NextChar.lower()
        Result = Result + NextChar

    return Result
