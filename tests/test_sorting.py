import unittest
import sorting_algorithms 

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
       
        karisik_liste = [5, 2, 9, 1, 5, 6]
        beklenen_sonuc = [1, 2, 5, 5, 6, 9]
        
    
        sonuc = sorting_algorithms.bubble_sort(karisik_liste) 
        
     
        self.assertEqual(sonuc, beklenen_sonuc)

if __name__ == '__main__':
    unittest.main()