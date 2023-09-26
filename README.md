
# TXT Spider Project

Personal spider project for study.

## Milestones

The development of this project is planned to be executed in several key milestones:

### Milestone 1: Initial Setup and Core Functionality

1. Project setup and configuration
2. Scrapy spider for basic web scraping
3. Initial database models
4. Logging system

### Milestone 2: Advanced Features

1. Implement Scrapy-Selenium and Scrapy-Splash for dynamic web scraping
2. Advanced database models and pipelines
3. Real-time status monitoring using FastAPI

### Milestone 3: Testing and Deployment

1. Unit and integration tests
2. Dockerization and initial deployment
3. Setup CI/CD pipeline

### Milestone 4: Additional Tools and Features

1. Auxiliary tool for adding new data sources
2. Further optimizations and feature additions



## Technology Stack

1. **Web Scraping Framework**: Scrapy (Python) - For web scraping and parsing.
2. **Interactive Web Scraping**: Scrapy-Selenium & Scrapy-Splash - For handling dynamic pages and complex interactions.
3. **Data Storage**: SQLAlchemy (Python) with SQLite or PostgreSQL - For storing scraped data.
4. **Task Queue**: Celery (Python) - For managing scraping tasks.
5. **Real-time Status Display**: FastAPI (Python) with WebSocket - For displaying real-time scraping status.
6. **Logging**: Loguru (Python) - For comprehensive logging.
7. **Frontend**: HTML, CSS, JavaScript (Optional) - If a web interface is needed.
8. **Auxiliary Tools**: Custom Python module - For simplifying the addition of new data sources.
9. **Testing Framework**: Pytest (Python) - For writing and running unit and integration tests.
10. **Continuous Integration/Continuous Deployment (CI/CD)**: Jenkins, GitLab CI, or GitHub Actions - For automated testing and deployment.
11. **Containerization**: Docker - For packaging the application and dependencies.
12. **Configuration Management**: Ansible or Kubernetes - For automating configuration and server management.

## Component Design

1. **Scrapy Spider**: Responsible for web scraping and parsing.
    - Config Files: For defining the scraping logic and data model for different websites.
2. **Interactive Spider Module**: Uses Scrapy-Selenium and Scrapy-Splash for handling websites requiring JavaScript rendering or complex interactions.
3. **Data Model**: Uses SQLAlchemy for defining a flexible data storage model.
    - Supports multiple data sources and data types.
4. **Task Management**: Uses Celery for managing scraping tasks.
    - Supports scheduled and real-time tasks.
5. **Status Display**: Uses FastAPI/Console and WebSocket for real-time status display.
    - Displays ongoing tasks and historical information.
6. **Logging**: Use Loguru for logging for diagnostics and performance optimization.
    - Supports multi-level logging
    - can save logs as files
    - can send logs to a logging server.
7. **Auxiliary Tool or Module**:
    - Data Source Configuration: For simplifying the process of adding new data sources.
    - Template Selection: For selecting an appropriate scraping template based on website characteristics.
    - Custom Settings: Provides a graphical or command-line interface for entering specific website settings.
8. **Testing**: Perform comprehensive testing before adding the new data source to ensure accurate data scraping.
9. **Build**: Use Docker to build application containers.
10. **Deployment**: Use Ansible or Kubernetes to automate the deployment of the application
11. **Monitoring and Adjustment**: Use FastAPI and WebSocket for real-time monitoring and make further optimizations as necessary.


## Project Directory Structure

Designed for ease of adding new websites and to have a modular design for decoupling between different modules.

```
txt_spider/
|-- scrapy.cfg
|-- requirements.txt
|-- Dockerfile
|-- README.md
|-- txt_spider/
|   |-- __init__.py
|   |-- items.py
|   |-- middlewares.py
|   |-- pipelines.py
|   |-- settings.py
|   |-- spiders/
|   |   |-- __init__.py
|   |   |-- example_spider.py
|-- logs/
|   |-- access.log
|   |-- error.log
|-- db_models/
|   |-- __init__.py
|   |-- example_model.py
|-- utils/
|   |-- __init__.py
|   |-- common_utils.py
|-- tests/
|-- docker-compose.yml
|-- .gitlab-ci.yml (or Jenkinsfile or .github/workflows)
```

## Usage

### Installation, Running, and Usage

1. Clone the repository: `git clone https://github.com/realm520/txt_spider.git`
2. Navigate to the project directory: `cd txt_spider`
3. Install dependencies: `pip install -r requirements.txt`
4. Run a spider: `scrapy crawl singaporepool`

### Development Environment, Packaging, and Deployment

1. Install `poetry`
2. Install development dependencies: `poetry install`
3. Enter venv: `poetry shell`
4. Package the application: `python setup.py sdist bdist_wheel`
5. Deploy using Docker: `docker-compose up`

### Add new spider

1. Generate spider file by scrapy
```
scrapy genspider singaporepool "https://online.singaporepools.com/cn/sports/category/1/football"
```

## Update Component

### Update chromedriver

1. Download from https://googlechromelabs.github.io/chrome-for-testing/
2. Replace zip file under "bin" directory