const mongoose = require("mongoose");

const messageSchema = mongoose.Schema({
    sender: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
    content: { type: String, trim: true },
    chat: { type: mongoose.Schema.Types.ObjectId, ref: "Chat" },
    readBy: [{ type: mongoose.Schema.Types.ObjectId, ref: "User" }],
    type: {
        type: String
    },
    text: {
        type: String
    },
}, { timestamps: true });

const Message = mongoose.model("Message", messageSchema);
module.exports = Message;