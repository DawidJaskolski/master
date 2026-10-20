import sys
from qdrant_client import QdrantClient
import psycopg

def test_qdrant():
    print("[1/2] Testowanie połączenia z Qdrant...", end=" ")
    try:
        client = QdrantClient(host="localhost", port=6333, timeout=3.0)
        collections = client.get_collections()
        print(f"OK (Połączono, liczba kolekcji: {len(collections.collections)})")
        return True
    except Exception as e:
        print(f"BŁĄD: {e}")
        return False

def test_postgres():
    print("[2/2] Testowanie połączenia z PostgreSQL...", end=" ")
    try:
        conn_str = "postgresql://postgres:postgrespassword@localhost:5432/master_eval"
        with psycopg.connect(conn_str) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'evaluation_runs'
                    );
                """)
                table_exists = cur.fetchone()[0]
                if table_exists:
                    print("OK (Połączono, tabela 'evaluation_runs' jest gotowa)")
                    return True
                else:
                    print("UWAGA: Połączono z bazą, ale brak tabeli 'evaluation_runs'")
                    return False
    except Exception as e:
        print(f"BŁĄD: {e}")
        return False

if __name__ == "__main__":
    print("=== Test łączności ze środowiskiem (Faza 2) ===")
    qdrant_ok = test_qdrant()
    postgres_ok = test_postgres()
    
    if qdrant_ok and postgres_ok:
        print("\nObie bazy działają i odpowiadają poprawnie.")
        sys.exit(0)
    else:
        print("\nWystąpił problem z połączeniem.")
        sys.exit(1)
