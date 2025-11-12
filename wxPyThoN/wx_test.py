#!  coding=utf-8
import wx, string


class MySalgar(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title=u"薪資試算程式", size=(250, 200))
        panel = wx.Panel(self)
        # 配置視窗元件 -- 開始 --
        wx.StaticText(parent=panel, label=u"工作幾年？", pos=(10, 10))
        self.a = wx.TextCtrl(parent=panel, pos=(100, 10))
        wx.StaticText(parent=panel, label=u"一個月多少錢？", pos=(10, 50))
        self.b = wx.TextCtrl(parent=panel, pos=(100, 50))
        self.btn = wx.Button(parent=panel, label=u"結算薪資", pos=(10, 100))
        self.message1 = wx.StaticText(parent=panel, pos=(10, 130))
        self.message2 = wx.StaticText(parent=panel, pos=(10, 150))


# 配置視窗元件 -- 結束 --
if __name__ == '__main__':
    app = wx.App()
    frame = MySalgar()
    frame.Show()
    app.MainLoop()
