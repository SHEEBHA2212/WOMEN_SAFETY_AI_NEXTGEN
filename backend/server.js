require("dotenv").config();
const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const Legal = require("./models/legal"); 

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB Connected Successfully"))
  .catch(err => console.error("MongoDB Connection Error:", err));

// POST Route - Save Legal Request
app.post("/api/legal-help", async (req, res) => {
  try {
    console.log("Received Data:", req.body);

    const newLegalRequest = new Legal(req.body);
    const savedData = await newLegalRequest.save();

    console.log("Saved to MongoDB:", savedData);

    res.status(200).json({
      message: "Legal request saved successfully!"
    });

  } catch (error) {
    console.error("Error saving legal request:", error);
    res.status(500).json({
      error: "Failed to save legal request"
    });
  }
});

// Start Server
app.listen(5000, () => {
  console.log("Server running on port 5000");
});