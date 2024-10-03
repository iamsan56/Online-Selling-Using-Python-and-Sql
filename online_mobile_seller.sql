-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: online_mobile_seller
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accessories`
--

DROP TABLE IF EXISTS `accessories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accessories` (
  `serialno` int NOT NULL AUTO_INCREMENT,
  `ProductName` varchar(100) DEFAULT NULL,
  `Brand` varchar(50) DEFAULT NULL,
  `ModelNo` varchar(50) DEFAULT NULL,
  `ProductId` int DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  PRIMARY KEY (`serialno`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessories`
--

LOCK TABLES `accessories` WRITE;
/*!40000 ALTER TABLE `accessories` DISABLE KEYS */;
INSERT INTO `accessories` VALUES (1,'Phone Case','Army','Tough Armor',23,2500),(2,'Bluetooth Speaker','Boat','MEGABOOM 3',129,1800),(3,'Apple Pro Vision','Apple','Foreign Product',142,290000),(4,'AirPods','Apple','Foreign Product',143,45000),(5,'Screen Protector','GorrilaTemper','Glass Screen Protector',145,1500),(6,'Gaming Mouse','Asus','M65 RGB Elite',147,6000),(7,'USB-C Cable','SamSung','PowerLine+',156,1000),(8,'Wireless Earphones','Boat','Elite 75t',166,1500),(9,'Car Phone Mount','Audi','Easy One Touch 5',168,2000),(10,'Wireless Charging Pad','Nothing','Boost Charge',212,4000),(11,'Mechanical Keyboard','Asus','Apex Pro',213,20000),(12,'Fitness Tracker','MicroMax','Charge 4',214,13000),(13,'Camera Bag','Canva','ProTactic BP 350 AW II',220,1200),(14,'Smart Home Hub','Google','Nest Hub',231,8000),(15,'Power Bank','SamSung','JP-101',314,2500),(16,'USB C','SAMSUNG','T-150',56,550),(17,'case','oppo','78',88,7800);
/*!40000 ALTER TABLE `accessories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'san',56),(2,'mj',123),(3,'sus',36);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `item_name` varchar(255) DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `date` date DEFAULT '2023-01-01',
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'SANJEEV','+917397458145','Card - Debit','A15',2,49000,'2023-01-01'),(4,'rj','+917397458145','Cash','F15',2,49000,'2023-01-01'),(5,'rj','+911111111111','Cash','F15',1,49500,'2023-01-01'),(6,'SANJEEV','+917397458145','Cash','TrackPad',10,891,'2023-01-01'),(7,'tj','+917397450987','Card - Debit','A31',2,49000,'2023-01-01'),(13,'ij','+917899877899','UPI','Phone Case',3,2425,'2023-01-01'),(17,'yu','+916789987667','Cash','Phone Case',0,2500,'2023-01-01'),(18,'CNC','+918056206789','Card - Debit','Apple Pro Vision',3,281300,'2023-01-01'),(19,'ij','+911234567890','Card - Debit','USB C',2,539,'2023-01-01'),(20,'hygbhyhyh','+911234567890','Card - Debit','13 pro',2,245000,'2023-01-01'),(21,'ufugefgue','+911234567890','Cash','Screen Protector',1,1485,'2023-01-01'),(22,'kjdkjkdgh','+911234567890','Card - Credit','F15',2,49000,'2023-01-01'),(23,'varun','+916383972050','Cash','V27 pro',1,74250,'2023-01-01'),(24,'SUSI','+917092205775','UPI','A31',4,48000,'2023-01-01'),(30,'poi','+911234567890','Cash','Smart Home Hub',1,7920,'2023-11-17'),(31,'oiu','+911234567890','Cash','Camera Bag',4,1152,'2023-11-17'),(32,'ikj','+917890654321','Cash','Smart Home Hub',1,7920,'2023-11-17'),(33,'poiuyttr','+910987654321','UPI','Bluetooth Speaker',3,1746,'2023-11-17'),(34,'opi','+911234567890','Cash','case',4,7488,'2023-11-17'),(35,'poi','+911234567890','Cash','11R',1,74250,'2023-11-17'),(36,'poi','+911234567890','Card - Debit','Power Bank',6,2350,'2023-11-17'),(37,'poi','+911234567890','Cash','Power Bank',5,2375,'2023-11-17'),(38,'poi','+911234567890','Cash','case',13,6786,'2023-11-17'),(39,'poi','+911234567890','Cash','Power Bank',9,2275,'2023-11-17'),(40,'poi','+911234567890','Cash','Mechanical Keyboard',8,18400,'2023-11-17'),(41,'poi','+911234567890','Cash','Power Bank',0,2500,'2023-11-17'),(42,'poi','+911234567890','UPI','Fitness Tracker',9,11830,'2023-11-17'),(43,'SUSINDHARAN CNC','+918056288080','UPI','A15',6,47000,'2023-11-17'),(44,'io','+919967812345','UPI','Fitness Tracker',6,12220,'2023-11-17'),(45,'oiu','+911234567890','UPI','Fitness Tracker',1,12870,'2023-11-17'),(46,'oiu','+911234567890','UPI','y93',4,72000,'2023-11-17'),(47,'oiu','+911234567890','UPI','Phone Case',3,2425,'2023-11-17'),(48,'SANJEEV','+919940621037','UPI','ROG 7 ++',3,111550,'2023-11-17'),(49,'SUSINDHAREN CNCCC','+918056288080','UPI','ROG 7 ++',1,118800,'2023-11-17');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smartphones`
--

DROP TABLE IF EXISTS `smartphones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `smartphones` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `ram` int DEFAULT NULL,
  `camera` int DEFAULT NULL,
  `storage` int DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `os` varchar(255) DEFAULT NULL,
  `price` int DEFAULT '75000',
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smartphones`
--

LOCK TABLES `smartphones` WRITE;
/*!40000 ALTER TABLE `smartphones` DISABLE KEYS */;
INSERT INTO `smartphones` VALUES (1,'F15','oppo',64,32,128,'blue','colorOS 13',50000),(2,'T2','vivo',128,32,256,'black','android 12',75000),(3,'IPHONE 14 PRO MAX','apple',128,32,256,'yellow','iOS',250000),(4,'NOTE 12','one plus',32,16,32,'grey','android 12',75000),(5,'iPHONE 14','apple',64,32,256,'orange','iOS',250000),(6,'NOTE 12','redmi',64,32,256,'green','android 12',75000),(7,'V27 pro','vivo',64,32,128,'half white','android 12',75000),(8,'13 pro','apple',64,32,256,'red','iOS',250000),(9,'13 pro max','apple',64,32,256,'grey','iOS',250000),(10,'13','apple',64,32,256,'green','iOS',250000),(11,'nord CE 3','one plus',64,16,128,'gold','android 11',75000),(12,'A31','oppo',64,16,128,'silver','colorOS 13',50000),(13,'NOTE 12 PRO','redmi',32,8,64,'silver','android 12',75000),(14,'y73','mi',32,8,64,'silver','android',75000),(15,'y93','mi',32,16,64,'brown','android',75000),(16,'galaxy Z','samsung',32,16,64,'orange','android',100000),(17,'14 pro max','apple',128,64,256,'orange','iOS',250000),(18,'G11','nokia',128,64,256,'white','android',75000),(19,'2.1','nokia',128,64,256,'violet','android',75000),(20,'11R','one plus',64,32,128,'violet','android 11',75000),(21,'NORD CE2','one plus',64,16,128,'blue black','android 11',75000),(22,'nord CE3','one plus',32,16,64,'blue black','android 11',75000),(23,'12 pro','apple',32,16,64,'red blue','iOS',250000),(24,'12 pro max','apple',32,16,128,'half white','iOS',250000),(25,'11i','xiaomi',64,32,128,'half white','android',75000),(26,'galaxy A71','samsung',64,32,128,'black','android',100000),(27,'V27','vivo',64,32,128,'black','android 12',75000),(28,'A15','oppo',128,64,256,'blue','colorOS 13',50000),(30,'ROG 7 ++','Asus',16,24,256,'White','Android 14',120000);
/*!40000 ALTER TABLE `smartphones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-17 23:55:07
