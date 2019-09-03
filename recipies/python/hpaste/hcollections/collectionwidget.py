if(__name__=='__main__'):
    import os
    os.environ['PATH']+='/studio/tools/hou/builds/hfs16.0.600/bin'
    from PySide2.QtCore import *
    from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools, QtUiTools
    
from logger import defaultLogger as log

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from QDropdownWidget import QDropdownWidget

import collectionbase


class SnippetCollectionModel(QAbstractTableModel):
	def __init__(self,collectionsList,parent=None,metadataExposedKeys=()):
		assert isinstance(metadataExposedKeys,list) or isinstance(metadataExposedKeys,tuple), 'metadataExposeKeys should be a collection of string keys'

		super(SnippetCollectionModel,self).__init__(parent)
		self.__collections=list(collectionsList)
		self.__itemList=[]

		self.__metadataExposedKeys=tuple(metadataExposedKeys)

		self.rescanCollections()

	def addCollection(self,collection):
		assert isinstance(collection,collectionbase.CollectionBase),'collection must be a collection'
		self.__collections.append(collection)
		tmplist=collection.list()
		if(len(tmplist)==0):return
		nextid=len(self.__itemList)
		self.beginInsertRows(QModelIndex(),nextid,nextid+len(tmplist)-1)
		self.__itemList+=tmplist
		self.endInsertRows()

	def addItemToCollection(self, collection, desiredName, description, content, public, metadata=None):
		if(collection not in self.__collections):raise ValueError('collection must belong to the model')
		access=collectionbase.CollectionItem.AccessType.public if public else collectionbase.CollectionItem.AccessType.private
		newitem=collection.addItem(desiredName, description, content, access,metadata=metadata)

		nextid=len(self.__itemList)
		self.beginInsertRows(QModelIndex(),nextid,nextid)
		self.__itemList.append(newitem)
		self.endInsertRows()

	def removeRows(self,row,count,parent):
		lastrow=row+count-1
		if(parent!=QModelIndex() or count==0 or  lastrow>=self.rowCount(parent)):return False

		self.beginRemoveRows(parent, row,lastrow)
		everythingIsBad=False
		for i in xrange(count):
			try:
				self.__itemList[row+i].removeSelf()
			except:
				everythingIsBad=True
				break
		else:
			self.__itemList=self.__itemList[:row]+self.__itemList[row+count:]
		self.endRemoveRows()

		return not everythingIsBad

	def collections(self):
		return tuple(self.__collections)

	def rescanCollections(self):
		if(len(self.__itemList)>0):
			self.beginRemoveRows(QModelIndex(),0,len(self.__itemList)-1)
			self.__itemList=[]
			self.endRemoveRows()

		templist=[]
		for collection in self.__collections:
			templist+=collection.list()

		self.beginInsertRows(QModelIndex(),0,len(templist)-1)
		self.__itemList=templist
		self.endInsertRows()

	def columnCount(self,index=None):
		if (index is None): index = QModelIndex()
		if (index.isValid()): return 0
		#name,desc,id + metadatakeys
		return 3+len(self.__metadataExposedKeys)

	def rowCount(self,index=None):
		if (index is None): index = QModelIndex()
		if (index.isValid()): return 0
		return len(self.__itemList)

	def index(self,row,col,parent):
		if(parent!=QModelIndex()):
			return QModelIndex()
		return self.createIndex(row,col,self.__itemList[row])

	def data(self,index, role = Qt.DisplayRole):
		if(role==Qt.DisplayRole):
			if(index.column() == 0):
				return self.__itemList[index.row()].name()
			elif(index.column() == 1):
				return self.__itemList[index.row()].description()
			elif(index.column() == 2):
				return self.__itemList[index.row()].id()
			else:
				metadata=self.__itemList[index.row()].metadata()
				key=self.__metadataExposedKeys[index.column()-3]
				if(key in metadata): return metadata[key]
				else: return ''
		return None


