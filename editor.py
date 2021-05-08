def get_row_number():
    rows = 0
    while rows <= 0:
        try:
            rows = int(input("- Number of rows: "))
            if rows <= 0:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("Number of rows must only be a numeric value")
            continue
    return rows


print("$ python markdown-editor.py")
formatters = ("plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line")
special = ("!help", "!done")
choice = input()
output = ""
while choice != "!done":
    if choice not in formatters and choice != "!help":
        print("Unknown formatting type or command. Please try again.")

    elif choice == "!help":
        print("Available formatters:", *formatters)
        print("Special commands:", *special)

    elif choice == "header":
        level = 0
        while level < 1 or level > 6:
            try:
                level = int(input("- Level: "))
                if level < 1 or level > 6: print("Kindly enter a number from 1 to 6")
            except ValueError:
                print("Level can only be a numerical value from 1 to 6")
                continue
        text = input("- Text: ")
        for _ in range(0, level):
            output += "#"
        output += " " + text + "\n"

    elif choice == "plain":
        text = input("- Text: ")
        output += text

    elif choice == "new-line":
        output += "\n"

    elif choice == "link":
        label = input("- Label: ")
        url = input("- URL: ")
        output += "[" + label + "](" + url + ")"

    elif choice == "bold":
        text = input("- Text: ")
        output += "**" + text + "**"

    elif choice == "italic":
        text = input("- Text: ")
        output += "*" + text + "*"

    elif choice == "inline-code":
        text = input("- Text: ")
        output += "`" + text + "`"

    elif choice == "ordered-list":
        rows = get_row_number()
        elements = []
        for i in range(0, rows):
            elements.append(input(f"Row #{i+1}: "))
        for i in range(0, rows):
            output += str(i+1)+". "+elements[i]+"\n"

    elif choice == "unordered-list":
        rows = get_row_number()
        elements = []
        for i in range(0, rows):
            elements.append(input(f"Row #{i + 1}: "))
        for i in range(0, rows):
            output += "* " + elements[i] + "\n"
    print(output)
    choice = input("- Choose a formatter: ")

with open("output.md", "w+") as outfile:
    outfile.write(output)