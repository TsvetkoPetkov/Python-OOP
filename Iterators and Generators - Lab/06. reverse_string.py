def reverse_text(text):
    start_inx = len(text) - 1
    end_inx = 0

    while start_inx >= end_inx:
        yield text[start_inx]
        start_inx -= 1


for char in reverse_text("step"):
    print(char, end='')
