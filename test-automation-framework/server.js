const express = require("express");
const app = express();

// Define a simple API endpoint
app.get("/", (req, res) => {
    res.send("🚀 Server is running!");
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`✅ Server started on http://localhost:${PORT}`);
});
