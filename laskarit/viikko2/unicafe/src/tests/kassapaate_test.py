import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()


    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_edulliset_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myydyt_maukkaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)



    def test_syo_edullisesti_kateisella_rahamaara_riittava_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_syo_edullisesti_kateisella_rahamaara_riittamaton_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_syo_edullisesti_kateisella_rahamaara_riittava_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_rahamaara_riittamaton_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_rahamaara_riittava_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_rahamaara_riittamaton_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)



    def test_syo_maukkaasti_kateisella_rahamaara_riittava_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_rahamaara_riittamaton_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_syo_maukkaasti_kateisella_rahamaara_riittava_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_rahamaara_riittamaton_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_rahamaara_riittava_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_rahamaara_riittamaton_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    
    def test_syo_edullisesti_kortilla_rahamaara_riittava_palautusarvo(self):
        testikortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(testikortti), True)

    def test_syo_edullisesti_kortilla_rahamaara_riittava_veloitus(self):
        testikortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(testikortti)
        self.assertEqual(testikortti.saldo, 760)

    def test_syo_edullisesti_kortilla_rahamaara_riittava_lounaat(self):
        testikortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_rahamaara_riittava_kassa(self):
        testikortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



    def test_syo_edullisesti_kortilla_rahamaara_riittamaton_palautusarvo(self):
        testikortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(testikortti), False)
    
    def test_syo_edullisesti_kortilla_rahamaara_riittamaton_veloitus(self):
        testikortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(testikortti)
        self.assertEqual(testikortti.saldo, 100)

    def test_syo_edullisesti_kortilla_rahamaara_riittamaton_lounaat(self):
        testikortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kortilla_rahamaara_riittamaton_kassa(self):
        testikortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    

    def test_syo_maukkaasti_kortilla_rahamaara_riittava_palautusarvo(self):
        testikortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(testikortti), True)

    def test_syo_maukkaasti_kortilla_rahamaara_riittava_veloitus(self):
        testikortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(testikortti)
        self.assertEqual(testikortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_rahamaara_riittava_lounaat(self):
        testikortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_rahamaara_riittava_kassa(self):
        testikortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
   


    def test_syo_maukkaasti_kortilla_rahamaara_riittamaton_palautusarvo(self):
        testikortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(testikortti), False)
    
    def test_syo_maukkaasti_kortilla_rahamaara_riittamaton_veloitus(self):
        testikortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(testikortti)
        self.assertEqual(testikortti.saldo, 300)

    def test_syo_maukkaasti_kortilla_rahamaara_riittamaton_lounaat(self):
        testikortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_rahamaara_riittamaton_kassa(self):
        testikortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(testikortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_lataus_kortin_saldo(self):
        testikortti = Maksukortti(500)
        testikortti.lataa_rahaa(100)
        self.assertEqual(str(testikortti), "Kortilla on rahaa 6.00 euroa")

    def test_lataus_kassan_saldo(self):
        testikortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(testikortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)


    def test_lataus_kassan_saldo_miinus(self):
        testikortti = Maksukortti(500)
        palautus = self.kassapaate.lataa_rahaa_kortille(testikortti, -100)
        self.assertEqual(palautus, None)