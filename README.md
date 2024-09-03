# Personal Portfolio Website

[![Live Site](https://img.shields.io/badge/Live-alinoureddine.tech-blue)](https://www.alinoureddine.tech)
[![Version](https://img.shields.io/badge/Version-1.0-green)]()
[![Built with Flask](https://img.shields.io/badge/Built%20with-Flask-lightgrey)]()


[Visit the Live Site](https://www.alinoureddine.tech)

## Overview

This project is a personal portfolio website built to showcase my projects and skills as a software developer. It features a responsive design, a contact form with backend processing, and a database for storing submissions.

## Key Features

- Responsive UI design built with HTML, CSS, and Bootstrap
- Interactive project showcase with detailed descriptions
- Contact form with client-side and server-side validation
- Flask backend to serve pages and process contact form data
- SQLite database to store and retrieve contact form submissions
- Data export functionality (100+ form submissions exported to CSV)
- Automated git pull functionality for easy updates
- Deployed live on PythonAnywhere

## Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python 3.6
- Flask 2.0.3
- Jinja2 3.0.3

### Database
- SQLite

### Version Control and Deployment
- Git
- GitPython 3.1.43
- PythonAnywhere for hosting

## Project Structure

```
portfo/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── resume.pdf
│
├── templates/
│   ├── index.html
│   ├── projects.html
│   ├── contact.html
│   └── thankyou.html
│
├── scripts/
│   ├── run_app.ps1
│   ├── run_tests.ps1
│   └── update_dependencies.ps1
│
├── tests/
│   └── test_server.py
│
├── .github/
│   └── workflows/
│       └── flask_ci.yml
│
├── server.py
├── requirements.txt
├── database.csv
└── README.md
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/portfo.git
   ```

2. Navigate to the project directory:
   ```
   cd portfo
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python server.py
   ```

   Or use the provided script:
   ```
   .\scripts\run_app.ps1
   ```

6. Open a web browser and go to `http://localhost:5000`

## Running Tests

To run the tests, use the following command:
```
.\scripts\run_tests.ps1
```

## Updating Dependencies

To update all dependencies and refresh the requirements.txt file, run:
```
.\scripts\update_dependencies.ps1
```

## Continuous Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/flask_ci.yml`. It automatically runs tests on every push and pull request to the main branch.

## Deployment

The site is deployed on PythonAnywhere. To deploy updates:

1. Push changes to the GitHub repository
2. Log in to PythonAnywhere
3. Use the `/git_update` endpoint to pull the latest changes
4. Reload the web app

## Future Enhancements

- Add a blog section to share tech articles
- Implement a dark mode toggle
- Create a project filter system
- Add internationalization support

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Alinoureddine1/portfo/issues).


Project Link: [https://github.com/Alinoureddine1/portfo](https://github.com/Alinoureddine1/portfo)
