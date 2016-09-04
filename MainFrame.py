# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.7.2 on Tue May 31 22:36:07 2016
#
import logging
import hashlib
import re
import os
import sys
import copy
import pytsk3
from ExtractionDialog import ExtractionDialog
import wx
import wx.dataview as dataview
import wx.lib.mixins.listctrl as listmix
from wx.lib.agw import ultimatelistctrl

from LogicalVolumeDialog import LogicalVolumeDialog

from libpv.EvidenceEnumerator import EvidenceManager
from libpv.FileExtractor import FileExtractor
from libpv import FileSystemEnumerator
from libpv import Properties
from wx.propgrid import PropertyGrid

from dfvfs.vfs import tsk_file_entry

logging.basicConfig(level=logging.DEBUG)

#C:\Python27\Lib\site-packages\wx-3.0-msw\wx\dataview.py

# begin wxGlade: dependencies
import wx.propgrid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.MainFrame_menubar = wx.MenuBar()
        self.File = wx.Menu()
        self.Open = wx.MenuItem(self.File, wx.ID_ANY, _("Open Image"), "", wx.ITEM_NORMAL)
        self.File.AppendItem(self.Open)
        self.openLogical = wx.MenuItem(self.File, wx.ID_ANY, _("Open Logical"), "", wx.ITEM_NORMAL)
        self.File.AppendItem(self.openLogical)
        self.File.AppendSeparator()
        self.Exit = wx.MenuItem(self.File, wx.ID_ANY, _("Exit"), "", wx.ITEM_NORMAL)
        self.File.AppendItem(self.Exit)
        self.MainFrame_menubar.Append(self.File, _("File"))
        self.SetMenuBar(self.MainFrame_menubar)
        # Menu Bar end
        self.MainFrame_statusbar = self.CreateStatusBar(1)
        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
        self.window_2 = wx.SplitterWindow(self.window_1_pane_1, wx.ID_ANY)
        self.window_2_pane_1 = wx.Panel(self.window_2, wx.ID_ANY)
        self.tree_fs = wx.TreeCtrl(self.window_2_pane_1, wx.ID_ANY, style=wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT)
        self.window_2_pane_2 = wx.Panel(self.window_2, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        self.notebook_1 = wx.Notebook(self.window_2_pane_2, wx.ID_ANY)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.property_grid_1 = PropertyGrid(self.notebook_1_pane_1, wx.ID_ANY)
        self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        self.window_3 = wx.SplitterWindow(self.window_1_pane_2, wx.ID_ANY)
        self.window_3_pane_1 = wx.Panel(self.window_3, wx.ID_ANY)
        self.list_records = RecordDVListCtrl(self.window_3_pane_1, wx.ID_ANY, style=wx.BORDER_THEME | dataview.DV_ROW_LINES | dataview.DV_VERT_RULES | dataview.DV_MULTIPLE)
        self.window_3_pane_2 = wx.Panel(self.window_3, wx.ID_ANY)
        self.notebook_2 = wx.Notebook(self.window_3_pane_2, wx.ID_ANY, style=wx.NB_MULTILINE)
        self.notebook_2_pane_1 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.text_hex = wx.TextCtrl(self.notebook_2_pane_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.notebook_2_pane_2 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.text_text = wx.TextCtrl(self.notebook_2_pane_2, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OpenSource, self.Open)
        self.Bind(wx.EVT_MENU, self.OpenLogical, self.openLogical)
        self.Bind(wx.EVT_MENU, self.ExitApplication, self.Exit)
        self.Bind(wx.EVT_TREE_ITEM_GETTOOLTIP, self.tree_fs_item_gettooltip, self.tree_fs)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.tree_fs_sel_changed, self.tree_fs)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.tree_fs_item_expanding, self.tree_fs)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.tree_fs_item_activated, self.tree_fs)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSING, self.tree_fs_item_collapsing, self.tree_fs)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.tree_fs_item_collapsed, self.tree_fs)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.tree_fs_item_expanded, self.tree_fs)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.tree_fs_sel_changing, self.tree_fs)
        # end wxGlade
        self._READ_BUFFER_SIZE = 32768

        self._InitRecordPaneMenu()
        self._InitRecordView()
        self.evidenceManager = EvidenceManager(
            self
        )
        self.fileSystemManager = FileSystemEnumerator.FileSystemManager(
            self
        )
        self.LoadIconList()
        dt = MyFileDropTarget(self)
        self.tree_fs.SetDropTarget(dt)

        #Root Containers
        self.tree_fs_root = self.tree_fs.AddRoot('root')

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle(_("Pancake Viewer"))
        self.SetSize((978, 584))
        self.MainFrame_statusbar.SetStatusWidths([-1])
        
        # statusbar fields
        MainFrame_statusbar_fields = [_("MainFrame_statusbar")]
        for i in range(len(MainFrame_statusbar_fields)):
            self.MainFrame_statusbar.SetStatusText(MainFrame_statusbar_fields[i], i)
        self.window_2.SetMinimumPaneSize(20)
        self.window_3.SetMinimumPaneSize(20)
        self.window_1.SetMinimumPaneSize(80)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.tree_fs, 1, wx.EXPAND, 0)
        self.window_2_pane_1.SetSizer(sizer_3)
        sizer_8.Add(self.property_grid_1, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_8)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Properties"))
        sizer_4.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.window_2_pane_2.SetSizer(sizer_4)
        self.window_2.SplitHorizontally(self.window_2_pane_1, self.window_2_pane_2, 300)
        sizer_2.Add(self.window_2, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_2)
        sizer_6.Add(self.list_records, 1, wx.EXPAND, 0)
        self.window_3_pane_1.SetSizer(sizer_6)
        sizer_9.Add(self.text_hex, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1.SetSizer(sizer_9)
        sizer_10.Add(self.text_text, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2.SetSizer(sizer_10)
        self.notebook_2.AddPage(self.notebook_2_pane_1, _("Hex"))
        self.notebook_2.AddPage(self.notebook_2_pane_2, _("Text"))
        sizer_7.Add(self.notebook_2, 1, wx.EXPAND, 0)
        self.window_3_pane_2.SetSizer(sizer_7)
        self.window_3.SplitHorizontally(self.window_3_pane_1, self.window_3_pane_2, 297)
        sizer_5.Add(self.window_3, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_5)
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 173)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def tree_fs_item_changed(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_changed'"
        self.FsTreeItemSelected(event)
        event.Skip()

    def tree_fs_item_expanding(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_expanding' not implemented!"
        event.Skip()

    def tree_fs_item_activated(self, event):  # wxGlade: MainFrame.<event_handler>
        self.FsTreeItemSelected(event)
        event.Skip()

    def tree_fs_item_collapsing(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_collapsing' not implemented!"
        event.Skip()

    def tree_fs_item_collapsed(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_collapsed' not implemented!"
        event.Skip()

    def tree_fs_item_expanded(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_expanded' not implemented!"
        event.Skip()

    def tree_fs_item_changing(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_changing'"
        event.Skip()

    def list_records_item_changed(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'list_records_item_changed' not implemented!"
        self.RecordItemSelected(event)
        event.Skip()

    def list_records_item_activated(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'list_records_item_activated' not implemented!"
        self.RecordItemSelected(event)
        event.Skip()

    def list_records_item_right_click(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'list_records_item_right_click' not implemented!"

        column = event.GetDataViewColumn()

        if column:
            # Get all selected items #
            if self.list_records.HasSelection():
                selected_cnt = self.list_records.GetSelectedItemsCount()
                selected_items = self.list_records.GetSelections()

                # Get right click item #
                right_click_item = event.GetItem()

                # If id is > 0, record is selected
                if right_click_item.ID > 0:
                    self.PopupMenu(self.record_pane_menu)

        event.Skip()

    def OpenSource(self, event):  # wxGlade: MainFrame.<event_handler>
        dlg = wx.FileDialog(
            self,
            message="Choose Image",
            wildcard="All files (*.*)|*.*",
            style=wx.OPEN | wx.CHANGE_DIR
        )

        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                self.EnumerateSource(path)
                print('           %s\n' % path)

        dlg.Destroy()
        event.Skip()

    def ExitApplication(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'ExitApplication' not implemented!"
        event.Skip()

    def LoadIconList(self):
        isz = (16, 16)
        self.tree_fs.icon_list = wx.ImageList(*isz)

        folder = wx.Icon(
            'icons/ic_folder_black_18dp.png',
            wx.BITMAP_TYPE_PNG,
            isz[0],
            isz[1],
        )
        folder_open = wx.Icon(
            'icons/ic_folder_open_black_18dp.png',
            wx.BITMAP_TYPE_PNG,
            isz[0],
            isz[1],
        )

        self.tree_fs.icon_fldridx = self.tree_fs.icon_list.AddIcon(folder)
        self.tree_fs.icon_fldropenidx = self.tree_fs.icon_list.AddIcon(folder_open)
        self.tree_fs.icon_fileidx = self.tree_fs.icon_list.AddIcon(wx.ArtProvider.GetIcon(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))

        self.tree_fs.SetImageList(self.tree_fs.icon_list)

    def EnumerateSource(self,filename):
        self.evidenceManager.EnumerateEvidenceSource(
            filename
        )

    def tree_fs_item_gettooltip(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_item_gettooltip' not implemented!"
        event.Skip()

    def tree_fs_sel_changed(self, event):  # wxGlade: MainFrame.<event_handler>
        self.FsTreeItemSelected(event)
        event.Skip()

    def tree_fs_sel_changing(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'tree_fs_sel_changing' not implemented!"
        event.Skip()

    def _InitRecordView(self):
        #http://docs.wxwidgets.org/3.0/classwx_data_view_ctrl.html
        # self.list_records.AppendBitmapColumn("",0,width=20)
        # self.list_records.AppendTextColumn("Name", 1, width=170)
        # self.list_records.AppendTextColumn("Size", 2, width=170)
        # renderer = MyCustomRenderer(varianttype="long",mode=dataview.DATAVIEW_CELL_EDITABLE)
        # size_column = dataview.DataViewColumn("Size", renderer, 1, width=170)
        # self.list_records.AppendColumn(size_column)

        for c in self.list_records.Columns:
            c.Sortable = True
            c.Reorderable = True

        self.Bind(dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.list_records_item_changed, self.list_records)
        self.Bind(dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.list_records_item_activated, self.list_records)
        self.Bind(dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.list_records_item_right_click, self.list_records)

    def _InitRecordPaneMenu(self):
        # make a menu
        self.record_pane_menu = wx.Menu()

        # Create IDs #
        self.record_pane_popup_id1 = wx.NewId()

        # Create Binds #
        self.Bind(wx.EVT_MENU, self.RecordPaneMenu_ExtractClick, id=self.record_pane_popup_id1)

        # Create Items #
        self.record_pane_menu.Append(self.record_pane_popup_id1, "Extract")

    def RecordPaneMenu_ExtractClick(self,event):
        print 'RecordPaneMenu_ExtractClick'
        dlg = ExtractionDialog(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            # Extraction Process #
            selected_items = self.list_records.GetSelections()

            # Get Filesystem Path Spec #
            i1 = selected_items[0]
            i1_index = self.list_records.GetItemData(i1)
            i1_data = self.list_records.data[i1_index - 1]
            fs_path_spec = i1_data._file_system._path_spec

            # Create our file extractor #
            fileExtractor = FileExtractor(
                fs_path_spec,
                dlg.text_ctrl_outpath.GetValue()
            )

            fileExtractor.start()

            # Extraction Process #
            for item in selected_items:
                data_index = self.list_records.GetItemData(item)
                data = self.list_records.data[data_index - 1]
                fileExtractor.AddFileToQueue(
                    data
                )

            fileExtractor.Finish()

            print(u'File extractor finished!')
            pass

        pass

    def RecordItemSelected(self,event):
        item = event.GetItem()
        value = event.GetValue()
        pos = event.GetPosition()

        pnt = self.list_records.GetItemData(item) - 1 # On a zero index
        node = self.list_records.data[pnt]

        # Set Properties
        self._SetProperties(node)

    def FsTreeItemSelected(self,event):
        print('FsTreeItemSelected')
        item = event.GetItem()
        node = self.tree_fs.GetItemData(item).Data

        # Set Properties
        self._SetProperties(node)

        # Enumerate Folders
        self._EnumFolders(item,node)

        # Populate Records Pane
        self._PopulateRecords(item,node)

        print item

    def _SetProperties(self,node):
        Properties.EnumerateProperties(
            self.property_grid_1,
            node
        )

    def _EnumFolders(self,tree_item,node):
        FileSystemEnumerator.EnumerateNode(
            self,
            tree_item,
            node
        )

    def _PopulateRecords(self,tree_item,file_entry):
        self.list_records.DeleteAllItems()
        self.list_records.ClearData()
        self.list_records.SetCurrentParrent(file_entry)
        if isinstance(file_entry,tsk_file_entry.TSKFileEntry):
            # After a while the file system will close... not sure if this is something I am doing.
            # We need to check if the file system is closed, and open it before we try enumerating the entries
            if not file_entry._file_system._is_open:
                # Not sure if using the TSKFileEntry.path_spec is the best option here... but it works
                file_entry._file_system.Open(file_entry.path_spec)

            for sub_file_entry in file_entry.sub_file_entries:
                self.list_records.InsertRecord(sub_file_entry,file_entry.full_path)

    def OpenLogical(self, event):  # wxGlade: MainFrame.<event_handler>
        print "Event handler 'OpenLogical' not implemented!"
        volumeDialog = LogicalVolumeDialog(
            self,
            -1
        )
        volumeDialog.CenterOnScreen()
        # this does not return until the dialog is closed.
        res = volumeDialog.ShowModal()
        if res == wx.ID_OK:
            volume = volumeDialog.combo_logical_volumes.GetValue()
            self.EnumerateSource(volume)

        volumeDialog.Destroy()

        event.Skip()
# end of class MainFrame

class RecordDVListCtrl(dataview.DataViewListCtrl):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        self.data = []
        self.current_parrent = None

        dataview.DataViewListCtrl.__init__(self, parent, ID, pos, size, style)

        self.AppendBitmapColumn("", 0, width=20)
        self.AppendTextColumn("Name", 1, width=170)
        self.AppendTextColumn("Size", 2, width=170)
        self._SetBitmaps()

    def _SetBitmaps(self):
        self.bmp_folder = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16))
        self.bmp_norm_file = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16))
        self.icons = {
            'Folder': self.bmp_folder,
            'File': self.bmp_norm_file
        }

    def SetCurrentParrent(self,node):
        self.current_parrent = node

    def ClearData(self):
        self.data = []

    def InsertRecord(self,node,path):
        if isinstance(node, tsk_file_entry.TSKFileEntry):
            # Open our tsk file, because it is not guaranteed that node._tsk_file is open
            tskfile = node.GetTSKFile()
            # Get meta for tsk file
            meta = tskfile.info.meta

            # Set data node #
            new_node = copy.copy(node)
            new_node.full_path = "{}/{}".format(path, node.name)
            self.data.append(
                new_node
            )

            icon = self.icons['File']
            if node.IsDirectory():
                icon = self.icons['Folder']

            # data int is key to the node #
            item = self.AppendItem(
                [icon, node.name, str(meta.size)],
                data=len(self.data)
            )

            for dstream in node.data_streams:
                if len(dstream.name) > 0:
                    cname = u'{}:{}'.format(node.name,dstream.name)
                    attr = dstream._tsk_attribute.info
                    meta = node._tsk_file.info.meta

                    # Set data node #
                    new_node = copy.copy(node)
                    new_node.full_path = "{}/{}".format(path,cname)

                    self.data.append(
                        new_node
                    )
                    # data int is key to the node #
                    item = self.AppendItem(
                        [icon, cname, str(attr.size)],
                        data=len(self.data)
                    )
                    pass

class UIntRenderer(dataview.DataViewCustomRenderer):
    def __init__(self, *args, **kw):
        dataview.PyDataViewCustomRenderer.__init__(self, *args, **kw)

class MyCustomRenderer(dataview.PyDataViewCustomRenderer):
    def __init__(self, *args, **kw):
        dataview.PyDataViewCustomRenderer.__init__(self, *args, **kw)
        pass

    def SetValue(self, value):
        self.value = value
        return True

    def GetValue(self):
        # self.log.write('GetValue')
        return self.value

    def GetSize(self):
        # Return the size needed to display the value.  The renderer
        # has a helper function we can use for measuring text that is
        # aware of any custom attributes that may have been set for
        # this item.
        return self.GetTextExtent(self.value)

    def Render(self, rect, dc, state):
        if state != 0:
            self.log.write('Render: %s, %d' % (rect, state))

        if not state & dataview.DATAVIEW_CELL_SELECTED:
            # we'll draw a shaded background to see if the rect correctly
            # fills the cell
            dc.SetBrush(wx.Brush('light grey'))
            dc.SetPen(wx.TRANSPARENT_PEN)
            rect.Deflate(1, 1)
            dc.DrawRoundedRectangleRect(rect, 2)

        # And then finish up with this helper function that draws the
        # text for us, dealing with alignment, font and color
        # attributes, etc
        self.RenderText(self.value,
                        4,  # x-offset, to compensate for the rounded rectangles
                        rect,
                        dc,
                        state  # wxDataViewCellRenderState flags
                        )

    # The HasEditorCtrl, CreateEditorCtrl and GetValueFromEditorCtrl
    # methods need to be implemented if this renderer is going to
    # support in-place editing of the cell value, otherwise they can
    # be omitted.

    def HasEditorCtrl(self):
        self.log.write('HasEditorCtrl')
        return True

    def CreateEditorCtrl(self, parent, labelRect, value):
        self.log.write('CreateEditorCtrl: %s' % labelRect)
        ctrl = wx.TextCtrl(parent,
                           value=value,
                           pos=labelRect.Position,
                           size=labelRect.Size)

        # select the text and put the caret at the end
        ctrl.SetInsertionPointEnd()
        ctrl.SelectAll()

        return ctrl

    def GetValueFromEditorCtrl(self, editor):
        self.log.write('GetValueFromEditorCtrl: %s' % editor)
        value = editor.GetValue()
        return value

    # The LeftClick and Activate methods serve as notifications
    # letting you know that the user has either clicked or
    # double-clicked on an item.  Implementing them in your renderer
    # is optional.

    def LeftClick(self, pos, cellRect, model, item, col):
        self.log.write('LeftClick')
        return False

    def Activate(self, cellRect, model, item, col):
        self.log.write('Activate')
        return False

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        wx.MessageBox(
            u"Items Added:\n{}".format("\n".join(filenames)), #message
            u'Evidence Dropped', #title
            wx.OK | wx.ICON_INFORMATION
        )
        for filename in filenames:
            self.window.EnumerateSource(
                filename
            )

        pass

myEVT_EVIDENCELOADED = wx.NewEventType()
EVT_EVIDENCELOADED = wx.PyEventBinder(myEVT_EVIDENCELOADED, 1)
class EvidenceLoadedEvent(wx.PyCommandEvent):
    """Event to signal that a count value is ready"""
    def __init__(self, etype, eid, value=None):
        """Creates the event object"""
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._value = value

        print 'EVIDENCELOADED EVENT'

    def GetValue(self):
        """Returns the value from the event.
        @return: the value of this event

        """
        print 'EVIDENCELOADED EVENT'