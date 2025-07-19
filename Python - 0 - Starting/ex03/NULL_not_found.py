def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f"Nothing: {object} {type(object)}")
            return 0
        elif isinstance(object, float) and object != object:
            print(f"Cheese: {object} {type(object)}")
            return 0
        elif isinstance(object, bool) and object is False:
            print(f"Fake: {object} {type(object)}")
            return 0
        elif isinstance(object, (int, float)) and object == 0:
            print(f"Zero: {object} {type(object)}")
            return 0
        elif object == "":
            print(f"Empty: {object} {type(object)}")
            return 0
        else:
            print("Type not Found")
    except Exception as e:
        print(f"An error occured: {e}")
    return 1
