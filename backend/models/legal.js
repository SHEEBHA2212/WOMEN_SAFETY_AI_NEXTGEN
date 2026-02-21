const mongoose = require("mongoose");

const legalSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  phone: {
    type: String,
    required: true
  },
  issue: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true,
    trim: true
  }
}, {
  timestamps: true
});

module.exports = mongoose.model("Legal", legalSchema);