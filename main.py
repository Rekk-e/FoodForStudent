# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('n=')
    n = int(input())
    k = 0
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if (c < a + b) and (a < b + c) and (b < a + c) and (a + b + c == n):
                    k = k+1
print(str(k) + ' treugolnikov')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
