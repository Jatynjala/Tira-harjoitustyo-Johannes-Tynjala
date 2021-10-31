from random import randint, choice

def SYT(a: int, b: int):
    """Palauttaa kokonaislukujen a ja b suurimman yhteisen tekijän"""
    if a==0:
        return b
    return SYT(b%a, a)

def onko_alkuluku(x: int):
    """Tarkistaa, onko annettu luku alkuluku"""
    if x%2==0:
        return False
    for y in range(3, x, 2):
        if x%y==0:
            return False
    return True

def RSA_avainten_muodostus():
    """Muodostaa tuplen (n, e, d), joista n ja e muodostavat julkisen avaimen ja d yksityisen"""
    lukulista=[x for x in range(101, 1000, 2) if onko_alkuluku(x)]
    p=lukulista.pop(randint(0, len(lukulista)))
    q=choice(lukulista)
    n=p*q
    luku=(p-1)*(q-1)
    e=randint(2, int((3*(n/4))))
    while SYT(e, luku)!=1:
        e+=1
    d=randint(101, int((3*(n/4))))
    while ((d*e)-1)%luku!=0:
        d+=1
    return (n, e, d)

if __name__ == "__main__":
    avain=RSA_avainten_muodostus()
    print(avain)
    print(SYT(25, 400))
    print(onko_alkuluku(19))
    print(onko_alkuluku(20))
    print(onko_alkuluku(21))