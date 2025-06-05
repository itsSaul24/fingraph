# Create backend/test_neo4j.py
import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv(".env.local")

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))


def test_connection():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connection successful!")

        # Test query
        with driver.session() as session:
            result = session.run("RETURN 'Hello, Neo4j!' as message")
            for record in result:
                print(record["message"])


if __name__ == "__main__":
    test_connection()
