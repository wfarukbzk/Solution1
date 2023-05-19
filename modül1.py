class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satislar = {}
        
    def get_magaza_adi(self):
        return self.__magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi
        
    def magaza_satis_tutar(self):
        satis_tutari = 0
        for satis in self.__satislar.values():
            satis_tutari += satis
        return satis_tutari

    def satici_satis_tutar(self):
        satis_tutarlari = {}
        for satis in self.__satislar.items():
            if satis[0][1] == self.__satici_adi:
                if satis[0][2] not in satis_tutarlari:
                    satis_tutarlari[satis[0][2]] = satis[1]
                else:
                    satis_tutarlari[satis[0][2]] += satis[1]
        return satis_tutarlari
    
    def add_satis(self, satici_adi, satici_cinsi, satis_tutari):
        anahtar = (self.__magaza_adi, self.__satici_adi, self.__satici_cinsi)
        if anahtar not in self.__satislar:
            self.__satislar[anahtar] = satis_tutari
        else:
            self.__satislar[anahtar] += satis_tutari

    def __str__(self):
        s = "\n************************************\n"
        s += f"{self.__magaza_adi} maðazasý için satýcý {self.__satici_adi}:\n"
        satislar = self.satici_satis_tutar()
        for cinsi, tutar in satislar.items():
            s += f"{cinsi} satýþý: {tutar} TL\n"
        s += f"Toplam satýþ tutarý: {self.magaza_satis_tutar()} TL\n"
        s += "************************************"            
        return s

    
def main():
    magazalar = {}
    while True:
        magaza_adi = input("Maðaza adý (press enter to exit): ")
        if not magaza_adi:
            break
        
        if magaza_adi=="*":
            print("\n******************************")
            print("*****Mehmet Faruk BOZKAYA*****")
            print("**********190601061***********")
            print("******************************\n")
            break
            
        if magaza_adi=="--help":
            print("\n******************************")
            print("*****Help for what?*****")
            print("******************************\n")
            break
        
        satici_adi = input("Satýcý adý: ")
        if not satici_adi:
            break
        
        while True:
            satici_cinsi = input("Satýcýnýn cinsi (tv, bilgisayar, beyaz eþya, diðer): ")
            if satici_cinsi in ("tv", "bilgisayar", "beyaz eþya", "diðer"):
                break
            else:
                print("Lütfen geçerli bir satýcý cinsi girin.")
        
        while True:
            try:
                satis_tutari = float(input("Satýþ tutarý: "))
                break
            except ValueError:
                print("Lütfen geçerli bir sayý girin.")
        
        if magaza_adi not in magazalar:
            magazalar[magaza_adi] = Magaza(magaza_adi, satici_adi, satici_cinsi)
        
        magazalar[magaza_adi].add_satis(satici_adi, satici_cinsi, satis_tutari)
    
    for magaza in magazalar.values():
        print(magaza)
        
if __name__ == "__main__":
    main()
