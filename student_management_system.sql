-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2021 at 05:43 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`) VALUES
('admin@gcetts.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `announcement`
--

CREATE TABLE `announcement` (
  `aID` int(8) NOT NULL,
  `aName` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `announcement`
--

INSERT INTO `announcement` (`aID`, `aName`) VALUES
(1, 'Enrollment of the students for even semester 2021-2022 has been started\r\n'),
(2, 'Re-schedule of postponed examinations of 17.03.2021 to be held on 26.03.2021\r\n'),
(3, 'Internal Assessment marks of the students will be uploaded by 19/04/2021\r\n'),
(4, 'Data for MAR, MOOCs and Mentoring have been submitted by the colleges in the Examinations portal regularly and database is made available to all stake holders\n'),
(5, 'College will remain closed till June due to increased Covid cases in Bengal\n');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `sID` int(8) NOT NULL,
  `sName` varchar(32) NOT NULL,
  `rollNo` int(32) NOT NULL,
  `email` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `year` int(2) NOT NULL,
  `subjectID` int(8) NOT NULL,
  `stream` varchar(64) NOT NULL,
  `sem` int(2) NOT NULL,
  `sMark1` int(3) NOT NULL,
  `sMark2` int(3) NOT NULL,
  `sMark3` int(3) NOT NULL,
  `sMark4` int(3) NOT NULL,
  `sMark5` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sID`, `sName`, `rollNo`, `email`, `password`, `year`, `subjectID`, `stream`, `sem`, `sMark1`, `sMark2`, `sMark3`, `sMark4`, `sMark5`) VALUES
(1, 'Subhashis Chakraborty', 1100120001, 'ch.subha01@gmail.com', '1100120001', 1, 2, 'Computer Science & Engineering', 2, 77, 62, 93, 81, 74),
(2, 'Suniti Basak', 1100220001, 'bas.suniti2001@rediffmail.com', '1100220001', 1, 10, 'Information Technology', 2, 82, 79, 87, 75, 79);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subjectID` int(8) NOT NULL,
  `stream` varchar(64) NOT NULL,
  `sem` int(2) NOT NULL,
  `sub1` varchar(64) NOT NULL,
  `sub2` varchar(64) NOT NULL,
  `sub3` varchar(64) NOT NULL,
  `sub4` varchar(64) NOT NULL,
  `sub5` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subjectID`, `stream`, `sem`, `sub1`, `sub2`, `sub3`, `sub4`, `sub5`) VALUES
(1, 'Computer Science & Engineering', 1, 'English Language & Technical Communication', 'Physics-I', 'Mathematics-I', 'Engineering Mechanics', 'Basic Electrical & Electronic Engineering-I'),
(2, 'Computer Science & Engineering', 2, 'Basic Computation & Principles of Computer Program', 'Chemistry-I', 'Mathematics-II', 'Engineering Thermodynamics & Fluid Mechanics', 'Basic Electrical & Electronic Engineering-II'),
(3, 'Computer Science & Engineering', 3, 'Values & Ethics in Profession', 'Physics-II', 'Analog & Digital Electronics', 'Data Structure & Algorithm', 'Computer Organization'),
(4, 'Computer Science & Engineering', 4, 'Numerical Methods', 'Mathematics-III', 'Communication Engineering & Coding Theory', 'Formal Language & Automata Theory', 'Computer Architecture'),
(5, 'Computer Science & Engineering', 5, 'Economics for Engineers', 'Design & Analysis of Algorithm', 'Microprocessors & Microcontrollers', 'Discrete Mathematics', 'Object Oriented Programming'),
(6, 'Computer Science & Engineering', 6, 'Database Management System', 'Computer Networks', 'Operating System', 'Computer Graphics', 'Multimedia Technology'),
(7, 'Computer Science & Engineering', 7, 'Software Engineering', 'Compiler Design', 'Artificial Intelligence', 'Cloud Computing', 'Internet Technology'),
(8, 'Computer Science & Engineering', 8, 'Project Management', 'Cryptography & Network Security', 'Cyber Law & Security Policy', 'Project', 'Design Lab / Industrial problem related practical training'),
(9, 'Information Technology', 1, 'English Language & Technical Communication', 'Physics-I', 'Mathematics-I', 'Engineering Mechanics', 'Basic Electrical & Electronic Engineering-I'),
(10, 'Information Technology', 2, 'Basic Computation & Principles of Computer Program', 'Chemistry-I', 'Mathematics-II', 'Engineering Thermodynamics & Fluid Mechanics', 'Basic Electrical & Electronic Engineering-II'),
(11, 'Information Technology', 3, 'Values & Ethics in Profession', 'Physics-II', 'Analog & Digital Electronics', 'Data Structure & Algorithm', 'Computer Organization'),
(12, 'Information Technology', 4, 'Numerical Methods', 'Mathematics-III', 'Communication Engineering & Coding Theory', 'Formal Language & Automata Theory', 'Object Oriented Programming & UML'),
(13, 'Information Technology', 5, 'Economics for Engineers', 'Design & Analysis of Algorithm', 'Computer Architecture', 'Operating System', 'Programming Practices using C++'),
(14, 'Information Technology', 6, 'Database Management System', 'Computer Networking', 'Software Engineering', 'Computer Graphics', 'Artificial Intelligence'),
(15, 'Information Technology', 7, 'Internet Technology', 'Multimedia', 'E-Commerce', 'Distributed Operating System\r\n', 'Advanced Data Communication & Coding'),
(16, 'Information Technology', 8, 'Project Management', 'Natural Language Processing', 'Business Analytics', 'Project', 'Design Lab / Industrial problem related practical training');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `announcement`
--
ALTER TABLE `announcement`
  ADD PRIMARY KEY (`aID`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`sID`),
  ADD UNIQUE KEY `rollNo` (`rollNo`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fk_subjectID` (`subjectID`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subjectID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `announcement`
--
ALTER TABLE `announcement`
  MODIFY `aID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `sID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `subjectID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `fk_subjectID` FOREIGN KEY (`subjectID`) REFERENCES `subject` (`subjectID`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
