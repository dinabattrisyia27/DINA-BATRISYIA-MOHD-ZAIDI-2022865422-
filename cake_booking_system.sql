-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 02:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cake_booking_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `cake_booking`
--

CREATE TABLE `cake_booking` (
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `cake_var` varchar(20) NOT NULL,
  `quantity_var` int(10) NOT NULL,
  `member_card_var` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cake_booking`
--

INSERT INTO `cake_booking` (`name`, `email`, `cake_var`, `quantity_var`, `member_card_var`) VALUES
('D', 'D', 'Enchanted Eclair', 1, 'Yes'),
('DINA BATRISYIA', 'mintdina763@gmail.com', 'Sparkling Raspberry ', 1, 'Yes'),
('AISYATULLIEZA', 'Aisyatullieza004@gmail..com', 'Golden Chiffon Casca', 3, 'Yes'),
('NORNATASHABELLA', 'tachobell12@gmail.com', 'Golden Chiffon Casca', 3, 'Yes'),
('DAEWI IZZATY', 'wiwizzaty21@gmail.com', 'Royal Velvet Delight', 1, 'Yes'),
('ABID NAUFAL', 'abid_naufal@gmail.com', 'Velvet Symphony Cake', 1, 'Yes'),
('ALYA SYAUQINA', 'alya_syauqina@gmail.com', 'Midnight Bliss Cake', 2, 'Yes'),
('AKID NUFAIL', 'akid_nufail@gmail.com', 'Emerald Dream Cake', 1, 'Yes'),
('DHIA ZAHRA', 'dhia_zahra@gmail.com', 'Celestial Frosting F', 1, 'Yes'),
('ASSYA\'AFATUL UDZMA', 'udzma77@gmail.com', 'Caramel Elegance Sup', 1, 'Yes'),
('AKIF ZIYAD', 'akif_33@gmail.com', 'Enchanted Eclair', 1, 'Yes'),
('', '', '', 0, 'No'),
('', '', '', 0, 'No'),
('', '', '', 0, 'No');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
