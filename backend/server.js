const express = require("express");

const app = express();
const PORT = 5000;

console.log("1. Starting backend...");

app.get("/", (req, res) => {
  console.log("2. Browser requested /");
  res.send("Weather backend is running!");
});

app.listen(PORT, () => {
  console.log("3. Server is running on port 5000");
});