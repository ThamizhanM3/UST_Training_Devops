import axios from "axios";

const baseURL =
  (import.meta && import.meta.env && import.meta.env.VITE_API_BASE_URL) ||
  (typeof process !== "undefined" && process.env && process.env.REACT_APP_API_BASE_URL) ||
  "";

const timeout =
  Number(
    (import.meta && import.meta.env && import.meta.env.VITE_API_TIMEOUT) ||
      (typeof process !== "undefined" && process.env && process.env.REACT_APP_API_TIMEOUT) ||
      10000
  );

if (!baseURL) {
  // You can throw or render a fallback UI elsewhere
  // throw new Error("API base URL is not configured");
  console.warn("API base URL is not configured");
}

export const api = axios.create({
  baseURL,
  timeout,
  // withCredentials: true, // uncomment if your API uses cookies across domains
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

// Request interceptor: attach token if present
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token");
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor: centralize error handling / token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    // Example: if (error.response?.status === 401) { ... }
    return Promise.reject(error);
  }
);
