def action():
    a = list(range(100))
    print(a[200])


if __name__ == '__main__':
    try:
        action()
    except NameError:
        print("single name")
    # 一次捕獲多種異常
    except(KeyError, PermissionError):
        print("Multi Name")
    # 空的except會捕獲其他未能捕獲的異常
    # except:
    #     print("empty Except block")

    #功能相似於空的except,但能夠避免系統退出相關所觸發的異常。
    except Exception:
        print("Like empty Except block,but Ignore system break error")

    # else當try未產生異常時執行
    else:
        print("goodEnd")
