# Alodokter Scraper

[![Code](https://img.shields.io/badge/Code-Python_3.11.0-1B9D73?style=flat&logo=python)](https://python.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Package Manager](https://img.shields.io/badge/Package_Manager-uv-1B9D73?style=flat&logo=python)](https://github.com/astral-sh/uv)

This project is a scraping tool designed to extract question-answers from [Alodokter.com](alodokter.com).

## Features
- Extract `topic` and `url` from [Alodokter Topik](https://www.alodokter.com/komunitas/topik). Sample JSON result:
```JSON
{
 "topic": "Ablasi Retina",
 "url": "https://www.alodokter.com/komunitas/topic-tag/ablasi-retina"
}
```

- Extract question-answers for all the topics. Sample JSON result:
 ```JSON
{
 "topic_category": "Ablasi Retina",
 "question_title": "Mata hanya melihat warna putih setelah operasi ablasi retina dan katarak",
 "question_body": "Alo dok, assalamualaikum wr wb. Sekitar 2 bulan yg lalu ayah saya telah menjalani operasi ablasi retina.....",
 "question_date": "2021-10-25 11:54:00",
 "doctor_name": "dr. Riza Marlina",
 "answer_body": "Alo, selamat siang\nkeluhan mata kabur kondisi ini dapat disebabkan oleh berapa hal seperti....",
 "answer_date": "2021-10-25 13:05:00"
}
```

## Requirements

- Python >= 3.11.0
- [uv](https://docs.astral.sh/uv/) >= 0.6
- [Tools] = [ruff](https://docs.astral.sh/ruff/) 

## Installations
Use the package manager [uv](https://docs.astral.sh/uv/) to install dependencies.

```bash
uv sync
```

## Usage

Returns the result in JSON format:
```bash
uv run scrapy crawl <spider name> -o filename.json
```

Returns the result in CSV format:
```bash
uv run scrapy crawl <spider name> -o filename.csv
```
