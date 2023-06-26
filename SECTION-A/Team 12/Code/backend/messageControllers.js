const asyncHandler = require("express-async-handler");
const Message = require("../models/messageModel");
const User = require("../models/userModel");
const Chat = require("../models/chatModel");

//@description     Get all Messages
//@route           GET /api/Message/:chatId
//@access          Protected
const allMessages = asyncHandler(async(req, res) => {
    console.log(req.body, req.params.chatId)
    try {
        const messages = await Message.find({ chat: req.params.chatId })
            .populate("sender", "name pic email")
            .populate("chat");
        console.log(messages)
        res.json(messages);
    } catch (error) {
        res.status(400);
        throw new Error(error.message);
    }
});

//@description     Create New Message
//@route           POST /api/Message/
//@access          Protected
const sendMessage = asyncHandler(async(req, res) => {
    // console.log(req.body)
    const { content, chatId, text, type } = req.body;

    if (!content || !chatId) {
        console.log("Invalid data passed into request");
        return res.sendStatus(400);
    }

    var newMessage = {
        sender: req.user._id,
        content: content,
        chat: chatId,
        type: type,
        text: text
    };

    try {
        var message = await Message.create(newMessage);

        message = await message.populate("sender", "name pic").execPopulate();
        message = await message.populate("chat").execPopulate();
        message = await User.populate(message, {
            path: "chat.users",
            select: "name pic email",
        });

        await Chat.findByIdAndUpdate(req.body.chatId, { latestMessage: message });

        res.json(message);
    } catch (error) {
        res.status(400);
        throw new Error(error.message);
    }
});

const deleteMessage = asyncHandler(async(req, res) => {
    try {
        const deletedMessage = await Message.findByIdAndDelete(req.params.messageId);
        if (!deletedMessage) {
            return res.status(404).json({ message: 'Message not found' });
        }
        return res.status(204).send();
    } catch (err) {
        console.error(err);
        return res.status(500).json({ message: 'Internal server error' });
    }

});

const updateMessage = asyncHandler(async(req, res) => {
    console.log(req.body.content)
    try {
        const { content } = req.body;
        const updatedMessage = await Message.findByIdAndUpdate(
            req.params.messageId, { content }, { new: true }
        );
        if (!updatedMessage) {
            return res.status(404).json({ message: 'Message not found' });
        }
        return res.status(200).json(updatedMessage);
    } catch (err) {
        console.error(err);
        return res.status(500).json({ message: 'Internal server error' });
    }

});


module.exports = { allMessages, sendMessage, deleteMessage, updateMessage };