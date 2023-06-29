/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - trust_based
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`trust_based` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `trust_based`;

/*Table structure for table `cloud` */

DROP TABLE IF EXISTS `cloud`;

CREATE TABLE `cloud` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `cloud` */

insert  into `cloud`(`username`,`password`) values ('cloud','cloud'),('cs1','cs1'),('cs2','cs2'),('cs3','cs3');

/*Table structure for table `manager` */

DROP TABLE IF EXISTS `manager`;

CREATE TABLE `manager` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `manager` */

insert  into `manager`(`username`,`password`) values ('manager','manager');

/*Table structure for table `owner` */

DROP TABLE IF EXISTS `owner`;

CREATE TABLE `owner` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `cloud` varchar(100) NOT NULL,
  `attributes` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `otp` int(11) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`username`,`cloud`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`username`,`password`,`email`,`gender`,`address`,`mobile`,`cloud`,`attributes`,`skey`,`status`,`otp`,`image`) values ('shiva','shiva','shiva.1000projects@gmail.com','MALE','Hyderabad','9032101992','IDM','developers','NkPg/0hhAM20HDdR4JakuA==','Blocked',27008,'shiva.jpg');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cipher` longtext,
  `data` longtext,
  `skey` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`filename`,`email`,`cipher`,`data`,`skey`,`owner`,`status`) values (4,'test.txt','shivakrish573@gmail.com','oxIUPMa3PoF/HEX3Wme1jf9h4wU/MAYxLdwyz23gsDqirZzQr baXLCVXr4kNX3gPyV7wotpuHW5OTc9gf9N2P3MoTjttt/AsZqxKwztBSyDiyK 4NLXr0As8Xj1CyHbvb2pgTYjP1uIWivreH2/mt4UbhnXsZe4gyyKkJEvnQBb7ZG9Ni7dUh1dKBhu1mgTYxGTJ4zg8BcUQpJy TABzKHouveQmCSrsqw7s0oQaR2PlDr3Zrl/iq9xDezqguBwOOdPKvBN zUWsWPkJMLRoT0w62xv9f6prC4Hu2cmDwX4YSTzisoK0pjEWIa IK77unQQ m7DC3Xnw0J6zVRNpTVvraSnWJ2Ipwh85SId1SpN4yim8D9d4c7S0qJUCCCY7WYseVfNqGvtM1OWkre7xUYdWoiJJDD/gFsY9akKy2l2AxmeZmRNy/tpAzyY6drYlspN7lv25bhB7HL/hvjGhe7zKTsOhx 5fdkBSAQsxYYqycspwiUM ODBLf4pPZcVUgy3LWyTR2O5r9NbP6nSbGD7NX1DbUQH4Is08MWNhpPNOAo8CdOSS6PiCxmZkIw/U9zIXmONx9kCF51Se6aSZL1XoZoLifOIZbek8Axpnf8oye YRIy17Q6UR8fG9mhmoxD4bHl18rbf iaEQm8N4MagVt7YYo3iEqaTSLGZwYL67ChjoUEBeqmuadi41RA2X0D4oiJzNsSpKNjFgivPDYM2ibXjMbUtB 6Kwo3dVSL 3kztM00djptnEPypmfKH8z4tJyNIeRSQKxIGcmNYBfCk9CTug3RFDwalBK/5cq/3G9GUZbuv1yT5A/0KPfE5CDNTMgTjplnjPe69xlOh7pU2r5agtxBULerc7fULN1ZmuT6hSOS/X6Kiptl9LIaPMUa2cljYiKsmHdUpykZxq0EVASftapZMHXeHF8jFCThrNjiN uPuRTgl8Be9uleyvbAchx5PTARfdep5IaC Mo8jQbHBIXEVBHt5P5rmCciczX e2rTR8Zfo/X6H/5D7vJM1m4oWSEqzVJ iBK0UZcHBiV CV1yB63m8cuCskaAa9mZGy4JCquGwHUBfoE22o8EQXCyhXMv6Po3FOReuNZPas64/qSDR7lwNpED 3Bk=','mobile source (  register , login , upload data, send data to edge server from edge server to cloud server show time for data process from source to edge server to cloud server , select mobile destination and send data along with key ,first time cloud will give permission to send data to mobile destination )send same data again to mobile destination this time edge server will send data to mobile desitnation cloud serveredge server  ( catching data, calculate time and energy used edoo oka value evu for energy only edge server loo vuntey oka value , cloud nundi veltey oka value ,  same data mobile desitination ke pamputhey for that day edge server will only give for new data cloud server will give permission )mobile destination ( register , login, view files , download directly with key received no need to request for key ','y11SZobKbLjBfXNbKv7WNg==','shiva.1000projects@gmail.com','sent');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `file` longtext,
  `filename` varchar(100) NOT NULL,
  `CDate` timestamp NULL DEFAULT NULL,
  `cipher` longtext,
  `email` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `cloud` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`filename`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`file`,`filename`,`CDate`,`cipher`,`email`,`skey`,`cloud`) values ('mobile source (  register , login , upload data, send data to edge server from edge server to cloud server show time for data process from \r\nsource to edge server to cloud server , select mobile destination and send data along with key ,first time cloud will give permission to send data to mobile destination \r\n)\r\nsend same data again to mobile destination this time edge server will send data to mobile desitnation \r\n\r\n\r\ncloud server\r\n\r\nedge server  ( catching data, calculate time and energy used edoo oka value evu for energy only edge server loo vuntey oka value , cloud nundi veltey oka value ,\r\n  same data mobile desitination ke pamputhey for that day edge server will only give for new data cloud server will give permission )\r\n\r\n\r\nmobile destination ( register , login, view files , download directly with key received no need to request for key ','test.txt','2023-03-13 00:00:00','oxIUPMa3PoF/HEX3Wme1jf9h4wU/MAYxLdwyz23gsDqirZzQr+baXLCVXr4kNX3gPyV7wotpuHW5\r\nOTc9gf9N2P3MoTjttt/AsZqxKwztBSyDiyK+4NLXr0As8Xj1CyHbvb2pgTYjP1uIWivreH2/mt4U\r\nbhnXsZe4gyyKkJEvnQBb7ZG9Ni7dUh1dKBhu1mgTYxGTJ4zg8BcUQpJy+TABzKHouveQmCSrsqw7\r\ns0oQaR2PlDr3Zrl/iq9xDezqguBwOOdPKvBN+zUWsWPkJMLRoT0w62xv9f6prC4Hu2cmDwX4YSTz\r\nisoK0pjEWIa+IK77unQQ+m7DC3Xnw0J6zVRNpTVvraSnWJ2Ipwh85SId1SpN4yim8D9d4c7S0qJU\r\nCCCY7WYseVfNqGvtM1OWkre7xUYdWoiJJDD/gFsY9akKy2l2AxmeZmRNy/tpAzyY6drYlspN7lv2\r\n5bhB7HL/hvjGhe7zKTsOhx+5fdkBSAQsxYYqycspwiUM+ODBLf4pPZcVUgy3LWyTR2O5r9NbP6nS\r\nbGD7NX1DbUQH4Is08MWNhpPNOAo8CdOSS6PiCxmZkIw/U9zIXmONx9kCF51Se6aSZL1XoZoLifOI\r\nZbek8Axpnf8oye+YRIy17Q6UR8fG9mhmoxD4bHl18rbf+iaEQm8N4MagVt7YYo3iEqaTSLGZwYL6\r\n7ChjoUEBeqmuadi41RA2X0D4oiJzNsSpKNjFgivPDYM2ibXjMbUtB+6Kwo3dVSL+3kztM00djptn\r\nEPypmfKH8z4tJyNIeRSQKxIGcmNYBfCk9CTug3RFDwalBK/5cq/3G9GUZbuv1yT5A/0KPfE5CDNT\r\nMgTjplnjPe69xlOh7pU2r5agtxBULerc7fULN1ZmuT6hSOS/X6Kiptl9LIaPMUa2cljYiKsmHdUp\r\nykZxq0EVASftapZMHXeHF8jFCThrNjiN+uPuRTgl8Be9uleyvbAchx5PTARfdep5IaC+Mo8jQbHB\r\nIXEVBHt5P5rmCciczX+e2rTR8Zfo/X6H/5D7vJM1m4oWSEqzVJ+iBK0UZcHBiV+CV1yB63m8cuCs\r\nkaAa9mZGy4JCquGwHUBfoE22o8EQXCyhXMv6Po3FOReuNZPas64/qSDR7lwNpED+3Bk=','shiva.1000projects@gmail.com','y11SZobKbLjBfXNbKv7WNg==','');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `address` text,
  `mobile` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`username`,`password`,`email`,`gender`,`address`,`mobile`,`status`) values ('sk','123','shivakrish573@gmail.com','MALE','hyd','9099990909','Blocked');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
