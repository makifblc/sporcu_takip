-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: sporcu_takip
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `antrenman_tipleri`
--

DROP TABLE IF EXISTS `antrenman_tipleri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `antrenman_tipleri` (
  `id` int NOT NULL AUTO_INCREMENT,
  `spor_dali` varchar(100) DEFAULT NULL,
  `antrenman_adi` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `antrenman_tipleri`
--

LOCK TABLES `antrenman_tipleri` WRITE;
/*!40000 ALTER TABLE `antrenman_tipleri` DISABLE KEYS */;
INSERT INTO `antrenman_tipleri` VALUES (1,'Futbol','Şut Çalışması'),(2,'Futbol','Pas Çalışması'),(3,'Koşu','Sprint'),(4,'Koşu','Uzun Mesafe'),(5,'Basketbol','Şut Atışı'),(6,'Basketbol','Dribbling');
/*!40000 ALTER TABLE `antrenman_tipleri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `antrenmanlar`
--

DROP TABLE IF EXISTS `antrenmanlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `antrenmanlar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sporcu_id` int DEFAULT NULL,
  `tarih` date DEFAULT NULL,
  `ad` varchar(100) DEFAULT NULL,
  `sure` int DEFAULT NULL,
  `aciklama` text,
  PRIMARY KEY (`id`),
  KEY `sporcu_id` (`sporcu_id`),
  CONSTRAINT `antrenmanlar_ibfk_1` FOREIGN KEY (`sporcu_id`) REFERENCES `sporcular` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `antrenmanlar`
--

LOCK TABLES `antrenmanlar` WRITE;
/*!40000 ALTER TABLE `antrenmanlar` DISABLE KEYS */;
INSERT INTO `antrenmanlar` VALUES (1,1,'2024-05-02','Ağırlık - Göğüs',60,'Bench press ve incline dumbbell'),(2,1,'2024-05-03','Ağırlık - Sırt',55,'Lat pulldown ve barbell row'),(3,1,'2024-05-04','HIIT',30,'20dk yoğun HIIT antrenmanı'),(4,1,'2024-05-05','Yoga',50,'Esneme ve nefes egzersizleri'),(5,1,'2024-05-06','Kardiyo - Bisiklet',40,'Kapalı alanda spinning'),(6,1,'2024-05-07','Ağırlık - Bacak',65,'Squat, leg press, calf raises'),(7,1,'2024-05-08','Ağırlık - Omuz',50,'Shoulder press, lateral raises'),(8,1,'2024-05-09','Fonksiyonel Antrenman',45,'TRX ve vücut ağırlığı ile'),(9,1,'2024-05-10','Yüzme',60,'Serbest stil 1 km yüzme'),(10,1,'2024-05-11','Kardiyo - Merdiven',35,'Merdiven tırmanma egzersizi'),(11,1,'2024-05-12','Ağırlık - Kol',50,'Biceps curl, triceps pushdown'),(12,1,'2024-05-13','Pilates',45,'Core bölgesine odaklı'),(13,1,'2024-05-14','Kickboks',55,'Teknik + kondisyon'),(14,1,'2024-05-15','Stretching',30,'Tüm vücut esnetme'),(15,1,'2024-05-16','Kardiyo - Eliptik',40,'Yağ yakım odaklı'),(16,1,'2024-05-17','Ağırlık - Full Body',70,'Tüm vücut çalışması'),(17,1,'2024-05-18','Zumba',45,'Müzikli grup dersi'),(18,1,'2024-05-19','TRX',35,'Vücut direnciyle denge çalışması'),(19,1,'2024-05-20','Kardiyo - Interval',30,'Koşu bandında interval setleri'),(20,1,'2024-05-01','Kardiyo - Koşu',45,'Sahilde tempolu koşu');
/*!40000 ALTER TABLE `antrenmanlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ilerlemeler`
--

DROP TABLE IF EXISTS `ilerlemeler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ilerlemeler` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sporcu_id` int DEFAULT NULL,
  `tarih` date DEFAULT NULL,
  `kilo` float DEFAULT NULL,
  `tekrar` int DEFAULT NULL,
  `notlar` text,
  PRIMARY KEY (`id`),
  KEY `sporcu_id` (`sporcu_id`),
  CONSTRAINT `ilerlemeler_ibfk_1` FOREIGN KEY (`sporcu_id`) REFERENCES `sporcular` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ilerlemeler`
--

LOCK TABLES `ilerlemeler` WRITE;
/*!40000 ALTER TABLE `ilerlemeler` DISABLE KEYS */;
INSERT INTO `ilerlemeler` VALUES (1,1,'2025-05-15',100,10,'tekrar'),(2,4,'2025-05-14',65,25,'Barbel Curl');
/*!40000 ALTER TABLE `ilerlemeler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kullanicilar`
--

DROP TABLE IF EXISTS `kullanicilar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kullanicilar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kullanici_adi` varchar(50) DEFAULT NULL,
  `sifre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kullanici_adi` (`kullanici_adi`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kullanicilar`
--

LOCK TABLES `kullanicilar` WRITE;
/*!40000 ALTER TABLE `kullanicilar` DISABLE KEYS */;
INSERT INTO `kullanicilar` VALUES (1,'admin','1234');
/*!40000 ALTER TABLE `kullanicilar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sporcular`
--

DROP TABLE IF EXISTS `sporcular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sporcular` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(100) DEFAULT NULL,
  `soyad` varchar(100) DEFAULT NULL,
  `spor_dali` varchar(100) DEFAULT NULL,
  `dogum_tarihi` date DEFAULT NULL,
  `cinsiyet` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sporcular`
--

LOCK TABLES `sporcular` WRITE;
/*!40000 ALTER TABLE `sporcular` DISABLE KEYS */;
INSERT INTO `sporcular` VALUES (1,'Ali','Yılmaz','Fitness','1990-01-01','Erkek'),(2,'Ali','Yılmaz','Fitness','1990-03-15','Erkek'),(3,'Ayşe','Demir','Pilates','1995-07-22','Kadın'),(4,'Mehmet','Kara','Kickboks','1988-11-03','Erkek'),(5,'Elif','Çelik','Yoga','1992-02-10','Kadın'),(6,'Hasan','Koç','Vücut Geliştirme','1991-06-19','Erkek'),(7,'Zeynep','Aydın','Fonksiyonel','1998-04-08','Kadın'),(8,'Mert','Şahin','CrossFit','1993-12-01','Erkek'),(9,'Selin','Aslan','Koşu','1996-09-27','Kadın'),(10,'Burak','Güneş','Yüzme','1994-05-30','Erkek'),(11,'Derya','Polat','Aerobik','1990-08-12','Kadın');
/*!40000 ALTER TABLE `sporcular` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-17 14:38:08
