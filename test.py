import wx

class MyApp(wx.App):
    def __init__(self):
        super(MyApp,self).__init__()

class MyFrame(wx.Frame):
    def __init__(self,title='test',size=wx.DefaultSize):
        super(MyFrame,self).__init__(None,wx.ID_ANY,title=title,size=size,style=wx.DEFAULT_FRAME_STYLE^wx.MINIMIZE_BOX)
        self.Center()
        #self.SetSize(500,500)
        #self.SetTitle('aaa')

if __name__ == '__main__':
    app = MyApp()
    frame = MyFrame(title='wx-test',size=(400,300))
    frame.Show()
    app.MainLoop()
