# Setup for Development

1. Create virtual environment:
```bash
python3 -m virtualenv venv
```

2. Activate environment:
```bash
./venv/Scripts/activate.bat
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Скопируйте .env.local в .env.

5. Run the web server:
```bash
uvicorn app.main:app --reload
```

6. Generate requirements.txt
```bash
pip install pigar
pigar generat
``