// src/lib/axios.js
import axios from "axios";

const baseURL =
  (typeof window !== "undefined" && window.__ENV__ && window.__ENV__.API_BASE_URL) ||
  import.meta.env?.VITE_API_BASE_URL ||
  process.env?.REACT_APP_API_BASE_URL ||
  "";

const timeout = Number(
  (typeof window !== "undefined" && window.__ENV__ && window.__ENV__.API_TIMEOUT) ||
  import.meta.env?.VITE_API_TIMEOUT ||
  process.env?.REACT_APP_API_TIMEOUT ||
  10000
);

export const api = axios.create({ baseURL, timeout });
