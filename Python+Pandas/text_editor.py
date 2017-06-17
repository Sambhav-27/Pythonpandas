import wx
import wx.lib.dialogs
import wx.stc as stc

faces ={
	'times':'Times New Roman',
	'mono': 'Courier New',
	'helv': 'Arial',
	'other':'Comic Sans MS',
	'size': 10,
	'size2': 14,
}

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		self.leftMarginWidth = 25

		wx.Frame.__init__(self, parent, title=title, size=(800,600))
		self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)

		self.Show()

app = wx.App()
frame = MainWindow(None, "My Text Editor")
app.MainLoop()