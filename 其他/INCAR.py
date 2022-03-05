def repeat(string, a, b, c, alpha, beta, gamma):
    arr = string.split(" ")
    arr = [int(x) for x in arr ]
    arr = [alpha * [i * a for i in arr]] + [beta * [i * b for i in arr]] + [gamma * [i * c for i in arr]]
    new_arr = []
    for i in arr:
        new_arr += i
    ans = " ".join([str(_) for _ in new_arr])
    return ans


if __name__ == "__main__":
    string = "0 0 1"
    a = 5
    b = -5
    c = 3
    alpha = 8
    beta = 8
    gamma = 8
    result = repeat(string, a, b, c, alpha, beta, gamma)
    print(result)

