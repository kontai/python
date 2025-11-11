#----------------------------------------------------------------------------
# 示範在 Python 中撰寫非 ASCII 文字的所有方法，以及原始碼編碼宣告。
#
# 如果這個檔案以 Latin-1 編碼儲存，它會正常運作。
# 若將上面的宣告改成 ASCII 或 UTF-8，則會失敗，
# 因為 myStr1 的值中 0xC4 和 0xE8 並非這些編碼下的有效字元。
#
# 若將檔案儲存為 UTF-8，並同時改成 UTF-8 宣告，則也能運作。
# 由於 Python 預設使用 UTF-8 讀取原始碼，因此若本檔案以 UTF-8 儲存，
# 或其文字皆為 ASCII（ASCII 是 Latin-1 與 UTF-8 的子集），
# 則宣告行可以省略。
#----------------------------------------------------------------------------
myStr1 = 'AÄBèC'                   # 直接以原始編碼書寫
myStr2 = 'A\xc4B\xe8C'             # 使用十六進位轉義碼
myStr3 = 'A\u00c4B\U000000e8C'     # 使用 Unicode 短/長轉義碼
myStr4 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'  # 使用 chr() 組成字串

import sys, locale
print('Sys hosting platform: ', sys.platform)
print('Sys default encoding: ', sys.getdefaultencoding())
print('Open default encoding:', locale.getpreferredencoding(False))

for aStr in (myStr1, myStr2, myStr3, myStr4):
    print(f'{aStr}, strlen={len(aStr)}', end=', ')
    bytes1 = aStr.encode()             # 預設 UTF-8：重音字母佔 2 bytes
    bytes2 = aStr.encode('latin-1')    # Latin-1：每字元 1 byte
    #bytes3 = aStr.encode('ascii')     # 失敗：超出 ASCII 範圍 0...127
    print(f'byteslen1={len(bytes1)}, byteslen2={len(bytes2)}')
