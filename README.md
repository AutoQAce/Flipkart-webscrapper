# Web Scraping Project

## Overview

This project is a web scraping application built using Python, Flask, Selenium, and BeautifulSoup. It scrapes product reviews, including the product name, customer name, rating, comment heading, and full comment. The data is stored in a MongoDB database. The application is containerized using Docker and hosted on Azure using Azure Functions with continuous integration set up on Azure DevOps.

## Features

- **Web Scraping**: Extracts product review information from websites.
- **Backend**: Built with Flask to handle HTTP requests and responses.
- **Data Parsing**: Utilizes Selenium and BeautifulSoup for web scraping.
- **Database**: MongoDB is used to store the scraped data.
- **Containerization**: Docker is used to containerize the application.
- **Hosting**: Hosted on Azure Functions.
- **CI/CD**: Continuous Integration and Deployment are set up using Azure DevOps.

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework for building the application.
- **Selenium**: Web scraping library to interact with web pages.
- **BeautifulSoup**: Web scraping library to parse HTML content.
- **MongoDB**: NoSQL database to store the scraped data.
- **Docker**: Containerization platform.
- **Azure Functions**: Serverless computing service to host the application.
- **Azure DevOps**: CI/CD platform for automated deployment.

## Setup and Installation

### Prerequisites

- Python 3.x
- Docker
- Azure account
- Azure CLI
- MongoDB

### Local Development

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure MongoDB**
    goto Mongodb.com and create few cluster and database for the use.


### Docker Setup

1. **Build the Docker image**
    ```sh
    docker build -t flipkartwebscrapper .
    ```

2. **Run the Docker container**
    ```sh
    docker run -d -p 5000:5000 flipkartwebscrapper
    ```

### Deploy to Azure

1. **Login to Azure**
    ```
    az login
    ```

2. **Create Azure resources**
    - Create an Azure Container Registry (ACR)
    - Create an Azure Function App

3. **Push Docker image to ACR**
    ```
    az acr credential show --name <ACR Name> --output table
    sh ./build_docker.sh
    ```

4. **Configure Azure Function App**
    Update the Azure Function App settings to use the Docker image from ACR.

### Continuous Integration and Deployment

1. **Setup Azure DevOps**
    - Create a new project in Azure DevOps.
    - Set up a new pipeline connecting to your GitHub repository.

2. **Configure the pipeline**
    - Add tasks for building the Docker image.
    - Push the Docker image to ACR.
    - Deploy the image to the Azure Function App.

## Usage

- Access the web application via the Azure Function App URL.
- Use the provided endpoints to initiate web scraping and retrieve data.
