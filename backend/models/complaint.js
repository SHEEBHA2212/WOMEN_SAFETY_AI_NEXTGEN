const mongoose = require("mongoose");

const complaintSchema = new mongoose.Schema({
  name: String,
  phone: String,
  issue: String,
  description: String,
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model("Complaint", complaintSchema);