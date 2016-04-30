## Graphical User Interfaces

<!-- ==================== TOC using MarkdownTOC Sublime-Text plugin ===================== -->
<!-- MarkdownTOC depth=3 -->

- Basic frame
- Adding some controls

<!-- /MarkdownTOC -->
<!-- ==============================  END TOC ================================= -->

<!-- ============================= PRE ================================= -->

Using [wxPython](www.wxpython.org) for Python GUIs.

### Basic frame

```matlab
% Simple frame
f = figure('NumberTitle','off',...
           'Name','Example',
           'Position',[0 0 300 200]);
centerfig(f);
```

```python
# Simple frame
import wx

class Frame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.Centre()
        self.Show()

if __name__=='__main__':
    app = wx.App()
    fr = Frame(parent=None, title="Example", size=(300,200))
    app.MainLoop()
```

### Adding some controls

```matlab
% Adding controls
f = figure('NumberTitle','off',...
           'Name','Example',
           'Position',[0 0 300 200]);
centerfig(f);

% A button
bt = uicontrol('style','push',...
               'string','Button',...
               'Position',[10,10,100,25]);
% An edit text
text = uicontrol('style','edit',...
               'string','',...
               'Position',[10,50,100,25]);

```

```python
# Adding controls
import wx

class Frame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.bt = wx.Button(self, -1, label="Button", size=(100,25), pos=(10,10))
        self.text = wx.TextCtrl(self, -1, value="", size=(100,25), pos=(10,50))
        self.Centre()
        self.Show()

if __name__=='__main__':
    app = wx.App()
    fr = Frame(parent=None, title="Example", size=(300,200))
    app.MainLoop()
```
