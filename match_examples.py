
def process_data(data):
    match data:
        case "banana":
            print("Monkeys like bananas!")
        case "apple":
            print("Apples are okay.")
        case _:
            print("I don't know that fruit.")
        

data1 = "apple"
data2 = "orange"

process_data(data1)
process_data(data2)

def process_data_simple(data):
    match data:
        case 1:
            print("Data is 1")
        case 2:
            print("Data is 2")
        case _:
            print("Data is not 1 or 2")

process_data_simple(5)

print("Finish")

superhero = "Spiderman"
match superhero:
    case "Superman":
        secret_identity = "Clark Kent"
    case "Batman":
        secret_identity = "Bruce Wayne"
    case "Spiderman":
        secret_identity = "Peter Parker"
    case _:
        secret_identity = "?"

print(secret_identity)

subject = [3, 5]
match subject:
    case x, y if y > 6:
        print("y > 6")
    case 2, 5:
        print("2, 5")
    case x, 5:
        print(f"{x=}", f"{y=}")
    case 3, 5:
        print("3, 5")
    case _:
        print("no match for", subject)
