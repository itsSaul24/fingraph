import "@testing-library/jest-dom";
import { render, screen, waitFor } from "@testing-library/react";
import App from "./App";

// Mock fetch for testing
global.fetch = jest.fn();

beforeEach(() => {
  (fetch as jest.Mock).mockClear();
});

test("renders FinGraph title", () => {
  // Mock successful API response
  (fetch as jest.Mock).mockResolvedValueOnce({
    json: async () => ({ status: "healthy", version: "0.1.0" }),
  });

  render(<App />);
  const titleElement = screen.getByText(/FinGraph/i);
  expect(titleElement).toBeInTheDocument();
});

test("renders platform description", () => {
  // Mock successful API response
  (fetch as jest.Mock).mockResolvedValueOnce({
    json: async () => ({ status: "healthy", version: "0.1.0" }),
  });

  render(<App />);
  const descriptionElement = screen.getByText(
    /Financial Entity Intelligence Platform/i,
  );
  expect(descriptionElement).toBeInTheDocument();
});

test("shows loading state initially", () => {
  // Mock delayed API response
  (fetch as jest.Mock).mockImplementationOnce(
    () => new Promise((resolve) => setTimeout(resolve, 100)),
  );

  render(<App />);
  const loadingElement = screen.getByText(/Connecting to backend/i);
  expect(loadingElement).toBeInTheDocument();
});

test("shows backend status when API responds", async () => {
  // Mock successful API response
  (fetch as jest.Mock).mockResolvedValueOnce({
    json: async () => ({ status: "healthy", version: "0.1.0" }),
  });

  render(<App />);

  await waitFor(() => {
    expect(screen.getByText(/Backend Status: healthy/i)).toBeInTheDocument();
  });
});

test("shows error state when API fails", async () => {
  // Mock failed API response
  (fetch as jest.Mock).mockRejectedValueOnce(new Error("Network error"));

  render(<App />);

  await waitFor(() => {
    expect(screen.getByText(/Backend connection failed/i)).toBeInTheDocument();
  });
});

test("displays version information", async () => {
  // Mock successful API response
  (fetch as jest.Mock).mockResolvedValueOnce({
    json: async () => ({ status: "healthy", version: "0.1.0" }),
  });

  render(<App />);

  await waitFor(() => {
    expect(screen.getByText(/Version: 0.1.0/i)).toBeInTheDocument();
  });
});
