import random
def nenechan(Scooby):
    Arthur = open(Scooby, 'rb')
    im = (Arthur.read()[4:])
    Arthur.close()
    im = (bytearray(im))
    return im

def Shiro(im,gian):
    for j in gian:
        for ix, val in enumerate(im):
            im[ix] = val ^ ord(j)
    return im

def Shinchan(im,ph):
    fin = open(ph, 'wb')
    fin.write((im))
    fin.close()

def Himawari(michan, Suneo):
    Kazama = ""
    for Arthur in michan :
        if Arthur.isalpha():
            if Arthur.islower() :
                Hiroshi = chr((ord(Arthur)-ord('a') - Suneo)%26 + ord("a"))
            else:
                Hiroshi = chr((ord(Arthur)-Suneo-ord('A'))%26 + ord("A"))
            Kazama += Hiroshi
    
        else:
            Kazama += Arthur
    return Kazama


def main():
    Doraemon = "REDUCTED"
    shizuka = "REDUCTED"
    gian = random.randint(0,20)
    nobita = nenechan(Doraemon)
    shizuka = Himawari(shizuka,gian)
    nobita = Shiro(nobita,shizuka)
    Shinchan(nobita,Doraemon)


if __name__ == "__main__":
    main()