class CollectionWidget(QDropdownWidget):
	def __init__(self,parent=None,metadataExposedKeys=()):
		super(CollectionWidget,self).__init__(parent)
		self.setModel(SnippetCollectionModel([],self,metadataExposedKeys))

		self.ui.mainView.setContextMenuPolicy(Qt.CustomContextMenu)
		self.ui.mainView.customContextMenuRequested.connect(self.showContextMenu)

	def rescanCollections(self):
		self.model().rescanCollections()

	def addCollection(self,collection):
		self.model().addCollection(collection)

	def _addItem(self,collection):
		log('_addItem should be reimplemented in subclass to do what is needed in any specific situation',3)
		#not raising cuz this is called deep through signal-slot mech, that cause exceptions to be fucked somewhere on the way
		#raise NotImplementedError('This method should be overriden in subclasses to implement desired behaviour')

	def _itemInfo(self,index):
		log('_itemInfo should be reimplemented in subclass to do what is needed in any specific situation',3)
		item=index.internalPointer()
		stuff=vars(item)
		for v in stuff:
			log(v+' : '+repr(stuff[v]),2)

	def _renameItem(self,index):
		log('_renameItem should be reimplemented in subclass to do what is needed in any specific situation', 3)

	def _changeAccess(self,index):
		log('_changeAccess should be reimplemented in subclass to do what is needed in any specific situation', 3)

	def _replaceContent(self,index):
		log('_renameItem should be reimplemented in subclass to do what is needed in any specific situation', 3)

	def _confirmRemove(self,index):
		#reimplement this to add smth like confirmation window if needed
		return True

	def __removeItem(self,index):
		if(self._confirmRemove(index)):
			self.model().removeRows(index.row(),1,QModelIndex())


####Slots
	@Slot(QPoint)
	def showContextMenu(self,pos):
		menu=QMenu('orders, captain?',self)
		newaction=menu.addAction('choose this')
		newaction.triggered.connect(self.accept)

		sidemenu = menu.addMenu('collections')
		for col in self.model().collections():
			colmenu=sidemenu.addMenu(col.name())
			if(col.readonly()):
				newaction=colmenu.addAction('collection is READONLY')
				newaction.setEnabled(False)
			else:
				newaction=colmenu.addAction('add selected nodes')
				newaction.setData((col))
				newaction.triggered.connect(lambda x=col: self._addItem(x))
		menu.addSeparator()

		if(self.ui.mainView.currentIndex().isValid()):
			cindex=self._mapToSource(self.ui.mainView.currentIndex())
			item=cindex.internalPointer()
			sidemenu = menu.addMenu('item')
			newaction = sidemenu.addAction('info')
			newaction.triggered.connect(lambda x=cindex: self._itemInfo(x))
			if(not item.readonly()):
				sidemenu.addSeparator()
				newaction = sidemenu.addAction('rename')
				newaction.triggered.connect(lambda x=cindex:self._renameItem(x))
				newaction = sidemenu.addAction('change access')
				newaction.triggered.connect(lambda x=cindex:self._changeAccess(x))
				newaction = sidemenu.addAction('replace content')
				newaction.triggered.connect(lambda x=cindex:self._replaceContent(x))
				#newaction.setEnabled(False)
				#TODO: automatically enable stuff if subclass overrides item methods!
				sidemenu.addSeparator()
				newaction = sidemenu.addAction('remove item')
				newaction.triggered.connect(lambda x=cindex: self.__removeItem(x))


		menu.popup(self.mapToGlobal(pos))
		menu.aboutToHide.connect(menu.deleteLater)

####TESTING
if(__name__=='__main__'):
	class FakeCollection(collectionbase.CollectionBase):
		def __init__(self):
			super(FakeCollection,self).__init__()
			self.__coll=[collectionbase.CollectionItem(self,'item %s'%x,'fat %s'%(x*2),'testnoid',x%2,x%4<2,metadata={'raw_url':'https://fuck','nettype':'WOOF'}) for x in xrange(100)]

		def name(self):
			return 'testname'

		def list(self):
			return self.__coll

		def removeItem(self,item):
			self.__coll.remove(item)
			item._invalidate()

	import sys
	from os import path
	from githubcollection import GithubCollection
	#QCoreApplication.addLibraryPath(r'C:\Program Files\Side Effects Software\Houdini 16.0.600\bin\Qt_plugins')
	
	qapp=QApplication(sys.argv)

	add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
	QCoreApplication.addLibraryPath(add_path)
    
	#testToken = ''
	#with open(path.join(path.dirname(path.dirname(path.dirname(__file__))), 'githubtoken.tok'), 'r') as f:
	#	testToken = f.read()
	#	testToken = testToken.replace('\n', '')
	#print(testToken)
	col = FakeCollection()

	wid=CollectionWidget(metadataExposedKeys=('raw_url','nettype'))
	wid.move(800, 400)
	wid.addCollection(col)
	wid.accepted.connect(lambda x: log('dialog accepted "%s"'%x.name()))
	wid.finished.connect(lambda : qapp.quit())
	wid.show()
	sys.exit(qapp.exec_())
