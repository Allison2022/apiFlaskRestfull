def emptyFieldsValidatorInDictionaries(diccionary):
    switch = False
    for keys, value in diccionary.items():
        if value == "":
            switch = True
    return switch