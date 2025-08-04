from sqlalchemy import create_engine

# Test different connection strings
test_urls = [
    "postgresql://postgres:Sparsh1200%40@localhost:5432/signup_db"
]

for url in test_urls:
    try:
        print(f"Testing: {url}")
        engine = create_engine(url)
        connection = engine.connect()
        print(engine)
        connection.close()
        break
    except Exception as e:
        print(f"Failed: {type(e).__name__}: {e}")
        print()