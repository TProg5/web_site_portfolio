# web_site_portfolio
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>


<!-- SPOILER -->
## Spoiler

Some of the JavaScript animations and CSS styles were generated with the help of neural networks. However, the main focus of this project is the **BACKEND**, which I built myself


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Spoiler">Spoiler</a>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Run-the-Application">Run-the-Application</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project was originally created as a learning environment for learning internationalization (i18n) in Python using FastAPI, Jinja2 and Babel. I wanted to learn how to work with internationalization, get to know FastAPI better, and work on improving API creation. This is where I used Middleware for the first time.

At the moment and in the future, the project will serve as the basis for my personal portfolio. It will be constantly updated, adding new features and improving the design. All changes will be reflected here on GitHub.

It is both a learning platform and a portfolio showcase.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The main technologies and libraries used in this project:

- [FastAPI](https://fastapi.tiangolo.com/) — modern, fast (high-performance) web framework for building APIs with Python 3.7+
- [Starlette](https://www.starlette.io/) - Because FastAPI is an add-on over Starlette, I used Starlette specifically to create Middleware.
- [Jinja2](https://jinja.palletsprojects.com/) — templating engine for Python, used for generating HTML pages
- [Babel](https://babel.pocoo.org/en/latest/) — internationalization and localization library


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Create and activate a virtual environment:
* pip
  ```bash
    python -m venv .venv
    source .venv/bin/activate       # on Linux/macOS
    .venv\Scripts\activate          # on Windows
  ```

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/TProg5/web_site_portfolio.git
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your settings:
   ```dotenv
    # Localization
    DEFAULT_LOCALE="en"
    SUPPORTED_LOCALE="en,ru"

    # Telegram Bot Config
    BOT_TOKEN="your_bot_token"
    CHAT_ID="your_chat_id"  

   ```

### Babel Commands

Babel is used for handling translations (i18n). Below are the most common commands you'll need during development.
#### Extract translation strings:
Scans your project for translatable strings and generates a `.pot` template:
```bash
pybabel extract -F app/translations/babel.cfg -o app/translations/messages.pot .
```

#### Initialize languages (optional):
Use this only if you want to add new languages manually:
```bash
# English
pybabel init -i app/translations/messages.pot -d app/translations -l en

# Russian
pybabel init -i app/translations/messages.pot -d app/translations -l ru
```
This will create .po files inside app/translations/{lang}/LC_MESSAGES/.

#### Compile translations:
If you already have .po files (e.g. cloned the repo or edited them), compile them into .mo files with:

```bash
pybabel compile -d app/translations
```

### Run the Application
   Option 1 – Run as a module:
   ```bash
   python -m app.main
   ```
   Option 2 – Run with uvicorn (FastAPI recommended):
   ```bash
   uvicorn app.main:app --reload
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<img width="768" height="906" alt="image" src="https://github.com/user-attachments/assets/10d0d86e-afec-47d2-bb81-02b4ba4e3927" />


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the `MPL-2.0 license`. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
- [Email](mailto:ohotnkovtimur.dev@gmail.com)
- [Telegram](https://t.me/Mr_OmNom)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
Thanks for the `README` template
* [README TEMPLATE](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


