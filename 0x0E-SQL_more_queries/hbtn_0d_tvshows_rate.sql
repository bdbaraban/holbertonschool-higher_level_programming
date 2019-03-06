-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: hbtn_0d_tvshows_rate
-- ------------------------------------------------------
-- Server version	5.7.8-rc

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tv_genres`
--

DROP TABLE IF EXISTS `tv_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_genres`
--

LOCK TABLES `tv_genres` WRITE;
/*!40000 ALTER TABLE `tv_genres` DISABLE KEYS */;
INSERT INTO `tv_genres` VALUES (1,'Drama'),(2,'Mystery'),(3,'Adventure'),(4,'Fantasy'),(5,'Comedy'),(6,'Crime'),(7,'Suspense'),(8,'Thriller');
/*!40000 ALTER TABLE `tv_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_show_genres`
--

DROP TABLE IF EXISTS `tv_show_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_show_genres` (
  `show_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  KEY `show_id` (`show_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `tv_show_genres_ibfk_1` FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`),
  CONSTRAINT `tv_show_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `tv_genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_show_genres`
--

LOCK TABLES `tv_show_genres` WRITE;
/*!40000 ALTER TABLE `tv_show_genres` DISABLE KEYS */;
INSERT INTO `tv_show_genres` VALUES (2,1),(2,2),(3,3),(3,1),(3,4),(4,5),(5,5),(6,5),(7,6),(7,1),(7,7),(7,8),(9,6),(9,1),(9,2),(9,7),(9,8),(11,5),(11,1);
/*!40000 ALTER TABLE `tv_show_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_show_ratings`
--

DROP TABLE IF EXISTS `tv_show_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_show_ratings` (
  `show_id` int(11) NOT NULL,
  `rate` int(11) NOT NULL DEFAULT '0',
  KEY `show_id` (`show_id`),
  CONSTRAINT `tv_show_ratings_ibfk_1` FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_show_ratings`
--

LOCK TABLES `tv_show_ratings` WRITE;
/*!40000 ALTER TABLE `tv_show_ratings` DISABLE KEYS */;
INSERT INTO `tv_show_ratings` VALUES (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,0),(3,1),(3,2),(3,0),(3,0),(3,1),(3,2),(3,0),(3,0),(3,1),(3,2),(3,3),(3,4),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,0),(3,1),(3,2),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,0),(3,1),(3,2),(4,0),(5,0),(6,0),(6,0),(6,1),(6,2),(6,3),(6,4),(6,0),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(7,0),(7,1),(7,2),(7,0),(7,1),(7,2),(7,3),(7,4),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,0),(8,1),(8,2),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,0),(8,1),(8,2),(8,3),(8,4),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(9,0),(9,1),(9,2),(9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,0),(10,0),(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,0),(10,0),(10,1),(10,2),(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,0),(10,1),(10,2),(10,3),(10,4),(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,0),(10,1),(10,2),(11,0),(11,1),(11,2),(11,3),(11,4);
/*!40000 ALTER TABLE `tv_show_ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_shows`
--

DROP TABLE IF EXISTS `tv_shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_shows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_shows`
--

LOCK TABLES `tv_shows` WRITE;
/*!40000 ALTER TABLE `tv_shows` DISABLE KEYS */;
INSERT INTO `tv_shows` VALUES (2,'House'),(3,'Game of Thrones'),(4,'The Big Bang Theory'),(5,'New Girl'),(6,'Silicon Valley'),(7,'Breaking Bad'),(8,'Better Call Saul'),(9,'Dexter'),(10,'Homeland'),(11,'The Last Man on Earth');
/*!40000 ALTER TABLE `tv_shows` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-26 21:27:35
