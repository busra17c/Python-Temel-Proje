l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten(xs):
    res = []
    def loop(ys):
        for i in ys:
            if isinstance(i, list):
                loop(i)
            else:
                res.append(i)
    loop(xs)
    return res
flatten(l)
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]
