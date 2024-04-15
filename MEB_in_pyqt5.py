import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QtWidgets.QMainWindow):
    def __init__(self, size=[800,600], frame=None, centralWidget=None, default_url='https://www.google.com', backButton=True, forwardButton=True, topBar=True):
        """
            Initialize the browser GUI and connect the events
        """

        self.showBackButton = backButton
        self.showForwardButton = forwardButton
        self.showTopBar = topBar

        super().__init__()
        if (frame == None):
            self.frame = QtWidgets.QFrame()
        else:
            self.frame = frame

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)  # Set the margins here

        self.gridLayout = QtWidgets.QVBoxLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # Set the margins here
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        if (self.showTopBar):
            self.tb_url = QtWidgets.QLineEdit()
        if (self.showBackButton):
            self.bt_back = QtWidgets.QPushButton()
        if (self.showForwardButton):
            self.bt_ahead = QtWidgets.QPushButton()

        if (self.showBackButton):
            self.bt_back.setIcon(QtGui.QIcon.fromTheme("go-previous"))
        if (self.showForwardButton):
            self.bt_ahead.setIcon(QtGui.QIcon.fromTheme("go-next"))

        if (self.showBackButton):
            self.horizontalLayout.addWidget(self.bt_back)
        if (self.showForwardButton):
            self.horizontalLayout.addWidget(self.bt_ahead)
        if (self.showTopBar):
            self.horizontalLayout.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QWebEngineView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)

        if (self.showTopBar):
            self.tb_url.returnPressed.connect(self.browse)
        if (self.showBackButton):
            self.bt_back.clicked.connect(self.html.back)
        if (self.showForwardButton):
            self.bt_ahead.clicked.connect(self.html.forward)
        self.html.urlChanged.connect(self.url_changed)

        self.default_url = default_url
        if (self.showTopBar):
            self.tb_url.setText(self.default_url)
        self.open(self.default_url)

        # Set size policy to expanding
        self.centralwidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Connect to the loadFinished signal of the QWebEngineView
        self.html.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        """
        Triggered when the webpage is fully loaded
        """
        if ok:

            script = """
                let searchInput = document.querySelector("[name='q']");
                searchInput.focus();
                searchInput.click();
                searchInput.value = 'Rafay Asif Jiwani';
                searchInput.click();
                let btn = document.querySelector('[aria-label="Google Search"]');
                btn.click();
            """

            self.run_javascript(script)

    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        if (self.showTopBar):
            url = self.tb_url.text() if self.tb_url.text() else self.default_url
            self.html.load(QtCore.QUrl(url))
            self.html.show()
        else:
            pass

    def url_changed(self, url):
        """
            Triggered when the url is changed
        """
        if (self.showTopBar):
            self.tb_url.setText(url.toString())
        else:
            pass

    def open(self, url):
        self.html.load(QtCore.QUrl(url))
        self.html.show()

    def run_javascript(self, script):
        """
        Run JavaScript code in the browser.
        """
        self.html.page().runJavaScript(script)

class BrowserListItem(QtWidgets.QWidget):
    def __init__(self, browser_instance, browser_instances, remove_callback, parent=None):
        super().__init__(parent)

        self.browser_instance = browser_instance
        self.browser_instances = browser_instances
        self.remove_callback = remove_callback

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Set the margins here

        self.browser_label = QtWidgets.QLabel(f"Browser {len(self.browser_instances)}")
        layout.addWidget(self.browser_label)

        remove_button = QtWidgets.QPushButton("X")
        remove_button.setStyleSheet("color: red; font-weight: bold;")
        remove_button.clicked.connect(self.remove_browser)
        layout.addWidget(remove_button)

    def remove_browser(self):
        self.remove_callback(self.browser_instance)

    def set_active(self, active):
        if active:
            self.browser_label.setStyleSheet("font-weight: bold; color: blue;")
        else:
            self.browser_label.setStyleSheet("")

class BrowserListItemWidget(QtWidgets.QListWidgetItem):
    def __init__(self, browser_list_item):
        super().__init__()
        self.widget = browser_list_item

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Embedded Browser in Main Window with Sidebar")
        self.setGeometry(100, 100, 800, 600)

        self.sidebar = QtWidgets.QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)

        self.open_browser_btn = QtWidgets.QPushButton("Open Browser")
        self.open_browser_btn.clicked.connect(self.open_browser)
        self.sidebar_layout.addWidget(self.open_browser_btn)

        self.browser_list = QtWidgets.QListWidget()  # Use QListWidget for browser list
        self.browser_list.itemClicked.connect(self.display_browser)  # Connect itemClicked signal
        self.sidebar_layout.addWidget(self.browser_list)

        self.browser_instances = []
        self.browser_container = QtWidgets.QStackedWidget()

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.browser_container)

        self.current_browser = None

    def open_browser(self):
        browser_instance = Browser(default_url='https://www.google.com/', forwardButton=False, backButton=False, topBar=False)
        self.browser_instances.append(browser_instance)

        browser_list_item = BrowserListItem(browser_instance, self.browser_instances, self.remove_browser)  # Create browser list item
        list_item = BrowserListItemWidget(browser_list_item)  # Create a new item for the list
        list_item.setSizeHint(QtCore.QSize(200, 40))  # Set size hint for item
        self.browser_list.addItem(list_item)  # Add item to list
        self.browser_list.setItemWidget(list_item, browser_list_item)  # Set browser list item as widget for list item

        self.switch_browser(browser_instance)

    def display_browser(self, item):
        index = self.browser_list.row(item)  # Get index of clicked item
        browser_instance = self.browser_instances[index]  # Get corresponding browser instance
        self.switch_browser(browser_instance)

    def switch_browser(self, browser_instance):
        if self.current_browser:
            self.browser_container.removeWidget(self.current_browser)
            list_item = self.browser_list.item(self.browser_instances.index(self.current_browser))
            list_item.widget.set_active(False)  # Deactivate the current browser item

        self.current_browser = browser_instance
        self.browser_container.addWidget(browser_instance)
        self.browser_container.setCurrentWidget(browser_instance)
        list_item = self.browser_list.item(self.browser_instances.index(self.current_browser))
        list_item.widget.set_active(True)  # Activate the current browser item

    def remove_browser(self, browser_instance):
        if browser_instance in self.browser_instances:
            index = self.browser_instances.index(browser_instance)
            if self.current_browser == browser_instance:
                if len(self.browser_instances) > 1:
                    if index == 0:
                        self.switch_browser(self.browser_instances[1])
                    else:
                        self.switch_browser(self.browser_instances[index - 1])
                else:
                    self.current_browser = None

            item = self.browser_list.item(index)
            self.browser_instances.remove(browser_instance)  # Remove from browser_instances first
            self.browser_list.takeItem(index)  # Then remove from browser_list
            browser_instance.close()  # Close the browser instance

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
