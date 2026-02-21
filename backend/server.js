require("dotenv").config();
const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const Complaint = require("./models/complaint"); // make sure filename matches

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB Connected Successfully"))
  .catch(err => console.log(err));

// POST Route - Save Complaint
app.post("/api/legal-help", async (req, res) => {
  try {
    console.log("Received Data:", req.body);

    const newComplaint = new Complaint(req.body);
    await newComplaint.save();

    console.log("Saved to MongoDB:", newComplaint);

    res.status(200).json({
      message: "Complaint saved successfully!"
    });

  } catch (error) {
    console.error("Error saving complaint:", error);
    res.status(500).json({
      error: "Failed to save complaint"
    });
  }
});

// Start Server
app.listen(5000, () => {
  console.log("Server running on port 5000");
});