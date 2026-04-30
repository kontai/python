import time

# 裝飾器函數：用於測量函數執行時間並添加額外功能
def foo(func):
    def warpper(p):
        print("before")  # 執行前的訊息
        start_time = time.time()  # 記錄開始時間
        time.sleep(1)  # 模擬延遲
        func(p*5)  # 執行原函數，參數乘以5
        end_time = time.time()  # 記錄結束時間
        func(end_time - start_time)  # 執行原函數，傳入執行時間
        print("after")  # 執行後的訊息
    return warpper

# 使用裝飾器修飾的測試函數
@foo
def test(aa):
    print(aa)  # 簡單的印出函數

# 程式入口點
if __name__ == "__main__":
    test("aa")  # 呼叫被裝飾的測試函數
