-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: fyp
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lawyers`
--

DROP TABLE IF EXISTS `lawyers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lawyers` (
  `name` varchar(38) DEFAULT NULL,
  `address` varchar(127) DEFAULT NULL,
  `contact` varchar(18) DEFAULT NULL,
  `email_website` varchar(60) DEFAULT NULL,
  `category` varchar(158) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lawyers`
--

LOCK TABLES `lawyers` WRITE;
/*!40000 ALTER TABLE `lawyers` DISABLE KEYS */;
INSERT INTO `lawyers` VALUES ('Mohammad Akram Sheikh','Senior Advocate Supreme Court of Pakistan','+92 51 2274386-87','akramsheikh@asla.pk','Civil, Criminal cases','Lahore'),('Aazad Law Associates','19A Abbot Road Barq Plaza\r\n2nd Floor\r\nLahore 54000\r\nPakistan','+92 (34) 6446-5967','','Court Marriage, Divorce, Business & Family Law','Lahore'),('Rana Ijaz & Partners','','+92 (42) 3731-2828','https://www.linkedin.com/company/rana-ijaz-&-partners/about/','Advisory and Commercial Litigation','Lahore'),('Salman Khurshid Law Associates','14-A Dayal Singh Mansion, The Mall Lahore 54000,Pakistan','+92 300-4231842','','Civil, Corporate, Commercial and Criminal laws.','Lahore'),('G.N.Q. Advocates and Legal Consultants','Office No. 2, 3rd Floor, Silver City Plaza, G-11 Markaz, Islamabad','+92 336 329 3159','http://www.gnqlegal.com','Corporate Law; Commercial Law; Income Tax Law; Intellectual Property Law; Information Technology Law; Cyber Law; Defamation Law; Constitutional and Civil Law.','Islamabad'),('AFZAL LAW CHAMBER','D 754atellite town rawalpindi,','0514456244','http://www.myislamabad.net','family and civil cases','rawalpindi/islamabad'),('AAM Law Associates','84 Kh.Shrif Block Rawalpindi','+923335214773','','corporate law , civil, criminal, firm registration, income tax, sales tax, immigration, trade mark','rawalpindi/islamabad'),('Sattar and Sattar','Executive Counsel\r\n3rd Floor, UBL Building\r\nI.I. Chundrigar Road, Karachi','92 300 823 6688','lawstar@cyber.net.pk','Corporate and company law, banking and finance, investment advisory services, patents and copyrights.','karachi'),('Jamil & Jamil','Mr. Zahid U. Jamil\r\nBarrister-at-Law\r\n219-221, Central Hotel Annex\r\nAbdullah Haroon Road\r\nKarachi','92 (21) 3568 0760','zjamil@cyber.net.pk','International finance, matters relating to the WTO, securities, banking, corporate, commercial, privatization, intellectual property, trademark & copy right.','karachi'),('M. ILYAS KHAN & ASSOCIATES','106 -108 Asad Chambers, 146 Shambunath Street, off Passport Office, Saddar, Karachi. Pakistan','92-300-825 5495','ilyaskhan@cyber.net.pk','Banking/Financial, Civil Damages, Corporations, Foreign Investments, Theft/Fraud/ Embezzlement, Contracts.','karachi'),('Yasir Khattak Lawyer, Peshawar','Zeb Plaza, G.T. Road, Tehkal Bala, Peshawar','','https://www.peshawar.co/peshawar/Yasir-Khattak-Lawyer-1423','civil law , criminal law','peshawar'),('KakaKhel Law Associaties , Peshawar','Cantonment Plaza, 36-C 2nd Floor, Saddar Road, Peshawar Cantt, Peshawar','0334-4440744','','civil law,family law','peshawar'),('Jaffar Ali Qazi Advocate','H/12, K-3, Phase 3\r\nHayatabad, Khyber Pakhtunkhwa\r\nPeshawar 25000\r\nPakistan','92 91 5817132 ','','Civil, Faimly, Labour, Customs, Sales Tax and Income Tax Law Firm','peshawar'),('Isaac Law Associates','HSE 12, Sector K-3\r\nPhase III, Hayatabad\r\nPeshawar 25000\r\nPakistan\r\nHSE 12, Sector K-3\r\nPhase III, Hayatabad\r\nPeshawar 25000\r\nP','92 91 5817132','','civil rights, bankruptcy,criminal law, employment, immigration, tax ','peshawar'),('S & A Law Associates','50-Justice R.Tariq Mahmood Block2nd Floor District Kutchery\r\nMultan 6000\r\nPakistan','92 333 6181901 ','','family law, banking and finance , divorce','multan '),('Nblc','Chamber 148, 1st flour Sufi Barkat Building, District Courts\r\nFaisalabad 38000\r\nPakistan','92 (300) 4218121 ','','Family and Civil Law','faisalabad'),('Mandviwalla & Zafar','356-A, Ikram Plaza, 2nd Floor, Small D Ground, Peoples Colony No.1\r\nFaisalabad\r\nPakistan','92 41 8555696 ','','Commercial, Corporate, Investment, Banking & Finance Law','faisalabad'),('Syed Muhammad Bilal','','','','family , property , criminal , civil,','quetta'),('Temor Hussain','','','https://www.facebook.com/temorhassani','Criminal laws, Civil Laws & Services Laws','quetta');
/*!40000 ALTER TABLE `lawyers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-13 12:53:56
