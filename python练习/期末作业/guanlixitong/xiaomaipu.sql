-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: xiaomaipu
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_czech_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add 地点',7,'add_place'),(26,'Can change 地点',7,'change_place'),(27,'Can delete 地点',7,'delete_place'),(28,'Can view 地点',7,'view_place'),(29,'Can add 用户',8,'add_user'),(30,'Can change 用户',8,'change_user'),(31,'Can delete 用户',8,'delete_user'),(32,'Can view 用户',8,'view_user'),(33,'Can add 商品',9,'add_shop'),(34,'Can change 商品',9,'change_shop'),(35,'Can delete 商品',9,'delete_shop'),(36,'Can view 商品',9,'view_shop');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb3_czech_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_czech_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb3_czech_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb3_czech_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb3_czech_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$Bj6Bcclw5dugymzLfMcFDp$sYhDlDgFLfO90AqZjEMqwu5E4y+zCELymzYLXzR6fgY=','2023-12-27 16:00:46.001237',1,'admin','','','1@123.com',1,1,'2023-12-27 16:00:06.755793');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb3_czech_ci,
  `object_repr` varchar(200) COLLATE utf8mb3_czech_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb3_czech_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-28 13:42:59.152896','1','北六',1,'[{\"added\": {}}]',7,1),(2,'2023-12-28 13:43:48.569761','2','北七',1,'[{\"added\": {}}]',7,1),(3,'2023-12-28 13:44:03.220771','1','解子祥',1,'[{\"added\": {}}]',8,1),(4,'2023-12-28 13:45:07.093503','1','康师傅矿泉水',1,'[{\"added\": {}}]',9,1),(5,'2023-12-28 13:54:41.904098','2','康师傅冰糖雪梨',1,'[{\"added\": {}}]',9,1),(6,'2023-12-28 13:55:41.254701','3','凉白开',1,'[{\"added\": {}}]',9,1),(7,'2023-12-28 13:55:52.294745','3','凉白开',2,'[{\"changed\": {\"fields\": [\"\\u5269\\u4f59\\u6570\\u91cf\"]}}]',9,1),(8,'2023-12-28 13:58:02.681904','4','香辣牛肉面',1,'[{\"added\": {}}]',9,1),(9,'2023-12-28 13:58:25.054588','5','香辣牛肉面',1,'[{\"added\": {}}]',9,1),(10,'2023-12-28 14:32:31.318393','2','123',1,'[{\"added\": {}}]',8,1),(11,'2023-12-28 14:36:29.408072','6','凉白开',1,'[{\"added\": {}}]',9,1),(12,'2023-12-30 03:44:08.100411','6','凉白开',2,'[{\"changed\": {\"fields\": [\"\\u5546\\u54c1\\u56fe\\u7247\"]}}]',9,1),(13,'2023-12-30 03:49:08.114844','5','香辣牛肉面',2,'[{\"changed\": {\"fields\": [\"\\u5546\\u54c1\\u56fe\\u7247\"]}}]',9,1),(14,'2023-12-30 03:49:17.188647','4','香辣牛肉面',2,'[{\"changed\": {\"fields\": [\"\\u5546\\u54c1\\u56fe\\u7247\"]}}]',9,1),(15,'2023-12-30 03:49:31.178431','3','凉白开',2,'[{\"changed\": {\"fields\": [\"\\u5546\\u54c1\\u56fe\\u7247\"]}}]',9,1),(16,'2023-12-30 03:49:40.288369','2','康师傅冰糖雪梨',2,'[{\"changed\": {\"fields\": [\"\\u5546\\u54c1\\u56fe\\u7247\"]}}]',9,1),(17,'2023-12-30 03:49:50.395244','1','康师傅矿泉水',2,'[{\"changed\": {\"fields\": [\"\\u5546\\u54c1\\u56fe\\u7247\"]}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb3_czech_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'smallshop','place'),(9,'smallshop','shop'),(8,'smallshop','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb3_czech_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_czech_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-27 15:59:17.690499'),(2,'auth','0001_initial','2023-12-27 15:59:20.739333'),(3,'admin','0001_initial','2023-12-27 15:59:21.467038'),(4,'admin','0002_logentry_remove_auto_add','2023-12-27 15:59:21.494211'),(5,'admin','0003_logentry_add_action_flag_choices','2023-12-27 15:59:21.526302'),(6,'contenttypes','0002_remove_content_type_name','2023-12-27 15:59:21.885518'),(7,'auth','0002_alter_permission_name_max_length','2023-12-27 15:59:22.198500'),(8,'auth','0003_alter_user_email_max_length','2023-12-27 15:59:22.509424'),(9,'auth','0004_alter_user_username_opts','2023-12-27 15:59:22.539250'),(10,'auth','0005_alter_user_last_login_null','2023-12-27 15:59:22.798048'),(11,'auth','0006_require_contenttypes_0002','2023-12-27 15:59:22.815256'),(12,'auth','0007_alter_validators_add_error_messages','2023-12-27 15:59:22.843692'),(13,'auth','0008_alter_user_username_max_length','2023-12-27 15:59:23.171921'),(14,'auth','0009_alter_user_last_name_max_length','2023-12-27 15:59:23.492064'),(15,'auth','0010_alter_group_name_max_length','2023-12-27 15:59:23.776648'),(16,'auth','0011_update_proxy_permissions','2023-12-27 15:59:23.805088'),(17,'auth','0012_alter_user_first_name_max_length','2023-12-27 15:59:24.126755'),(18,'sessions','0001_initial','2023-12-27 15:59:24.312952'),(19,'smallshop','0001_initial','2023-12-27 15:59:25.175138'),(20,'smallshop','0002_alter_shop_price_alter_shop_prime_cost_and_more','2023-12-28 13:52:31.471867'),(21,'smallshop','0003_alter_shop_quantity_alter_shop_residual_quantity','2023-12-28 13:56:43.900231'),(22,'smallshop','0004_shop_msg','2023-12-30 03:37:38.201399');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb3_czech_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb3_czech_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('vifeoy6vcmjck9t8yjvk5klc5m8d14qf','.eJxVjMsOwiAQRf-FtSHDozK4dN9vIAMMUjU0Ke3K-O_apAvd3nPOfYlA21rD1nkJUxYXocTpd4uUHtx2kO_UbrNMc1uXKcpdkQftcpwzP6-H-3dQqddvbRKSAlTAg2Lno06AJltXELTyCUwZmKB4mzmqMzhAryFhZmujs2TE-wPHDDc0:1rIWKs:4dBZ3FzwKd1Yw4Q37cy6oFYeo6yBxBZSwrL-Pl0NMX0','2024-01-10 16:00:46.019466');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smallshop_place`
--

DROP TABLE IF EXISTS `smallshop_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `smallshop_place` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `place_name` varchar(40) COLLATE utf8mb3_czech_ci DEFAULT NULL,
  `detail_place` longtext COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smallshop_place`
--

LOCK TABLES `smallshop_place` WRITE;
/*!40000 ALTER TABLE `smallshop_place` DISABLE KEYS */;
INSERT INTO `smallshop_place` VALUES (1,'北六','河西学院北区六号楼'),(2,'北七','河西学院北区七号楼');
/*!40000 ALTER TABLE `smallshop_place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smallshop_shop`
--

DROP TABLE IF EXISTS `smallshop_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `smallshop_shop` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(40) COLLATE utf8mb3_czech_ci DEFAULT NULL,
  `prime_cost` double DEFAULT NULL,
  `price` double DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `residual_quantity` int DEFAULT NULL,
  `place_id` bigint DEFAULT NULL,
  `msg` varchar(100) COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smallshop_shop_place_id_a803656a_fk_smallshop_place_id` (`place_id`),
  CONSTRAINT `smallshop_shop_place_id_a803656a_fk_smallshop_place_id` FOREIGN KEY (`place_id`) REFERENCES `smallshop_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smallshop_shop`
--

LOCK TABLES `smallshop_shop` WRITE;
/*!40000 ALTER TABLE `smallshop_shop` DISABLE KEYS */;
INSERT INTO `smallshop_shop` VALUES (1,'康师傅矿泉水',0.8,1,20,17,1,'upload/covers/kuangquanshui.jpg'),(2,'康师傅冰糖雪梨',1.8,3,20,20,1,'upload/covers/bingtangxueli.jpg'),(3,'凉白开',1,2,10,10,1,'upload/covers/liangbaikai_3OCe0r9.jpg'),(4,'香辣牛肉面',2.8,4.5,20,20,1,'upload/covers/xianglaniuroumian_cRRvoA5.jpg'),(5,'香辣牛肉面',2.8,4.5,20,20,2,'upload/covers/xianglaniuroumian.jpg'),(6,'凉白开',1.2,2,20,20,2,'upload/covers/liangbaikai.jpg');
/*!40000 ALTER TABLE `smallshop_shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smallshop_user`
--

DROP TABLE IF EXISTS `smallshop_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `smallshop_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(40) COLLATE utf8mb3_czech_ci DEFAULT NULL,
  `password` varchar(40) COLLATE utf8mb3_czech_ci DEFAULT NULL,
  `place_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `smallshop_user_place_id_51517635_fk_smallshop_place_id` (`place_id`),
  CONSTRAINT `smallshop_user_place_id_51517635_fk_smallshop_place_id` FOREIGN KEY (`place_id`) REFERENCES `smallshop_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smallshop_user`
--

LOCK TABLES `smallshop_user` WRITE;
/*!40000 ALTER TABLE `smallshop_user` DISABLE KEYS */;
INSERT INTO `smallshop_user` VALUES (1,'解子祥','zxz',1),(2,'123','2',2);
/*!40000 ALTER TABLE `smallshop_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'xiaomaipu'
--

--
-- Dumping routines for database 'xiaomaipu'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-30 13:16:34
