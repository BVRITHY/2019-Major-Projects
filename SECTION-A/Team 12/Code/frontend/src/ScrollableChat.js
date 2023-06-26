import {React, useState} from 'react'
import { Avatar } from "@chakra-ui/avatar";
import { Tooltip } from "@chakra-ui/tooltip";
import ScrollableFeed from "react-scrollable-feed";
import {
  isLastMessage,
  isSameSender,
  isSameSenderMargin,
  isSameUser,
} from "../config/ChatLogics";
import { Box, styled, Typography } from '@mui/material';
import { GetApp as GetAppIcon } from '@mui/icons-material';

import { useToast } from "@chakra-ui/toast";
import axios from "axios";

import { ChatState } from "../Context/ChatProvider";
import { Menu, MenuButton, MenuList, MenuItem, MenuDivider } from "@chakra-ui/react";

import { Button } from "@chakra-ui/button";

import { BellIcon, ChevronDownIcon } from "@chakra-ui/icons";
import "./styles.css"
const Time = styled(Typography)`
    font-size: 10px;
    color: #919191;
    margin-top: 6px;
    word-break: keep-all;
    margin-top: auto;
`;

const ScrollableChat = ({ messages }) => {
  const {
    selectedChat,
    setSelectedChat,
    user,
    notification,
    setNotification,
    chats,
    setChats,
  } = ChatState();

  const toast = useToast();
  const [showPopup, setShowPopup] = useState(false);
  const [newContent, setNewContent] = useState('');
  const [updateMessageContent, setUpdateMessageContent] = useState('');

  const handleUpdateClick = (m) => {
    setShowPopup(true);
    setUpdateMessageContent(m._id)
  };

  const handlePopupClose = () => {
    setShowPopup(false);
    setNewContent('');
  };

  const handleInputChange = (event) => {
    setNewContent(event.target.value);
  };

  const [selectedMessage, setSelectedMessage] = useState("");
  const [loadingChat, setLoadingChat] = useState(false);

  // console.log(isLastMessage,
  //   isSameSender,
  //   isSameSenderMargin,
  //   isSameUser,)


  // const { user, setSelectedChat, selectedChat, chats } = ChatState();
  // console.log(messages)
  // console.log(notification)
  // console.log(selectedChat)

  // console.log(user)
  console.log(chats)

  const handleReplyPricvately = (message) => {
    console.log(message)
  }
  const handleReplyPrivately = (messageId) => {
    // Your logic to handle replying privately to a message goes here
    console.log(`Replying privately to message ${messageId}`);
  };

  const handleDeleteMessage = async (message) => {

    try {
      const config = {
        headers: {
          Authorization: `Bearer ${user.token}`,
        },
      };


      const { data } = await axios.delete(
        `/api/message/${message._id}`,
        config
      );
      toast({
        title: "Message Deleted!",
        description: "Message was deleted successfully!",
        status: "success",
        duration: 5000,
        isClosable: true,
        position: "bottom",
      });
      window.location.reload()
    } catch (error) {
      toast({
        title: "Error Occured!",
        description: "Failed to delete the Messages",
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom",
      });
    }
  };


  const handleUpdateSubmit = async (message) => {
    try {
      const config = {
        headers: {
          Authorization: `Bearer ${user.token}`,
        },
      };


      const { data } = await axios.put(
        `/api/message/${message._id}`,
        config,
      );
      // toast({
      //   title: "Message updated!",
      //   description: "Message was updated successfully!",
      //   status: "success",
      //   duration: 5000,
      //   isClosable: true,
      //   position: "bottom",
      // });
      // window.location.reload()
    } catch (error) {
      toast({
        title: "Error Occured!",
        description: "Failed to update the Messages",
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom",
      });
    }
  };

  const accessChat = async (userId) => {
    console.log(userId);

    try {
      setLoadingChat(true);
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${user.token}`,
        },
      };
      const { data } = await axios.post(`/api/chat`, { userId }, config);

      if (!chats.find((c) => c._id === data._id)) setChats([data, ...chats]);
      setSelectedChat(data);
      setLoadingChat(false);
      // onClose();
    } catch (error) {
      toast({
        title: "Error fetching the chat",
        description: error.message,
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom-left",
      });
    }
  };

  return (
    <>
    {/* <ScrollableFeed>
    {messages &&
      messages.map((m, i) => (
        <div style={{ display: "flex" }} key={m._id}>
          {(isSameSender(messages, m, i, user._id) ||
            isLastMessage(messages, i, user._id)) && (
            <Tooltip label={m.sender.name} placement="bottom-start" hasArrow>
              <Avatar
                mt="7px"
                mr={1}
                size="sm"
                cursor="pointer"
                name={m.sender.name}
                src={m.sender.pic}
              />
            </Tooltip>
          )}
          <span
            style={{
              backgroundColor: `${
                m.sender._id === user._id ? "#BEE3F8" : "#B9F5D0"
              }`,
              marginLeft: isSameSenderMargin(messages, m, i, user._id),
              marginTop: isSameUser(messages, m, i, user._id) ? 3 : 10,
              borderRadius: "20px",
              padding: "5px 15px",
              maxWidth: "75%",
              position: "relative", // To make the dropdown menu position relative to this element
            }}
          >
            {m.content}
            <Menu>
              <MenuButton
                as="span"
                ml={2}
                position="absolute"
                top="50%"
                right={0}
                transform="translateY(-50%)"
              >
                Reply Privately
              </MenuButton>
              <MenuList>
                <MenuItem
                  onClick={() => handleReplyPrivately(m._id)}
                  disabled={selectedMessageId !== "" && selectedMessageId !== m._id}
                >
                  {selectedMessageId === m._id ? "Selected" : "Reply privately"}
                </MenuItem>
              </MenuList>
            </Menu>
          </span>
        </div>
      ))}
  </ScrollableFeed> */}
    <ScrollableFeed>
    {showPopup && (
      
       <div className="popup">
       <input type="text" value={newContent} onChange={handleInputChange} />
       <button className="update" onClick={handleUpdateSubmit(updateMessageContent)}>Update</button>
       <button className="cancel" onClick={handlePopupClose}>Cancel</button>
     </div>
      )}
      {messages &&
        messages.map((m, i) => (
          <div style={{ display: "flex" }} key={m._id}>
            {(isSameSender(messages, m, i, user._id) ||
              isLastMessage(messages, i, user._id)) && (
              <Tooltip label={m.sender.name} placement="bottom-start" hasArrow>
                <Avatar
                  mt="7px"
                  mr={1}
                  size="sm"
                  cursor="pointer"
                  name={m.sender.name}
                  src={m.sender.pic}
                />
              </Tooltip>
            )}
            <span
              style={{
                backgroundColor: `${
                  m.sender._id === user._id ? "#BEE3F8" : "#B9F5D0"
                }`,
                marginLeft: isSameSenderMargin(messages, m, i, user._id),
                marginTop: isSameUser(messages, m, i, user._id) ? 3 : 10,
                borderRadius: "20px",
                padding: "5px 15px",
                maxWidth: "75%",
              }}
            >
              {
                  m.type === 'file' ? <ImageMessage message={m} /> : m.content
              }
              {/* {m.content} */}
              {m.chat.isGroupChat === true && isSameSender(messages, m, i, user._id) &&  (
                  <Menu>
                    <MenuButton
                      as={Button}
                      bg="none"
                      rightIcon={<ChevronDownIcon />}
                      size="xs"
                      ml={1}
                    >
                    </MenuButton>
                    <MenuList>
                      <MenuItem
                        fontSize="xs"
                        fontWeight="semibold"
                        color="gray.600"
                        _hover={{ bg: "gray.100" }}
                        onClick={() => accessChat(m.sender._id)}
                      >
                        Reply Privately
                      </MenuItem>
                      {/* <MenuItem
                        fontSize="xs"
                        fontWeight="semibold"
                        color="gray.600"
                        _hover={{ bg: "gray.100" }}
                        // onClick={() => handleReplyPricvately(m.chat)}
                      >
                        React
                      </MenuItem> */}
                    </MenuList>
                  </Menu>
                )}
                 {isSameUser(messages, m, i, user.    _id) &&
                  (
                  <Menu>
                    <MenuButton
                      as={Button}
                      bg="none"
                      rightIcon={<ChevronDownIcon />}
                      size="xs"
                      ml={1}
                    >
                    </MenuButton>
                    <MenuList>
                      {/* <MenuItem
                        fontSize="xs"
                        fontWeight="semibold"
                        color="gray.600"
                        _hover={{ bg: "gray.100" }}
                        // onClick={() => handleReplyPricvately(m.chat)}
                      >
                        React
                      </MenuItem>
                      <MenuItem
                        fontSize="xs"
                        fontWeight="semibold"
                        color="gray.600"
                        _hover={{ bg: "gray.100" }}
                        onClick={() => handleUpdateClick(m)}
                      >
                        Update
                      </MenuItem> */}
                      <MenuItem
                        fontSize="xs"
                        fontWeight="semibold"
                        color="gray.600"
                        _hover={{ bg: "gray.100" }}
                        onClick={() => handleDeleteMessage(m)}
                      >
                        Delete
                      </MenuItem>
                    </MenuList>
                  </Menu>
                )}
            </span>
          </div>
        ))}
    </ScrollableFeed>
    </>
  );
};

const ImageMessage = ({ message }) => {
  const iconPDF = 'https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/27_Pdf_File_Type_Adobe_logo_logos-512.png';

  const downloadMedia = async (e, originalImage) => {
    e.preventDefault();
    console.log(originalImage)
    try {
        fetch(originalImage)
        .then(resp => resp.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;

            const nameSplit = originalImage.split("/");
            const duplicateName = nameSplit.pop();

            // the filename you want
            a.download = "" + duplicateName + "";
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch((error) => console.log('Error while downloading the image ', error))

    } catch (error) {
        console.log('Error while downloading the image ', error);
    }
}
  return (
      <div style={{ position: 'relative' }}>
          {
              message?.text?.includes('.pdf') ?
                  <div style={{ display: 'flex' }}>
                      <img src={iconPDF} alt="pdf-icon" style={{ width: 80 }} />
                      {/* <Typography style={{ fontSize: 14 }} >{message.text.split("/").pop()}</Typography> */}
                  </div>
              : 
                  <img style={{ width: 300, height: '100%', objectFit: 'cover' }} src={message.text} alt={message.text} />
          }
           <GetAppIcon 
                  onClick={(e) => downloadMedia(e, message.text)} 
                  fontSize='small' 
                  style={{ marginRight: 10, border: '1px solid grey', borderRadius: '50%' }} 
              />
          {/* <Time style={{ position: 'absolute', bottom: 0, right: 0 }}>
              <GetAppIcon 
                  onClick={(e) => downloadMedia(e, message.text)} 
                  fontSize='small' 
                  style={{ marginRight: 10, border: '1px solid grey', borderRadius: '50%' }} 
              />
              {formatDate(message.createdAt)}
          </Time> */}
      </div>
  )
}

export default ScrollableChat;
