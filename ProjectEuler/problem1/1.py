

def sol():
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    
    return sum


if __name__ == "__main__":
    res = sol()
    print(res)
        