import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_rahan_ottaminen_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")

    def test_rahan_ottaminen_rahaa_tarpeeksi_palautus(self):
        tulos = self.maksukortti.ota_rahaa(100)
        self.assertEqual(tulos, True)

    def test_rahan_ottaminen_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(100)
        kortti.ota_rahaa(200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")

    def test_rahan_ottaminen_rahaa_ei_tarpeeksi_palautus(self):
        kortti = Maksukortti(100)
        tulos = kortti.ota_rahaa(200)
        self.assertEqual(tulos, False)


