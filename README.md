# profile-insight-api

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](https://opensource.org/licenses/MIT)
<br/>
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/fastapi-%2300C7B7.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![SWI-Prolog](https://img.shields.io/badge/swi--prolog-%233776AB.svg?style=for-the-badge&logo=prolog&logoColor=white)
<br/>
This project is an API built using **Python, FastAPI, and SWI-Prolog**. The API allows users to retrieve questions based on profiles and calculate diagnostic scores based on their answers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Usage](#docker-usage)
- [Contributing](#contributing)
- [Team Members](#team-members)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/PedroSmaxY/profile-insight-api.git
```

2. Install dependencies with pip

```bash
cd profile-insight-api
pip install -r requirements.txt
```

3. Install SWI-Prolog version 8.4.2-1 from the [official website](https://www.swi-prolog.org/download/stable?show=all).

## Usage

1. Start the application:

```bash
uvicorn main:app --reload
```

2. The API will be accessible at `http://localhost:8000`.

## API Endpoints

The API provides the following endpoints:

### 1. Questions

#### 1.1 Get Question

```markdown
GET - /api/v1/questions/{perfil}/{num}/ - Retrieve a question based on profile and question number
```

- Response

```json
{
  "question": "Você se considera uma pessoa competitiva?"
}
```

### 2. Diagnostic

#### 2.1 Calculate Score

```markdown
POST - /api/v1/diagnostic/ - Calculate the diagnostic score based on profile and answers
```

- Request Body

```json
{
  "perfil": "dominancia",
  "answers": [5, 4, 3, 2, 1]
}
```

- Response

```json
{
  "diagnostic": "Alta dominância"
}
```

#### 2.2 Complete Score Calculation

```markdown
POST - /api/v1/diagnostic/complete/ - Calculate the diagnostic score for all profiles based on answers
```

- Request Body

```json
{
  "dominancia": [5, 4, 3, 2, 1],
  "influencia": [4, 3, 2, 1, 5],
  "estabilidade": [3, 2, 1, 5, 4],
  "conformidade": [2, 1, 5, 4, 3]
}
```

- Response

```json
{
  "dominancia": "Alta dominância",
  "influencia": "Influência moderada",
  "estabilidade": "Baixa estabilidade",
  "conformidade": "Alta conformidade"
}
```

## Docker Usage

1. Build the Docker image:

```bash
docker build -t profile-insight-api .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 profile-insight-api
```

3. The API will be accessible at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request to the repository.

When contributing to this project, please follow the existing code style, [commit conventions](https://www.conventionalcommits.org/en/v1.0.0/), and submit your changes in a separate branch.

## Team Members

This project was created with the help of the following team members:

- **Lucas Amaral** - [GitHub](https://github.com/LucasLimaAmaral)
- **Pedro Carvalho** - [GitHub](https://github.com/Phscarvalho)
- **Pedro Novais** - [GitHub](https://github.com/PedroSmaxY)
- **Victor Jacques** - [GitHub](https://github.com/Victor-Jacques)
