DROP TABLE IF EXISTS `barweeklyprofit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barweeklyprofit` (
  `Name` varchar(45) DEFAULT NULL,
  `StartD` varchar(45) DEFAULT NULL,
  `EndD` varchar(45) DEFAULT NULL,
  `Profit` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `baryearlyprofit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baryearlyprofit` (
  `Name` varchar(45) DEFAULT NULL,
  `StartD` varchar(45) DEFAULT NULL,
  `EndD` varchar(45) DEFAULT NULL,
  `Profit` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `barmonthlyprofit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barmonthlyprofit` (
  `Name` varchar(45) DEFAULT NULL,
  `StartD` varchar(45) DEFAULT NULL,
  `EndD` varchar(45) DEFAULT NULL,
  `Profit` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;