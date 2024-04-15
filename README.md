# Multiple-Embedded-Browsers-in-PyQt5-With-Automation
![VE Project 4-1](https://github.com/Rafayjiwani/Multiple-Embedded-Browsers-in-PyQt5-With-Automation/assets/51723292/29bd0a97-4d8d-4443-9c33-5814e33ccc1b)
Multiple Embedded Browsers in PyQt5 With Automation Supported and Sidebar Management

#### Introduction

In modern software development, integrating web browsing capabilities directly into desktop applications has become increasingly popular. PyQt5, a Python library for creating graphical user interfaces, offers robust support for embedding web views within applications. This repository serves as both a guide and an implementation example for seamlessly integrating browsers into your PyQt5 projects.

#### Features

- **Integration**: Embed web content directly within your PyQt5 application's user interface.
- **Customization**: Customize the browsing experience to match your application's aesthetics and branding.
- **Interactivity**: Allow users to interact with web content seamlessly without resorting to external browsers.
- **Control**: Maintain control over user interactions and enforce security measures within the embedded browser environment.

#### Getting Started

To begin using PyQt5 Embedded Browser, follow these steps:

1. **Installation**: Ensure PyQt5 is installed in your Python environment. You can install it via pip:

    ```
    pip install PyQt5
    ```

2. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```
    git clone https://github.com/Rafayjiwani/Multiple-Embedded-Browsers-in-PyQt5-With-Automation.git
    ```

3. **Run the Demo**: Navigate to the repository directory and execute the demo script to see the embedded browser in action:

    ```
    cd repo
    python main.py
    ```

#### Usage

To embed a browser within your PyQt5 application, follow these steps:

1. **Import the Browser Class**: Import the `Browser` class from the provided module into your Python script.

    ```python
    from embedded_browser import Browser
    ```

2. **Instantiate the Browser**: Create an instance of the `Browser` class within your application's UI layout.

    ```python
    browser = Browser()
    ```

3. **Integrate with UI**: Add the browser widget to your application's layout to display it to the user.

    ```python
    layout.addWidget(browser)
    ```

#### JavaScript Automation

One powerful feature of embedded browsers is the ability to automate interactions with web content using JavaScript. This capability opens up a wide range of possibilities for enhancing user experiences and streamlining workflows within your PyQt5 application.

```python
def on_load_finished(self, ok):
    """
    Triggered when the webpage is fully loaded
    """
    if ok:
        # Define JavaScript code to perform a search
        script = """
            let searchInput = document.querySelector("[name='q']");
            searchInput.focus();
            searchInput.click();
            searchInput.value = 'Your search query here';
            searchInput.click();
            let btn = document.querySelector('[aria-label="Google Search"]');
            btn.click();
        """

        # Execute the JavaScript code in the embedded browser
        self.run_javascript(script)
```

By leveraging JavaScript automation, you can programmatically interact with web content and perform tasks such as form submissions, data retrieval, and more, directly within your PyQt5 application.

#### Examples

Explore the `main.py` script included in this repository for a comprehensive example of embedding a browser using PyQt5 and JavaScript automation. Additionally, refer to the provided documentation for detailed usage instructions and customization options.

#### Contributions

Contributions to this project are welcome! Whether you're fixing bugs, adding features, or improving documentation, your contributions help make PyQt5 Embedded Browser even better. To contribute, fork this repository, make your changes, and submit a pull request.

#### License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Rafayjiwani/Multiple-Embedded-Browsers-in-PyQt5-With-Automation/blob/master/LICENSE) file for details.

#### Acknowledgments

Special thanks to the PyQt5 community for their continuous support and contributions to the project.If you encounter any issues or have suggestions for improvement, feel free to open an issue on the repository. Happy browsing! 🚀
