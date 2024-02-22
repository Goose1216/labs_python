import sys

def ord_by_len():
    lines = []
    print("Введите строки (для завершения ввода нажмите Ctrl+D):")
    for line in sys.stdin:
        lines.append(line)
    return sorted(lines, key=len)


print("\n", *ord_by_len(), sep="")
