def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def listToString(var):
    assert isinstance(var, list)
    return ", ".join(var)


def removeComma(var):
    try:
        return var.replace(',', "")
    except:
        return ""


def removeParenthesis(var):
    try:
        var = var.replace('(', "")
        var = var.replace(')', "")
        return var
    except:
        return ""
