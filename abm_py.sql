-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: abm_python
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `nombre_proveedor` varchar(45) NOT NULL,
  `telefono_proveedor` bigint DEFAULT NULL,
  `domicilio_proveedor` varchar(45) NOT NULL,
  `correo_proveedor` varchar(50) NOT NULL,
  PRIMARY KEY (`id_proveedor`),
  UNIQUE KEY `correo_proveedor_UNIQUE` (`correo_proveedor`),
  UNIQUE KEY `telefono_proveedor_UNIQUE` (`telefono_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'juan gomez',2604551200,'rivadavia 1500','juangomez55@gmail.com'),(2,'maria rodriguez',2604551001,'olascoaga 123','mariarodriguez1@gmail.com'),(3,'pedro lopez',2604551002,'santiago del estero 422','pedrolopez2@gmail.com'),(4,'ana martinez',2604551003,'san martin 921','anamartinez3@gmail.com'),(5,'luis perez',2604551004,'paunero 555','luisperez4@gmail.com'),(6,'laura garcia',2604551005,'rawson 847','lauragarcia5@gmail.com'),(7,'diego fernandez',2604551006,'san juan 200','diegofernandez6@gmail.com'),(8,'sofia diaz',2604551007,'matienzo 1279','sofiadiaz7@gmail.com'),(9,'carlos sanchez',2604551008,'anglat 881','carlossanchez8@gmail.com'),(10,'elena ramirez',2604551009,'uriburu 430','elenaramirez9@gmail.com');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-06 18:13:48
