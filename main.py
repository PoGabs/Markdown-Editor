formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
markdown = []


def print_markdown():
    for entry in markdown:
        print(entry, end="")
    print()


def heading(heading_level, current_text):
    string_ = ""
    if len(markdown) > 0:
        markdown.append("\n")
    counter = 0
    while counter < heading_level:
        string_ = string_ + "#"
        counter = counter + 1
    string_ = string_ + " " + current_text
    markdown.append(string_)
    markdown.append("\n")


def listing(type_):
    row_list = []
    while True:
        number_of_rows = int(input("Number of rows: "))
        if number_of_rows < 1:
            print("The number of rows should be greater than zero")
            continue
        break
    current_row_counter = 1
    if type_ == "o":
        while current_row_counter <= number_of_rows:
            row_list.append(str(current_row_counter) + ". " + input(f"Row #{str(current_row_counter)}: "))
            current_row_counter += 1
    elif type_ == "u":
        while current_row_counter <= number_of_rows:
            row_list.append("* " + input(f"Row #{str(current_row_counter)}: "))
            current_row_counter += 1
    for item in row_list:
        markdown.append(item)
        markdown.append("\n")


while True:
    input_ = input("Choose a formatter: ")
    if input_ == "!help":
        print("Available formatters: ", end="")
        for i in formatters[:-1]:
            print(i + " ", end="")
        print(formatters[-1], end="")
        print()
        print("Special commands: !help !done")
        continue
    elif input_ == "!done":
        break
    elif input_ in formatters:
        if input_ == "header":
            while True:
                level = int(input("Level: "))
                if level < 1 or level > 6:
                    print("The level should be within the range of 1 to 6")
                    continue
                break
            text = input("Text: ")
            heading(level, text)
            print_markdown()
        elif input_ == "plain":
            text = input("Text: ")
            markdown.append(text)
            print_markdown()
        elif input_ == "bold":
            text = input("Text: ")
            markdown.append(f"**{text}**")
            print_markdown()
        elif input_ == "inline-code":
            text = input("Text: ")
            markdown.append(f"`{text}`")
            print_markdown()
        elif input_ == "italic":
            text = input("Text: ")
            markdown.append(f"*{text}*")
            print_markdown()
        elif input_ == "new-line":
            markdown.append("\n")
            print_markdown()
        elif input_ == "link":
            label = input("Label: ")
            url = input("URL: ")
            markdown.append(f"[{label}]({url})")
            print_markdown()
        elif input_ == "ordered-list":
            listing("o")
            print_markdown()
        elif input_ == "unordered-list":
            listing("u")
            print_markdown()
        continue
    print("Unknown formatting type or command")
f = open("output.md", "w")
f.writelines(markdown)
f.close()
