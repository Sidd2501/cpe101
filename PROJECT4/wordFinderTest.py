import unittest
from funcs import *


class TestCases(unittest.TestCase):
    def test_transpose_string(self):
        self.assertEqual(transpose_string(
            "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR", 10),
                         "EZAACBEABBOERANOEBOOABRCANRCIARRABBITEOABACRORCRRKRECRZBBIORNBOCOBRCRKIROHBNARCEABNEKCIHCABHRCAAAROR")
        self.assertEqual(transpose_string(
            "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRZARE", 10),
                         "EZAACBEABBOERANOEBOOABRCANRCIARRABBITEOABACRORCRRKRECRZBBIORNBOCOBRCRZIROHBNARCAABNEKCIHCRBHRCAAAROE")
        self.assertEqual(transpose_string(
            "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORBSDNENSQUEERD", 10),
                         "EZAACBEABNOERANOEBOEABRCANRCINRRABBITEOSBACRORCRRQRECRZBBIOUNBOCOBRCREIROHBNARBEABNEKCIHSRBHRCAAARDD")

    def test_flipString(self):
        self.assertEqual(flipString(
            "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"),
                         "PHLMSRRIMCAMCDSMGNHHLFDNOMSOGIMOAASLSBDIAORROHCROCRTEGAKSOMSSHUTECMABRHIGHLANDIOLLIMALLOOACLHAHSRALL")
        self.assertEqual(flipString("DEBMSUENKZW", ), "WZKNEUSMBED")
        self.assertEqual(flipString("HSMEJSDSEHNDM"), "MDNHESDSJEMSH")

    def test_checkForward(self):
        self.assertEqual(checkForward("AOOLLAMILL", "LAM"), "LAM: (FORWARD) row: 0 column: 4")
        self.assertEqual(checkForward("SMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP", "CHORRO"),
                         "CHORRO: (FORWARD) row: 1 column: 3")
        self.assertEqual(checkForward("SMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP", "!DS"), None)

    def test_checkBackward(self):
        self.assertEqual(checkBackward(
            "OIDNALHGIHAOOLLAMILLOIDEHSHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "LAND"), "LAND: (BACKWARD) row: 0 column: 5")

        self.assertEqual(checkBackward("IGOSMONDFL", "NOMS"), "NOMS: (BACKWARD) row: 0 column: 6")
        self.assertEqual(checkBackward("IGOSMONDFL", "!DE"), None)

    def test_checkDown(self):
        self.assertEqual(checkDown(
            "AOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "AOR"), "AOR: (DOWN) row: 0 column: 0")
        self.assertEqual(checkDown(
            "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "MLAP"), "MLAP: (DOWN) row: 6 column: 9")
        self.assertEqual(checkDown(
            "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "M!"), None)

    def test_checkUp(self):
        self.assertEqual(checkUp(
            "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "PALM"), "PALM: (UP) row: 9 column: 9")
        self.assertEqual(checkUp(
            "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "MARSH"), "MARSH: (UP) row: 6 column: 9")
        self.assertEqual(checkUp(
            "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP",
            "D!"), None)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
