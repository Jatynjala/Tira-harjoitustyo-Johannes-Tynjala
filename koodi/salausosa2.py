from random import randint, choice

def SYT(a:int, b:int):
    """Palauttaa kokonaislukujen a ja b suurimman yhteisen tekijän"""
    if a==0:
        return b
    return SYT(b%a, a)

def RSA_avainten_muodostus():
    """Muodostaa tuplen (n, e, d), joista n ja e muodostavat julkisen avaimen ja d yksityisen"""
    lukulista=[x for x in range(101, 500)]
    p=choice(lukulista)
    q=choice(lukulista)
    del lukulista
    n=p*q
    luku=(p-1)*(q-1)
    e=randint(2, n-1)
    suunta=choice([-1, 1])
    while SYT(e, luku)!=1:
        if e+suunta not in range(2, n):
            suunta=suunta*-1
        e+=suunta
    d=randint(101, 9999)
    suunta=choice([-1, 1])
    while ((d*e)-1)%luku!=0:
        if d+suunta not in range(101, 10000):
            suunta=suunta*-1
        d+=1
    return (n, e, d)

if __name__ == "__main__":
    avain=RSA_avainten_muodostus()
    print(avain)