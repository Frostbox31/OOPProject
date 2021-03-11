DROP TABLE IF EXISTS `weeklyprofit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weeklyprofit` (
  `Name` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Price` decimal DEFAULT NULL,
  `Profit` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `yearlyprofit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yearlyprofit` (
  `Name` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Price` decimal DEFAULT NULL,
  `Profit` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
DROP TABLE IF EXISTS `monthlyprofit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monthlyprofit` (
  `Name` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Price` decimal DEFAULT NULL,
  `Profit` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;