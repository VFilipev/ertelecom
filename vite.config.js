import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
const HOST = "http://127.0.0.1:8000/";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 8080,
    host: "127.0.0.1",
    proxy: {
      "^/api": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
      "^/media": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
      "^/api-token-auth": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
    },
  },
  plugins: [vue()],
});
