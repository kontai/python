import unittest
import cap

class TestCap(unittest.TestCase):

    def setup(self):
        '''
        將測試前的準備工作寫在 setUp() 裡，在每一個 test case 開始前執行
        '''
        pass


    def tearDown(self):
        '''
        將測試後的清理工作寫在 tearDown() 裡，在每一個 test case 結束後執行，無論測試結果如何（甚至是 test error）
        '''
        pass


    def test_one(self):
        text = 'duck'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Duck')


    def test_nultiple_word(self):
        text = 'a veritable flock of ducks'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')


    if __name__ == '__main__':
        unittest.main
