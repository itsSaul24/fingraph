import { useEffect, useState } from "react";
import "./App.css";

interface HealthStatus {
  status: string;
  version: string;
}

function App() {
  const [health, setHealth] = useState<HealthStatus | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch("http://localhost:8000/health");
        const data = await response.json();
        setHealth(data);
      } catch (error) {
        console.error("Failed to fetch health status:", error);
      } finally {
        setLoading(false);
      }
    };

    checkHealth();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>FinGraph</h1>
        <p>Financial Entity Intelligence Platform</p>

        {loading ? (
          <p>Connecting to backend...</p>
        ) : health ? (
          <div>
            <p>Backend Status: {health.status}</p>
            <p>Version: {health.version}</p>
          </div>
        ) : (
          <p>Backend connection failed</p>
        )}
      </header>
    </div>
  );
}

export default App;
