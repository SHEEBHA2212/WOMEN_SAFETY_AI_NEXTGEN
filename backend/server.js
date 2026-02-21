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
  .catch((err) => console.error("MongoDB Connection Error:", err));

// ===============================
// POST - Create Legal Request
// ===============================
app.post("/api/legal-help", async (req, res) => {
  try {
    const { name, phone, issue, description } = req.body;

    // Basic Validation
    if (!name || !phone || !issue || !description) {
      return res.status(400).json({
        error: "All fields are required",
      });
    }

    const newLegalRequest = new Legal({
      name,
      phone,
      issue,
      description,
    });

    const savedData = await newLegalRequest.save();

    res.status(201).json({
      message: "Legal request saved successfully!",
      data: savedData,
    });

  } catch (error) {
    console.error("Error saving legal request:", error);
    res.status(500).json({
      error: "Internal server error",
    });
  }
});

// ===============================
// GET - Fetch All Legal Requests
// ===============================
app.get("/api/legal-help", async (req, res) => {
  try {
    const allRequests = await Legal.find().sort({ createdAt: -1 });

    res.status(200).json(allRequests);

  } catch (error) {
    console.error("Error fetching legal requests:", error);
    res.status(500).json({
      error: "Failed to fetch legal requests",
    });
  }
});

// Start Server
const PORT = 5000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});