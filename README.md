rag-eval/
│
├── README.md
├── pyproject.toml / requirements.txt
├── .env.example
│
├── config/
│   ├── settings.yaml
│   ├── metrics.yaml
│   └── endpoints.yaml
│
├── data/
│   ├── raw/
│   │   └── input.csv
│   │   └── input.json
│   │   └── input.xlsx
│   ├── processed/
│   └── schemas/
│       └── dataset_schema.json
│
├── src/│
│   ├── clients/
│   │   └── rag_client.py
│   │
│   ├── datasets/
│   │   ├── loader.py
│   │   ├── validator.py
│   │   └── preprocessing.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── runner.py
│   │   └── thresholds.py
│   │
│   ├── ragas/
│   │   ├── sample_builder.py
│   │   └── evaluate.py
│   │
│   ├── reporting/
│   │   ├── exporters.py
│   │   └── summary.py
│   │
│   ├── utils/
│   │   ├── chunking.py
│   │   ├── logging.py
│   │   └── retries.py
│   │
│   └── main.py
│
├── tests/
│   ├── unit/
│   └── integration/
│
└── outputs/
    ├── runs/
    └── reports/