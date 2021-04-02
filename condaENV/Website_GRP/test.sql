-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 02, 2021 at 06:55 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_swedish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add project', 7, 'add_project'),
(26, 'Can change project', 7, 'change_project'),
(27, 'Can delete project', 7, 'delete_project'),
(28, 'Can view project', 7, 'view_project'),
(29, 'Can add video artefact', 8, 'add_videoartefact'),
(30, 'Can change video artefact', 8, 'change_videoartefact'),
(31, 'Can delete video artefact', 8, 'delete_videoartefact'),
(32, 'Can view video artefact', 8, 'view_videoartefact'),
(33, 'Can add user profile info', 9, 'add_userprofileinfo'),
(34, 'Can change user profile info', 9, 'change_userprofileinfo'),
(35, 'Can delete user profile info', 9, 'delete_userprofileinfo'),
(36, 'Can view user profile info', 9, 'view_userprofileinfo'),
(37, 'Can add image artefact', 10, 'add_imageartefact'),
(38, 'Can change image artefact', 10, 'change_imageartefact'),
(39, 'Can delete image artefact', 10, 'delete_imageartefact'),
(40, 'Can view image artefact', 10, 'view_imageartefact');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_swedish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_swedish_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_swedish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_swedish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_swedish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'argon2$argon2i$v=19$m=512,t=2,p=2$ODZrZDdHVUNhUnVp$5z3RZuz63YKesLMGVp090A', '2021-04-02 16:17:00.664280', 1, 'user', 'admin', 'user', 'user@email.com', 1, 1, '2021-04-02 15:14:11.000000'),
(2, 'argon2$argon2i$v=19$m=512,t=2,p=2$TUduRGNJYnVGRWlI$avQb3EzYlESKdHVBT2HWgw', '2021-04-02 16:13:47.233828', 0, 'JohnDoe', 'John', 'Doe', 'JohnDoe@email.com', 0, 1, '2021-04-02 15:15:33.021687'),
(3, 'argon2$argon2i$v=19$m=512,t=2,p=2$cTFua1hMN2kwbmVD$GVSdFrosxYONy9zaN0HCTA', '2021-04-02 16:15:49.356761', 0, 'MSmith', 'Michael', 'Smith', 'MSmith@email.com', 0, 1, '2021-04-02 15:16:31.242160'),
(4, 'argon2$argon2i$v=19$m=512,t=2,p=2$WUhWTEtYYmZ6bUps$hgvBpRTamgp42g3rFakZcQ', '2021-04-02 16:15:32.592271', 0, 'MJackson', 'Michael', 'Jackson', 'MJack@email.com', 0, 1, '2021-04-02 15:17:04.977705'),
(5, 'argon2$argon2i$v=19$m=512,t=2,p=2$UVJucDhXeGlKN3RB$LRAtemLQLvQx+BvhXwCn4A', '2021-04-02 16:16:03.737566', 0, 'NBread', 'Natsu', 'Bread', 'NBread@email.com', 0, 1, '2021-04-02 15:17:47.561489');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_swedish_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8_swedish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8_swedish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-04-02 15:14:38.246997', '1', 'user', 1, '[{\"added\": {}}]', 9, 1),
(2, '2021-04-02 15:18:00.693999', '1', 'user', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1),
(3, '2021-04-02 15:25:25.783126', '3', 'MyProject3', 2, '[{\"changed\": {\"fields\": [\"Project Approval Status\"]}}]', 7, 1),
(4, '2021-04-02 15:25:25.922517', '2', 'MyProject 2', 2, '[{\"changed\": {\"fields\": [\"Project Approval Status\"]}}]', 7, 1),
(5, '2021-04-02 15:25:26.257914', '1', 'MyProject1', 2, '[{\"changed\": {\"fields\": [\"Project Approval Status\"]}}]', 7, 1),
(6, '2021-04-02 15:26:21.296758', '1', 'MyProject1', 2, '[{\"changed\": {\"fields\": [\"Upload Date\", \"Approval Date\", \"Account ExpiryDate\", \"Last Updated\"]}}]', 7, 1),
(7, '2021-04-02 15:26:36.419639', '2', 'MyProject 2', 2, '[{\"changed\": {\"fields\": [\"Approval Date\", \"Account ExpiryDate\"]}}]', 7, 1),
(8, '2021-04-02 15:27:05.459713', '3', 'MyProject3', 2, '[{\"changed\": {\"fields\": [\"Upload Date\", \"Account ExpiryDate\", \"Last Updated\"]}}]', 7, 1),
(9, '2021-04-02 15:49:06.857770', '5', 'My Project 5', 2, '[{\"changed\": {\"fields\": [\"Project Approval Status\"]}}]', 7, 1),
(10, '2021-04-02 15:49:06.966965', '4', 'MyProject 4', 2, '[{\"changed\": {\"fields\": [\"Project Approval Status\"]}}]', 7, 1),
(11, '2021-04-02 15:49:21.026201', '3', 'MyProject 3', 2, '[{\"changed\": {\"fields\": [\"Project Name\"]}}]', 7, 1),
(12, '2021-04-02 15:49:28.024981', '1', 'MyProject 1', 2, '[{\"changed\": {\"fields\": [\"Project Name\"]}}]', 7, 1),
(13, '2021-04-02 15:49:37.753036', '5', 'MyProject 5', 2, '[{\"changed\": {\"fields\": [\"Project Name\"]}}]', 7, 1),
(14, '2021-04-02 15:49:43.165115', '6', 'MyProject 6', 2, '[{\"changed\": {\"fields\": [\"Project Name\"]}}]', 7, 1),
(15, '2021-04-02 15:52:11.203543', '7', 'MyProject 7', 1, '[{\"added\": {}}]', 7, 1),
(16, '2021-04-02 15:52:37.286055', '6', 'Artefact 6', 1, '[{\"added\": {}}]', 10, 1),
(17, '2021-04-02 15:52:56.996771', '7', 'Artefact 7', 1, '[{\"added\": {}}]', 10, 1),
(18, '2021-04-02 15:53:11.564168', '8', 'Arteafact 8', 1, '[{\"added\": {}}]', 10, 1),
(19, '2021-04-02 15:53:18.863392', '8', 'Artefact 8', 2, '[{\"changed\": {\"fields\": [\"Image Name\"]}}]', 10, 1),
(20, '2021-04-02 15:53:48.232844', '4', 'Video Artefact 4: artefacts/V_Artefact_4.mp4', 1, '[{\"added\": {}}]', 8, 1),
(21, '2021-04-02 15:54:41.681949', '7', 'MyProject 7', 2, '[{\"changed\": {\"fields\": [\"Project Tag\", \"Module Name\"]}}]', 7, 1),
(22, '2021-04-02 15:56:06.123381', '8', 'MyProject8', 1, '[{\"added\": {}}]', 7, 1),
(23, '2021-04-02 15:59:16.975397', '9', 'MyProject 9', 1, '[{\"added\": {}}]', 7, 1),
(24, '2021-04-02 15:59:25.341144', '8', 'MyProject 8', 2, '[{\"changed\": {\"fields\": [\"Project Name\"]}}]', 7, 1),
(25, '2021-04-02 16:00:07.919079', '5', 'Video Artefact 5: artefacts/V_Artefact_5.mp4', 1, '[{\"added\": {}}]', 8, 1),
(26, '2021-04-02 16:00:29.826692', '6', 'Video Artefact 6: artefacts/V_Artefact_6.mp4', 1, '[{\"added\": {}}]', 8, 1),
(27, '2021-04-02 16:01:11.538818', '9', 'Artefact 9', 1, '[{\"added\": {}}]', 10, 1),
(28, '2021-04-02 16:01:30.905766', '10', 'Artefact 10', 1, '[{\"added\": {}}]', 10, 1),
(29, '2021-04-02 16:02:15.156855', '9', 'Artefact 9', 2, '[{\"changed\": {\"fields\": [\"Project Owner\"]}}]', 10, 1),
(30, '2021-04-02 16:07:48.050002', '11', 'Artefact 17', 1, '[{\"added\": {}}]', 10, 1),
(31, '2021-04-02 16:08:01.633351', '12', 'Artefact 18', 1, '[{\"added\": {}}]', 10, 1),
(32, '2021-04-02 16:08:50.975866', '13', 'Artefact 19', 1, '[{\"added\": {}}]', 10, 1),
(33, '2021-04-02 16:09:19.475218', '14', 'Artefact 20', 1, '[{\"added\": {}}]', 10, 1),
(34, '2021-04-02 16:11:03.509262', '10', 'MyProject 10', 1, '[{\"added\": {}}]', 7, 1),
(35, '2021-04-02 16:12:54.356177', '15', 'Artefact 21', 1, '[{\"added\": {}}]', 10, 1),
(36, '2021-04-02 16:13:05.570479', '16', 'Artefact 22', 1, '[{\"added\": {}}]', 10, 1),
(37, '2021-04-02 16:21:15.794098', '18', 'Artefact 24', 1, '[{\"added\": {}}]', 10, 1),
(38, '2021-04-02 16:25:59.839920', '18', 'Artefact 24', 2, '[{\"changed\": {\"fields\": [\"Project Owner\"]}}]', 10, 1),
(39, '2021-04-02 16:26:29.970472', '18', 'Artefact 24', 2, '[{\"changed\": {\"fields\": [\"Project Owner\"]}}]', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'home_page', 'imageartefact'),
(7, 'home_page', 'project'),
(9, 'home_page', 'userprofileinfo'),
(8, 'home_page', 'videoartefact'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_swedish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_swedish_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-04-02 15:08:32.689968'),
(2, 'auth', '0001_initial', '2021-04-02 15:08:34.670844'),
(3, 'admin', '0001_initial', '2021-04-02 15:08:51.924811'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-04-02 15:08:57.801643'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-04-02 15:08:57.987268'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-04-02 15:09:01.635420'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-04-02 15:09:05.805078'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-04-02 15:09:09.147436'),
(9, 'auth', '0004_alter_user_username_opts', '2021-04-02 15:09:09.256673'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-04-02 15:09:11.389267'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-04-02 15:09:11.523905'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-04-02 15:09:11.633612'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-04-02 15:09:12.514962'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-04-02 15:09:14.249407'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-04-02 15:09:22.314645'),
(16, 'auth', '0011_update_proxy_permissions', '2021-04-02 15:09:22.550802'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-04-02 15:09:23.358645'),
(18, 'home_page', '0001_initial', '2021-04-02 15:09:29.562107'),
(19, 'sessions', '0001_initial', '2021-04-02 15:09:38.330033');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_swedish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_swedish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('34f3op1d3q6myelxuk0p802zls9tw5bh', '.eJxVjEEOwiAQRe_C2pDCBAZcuvcMZBhAqgaS0q6Md9cmXej2v_f-SwTa1hq2kZcwJ3EWSpx-t0j8yG0H6U7t1iX3ti5zlLsiDzrktaf8vBzu30GlUb81qsmx8h4jaoXM6CEpKmgoGrDOW8uT1gUzI1oAyMkBeTBJWw8Wi3h_ALy2NtY:1lSMTk:qoHwk1BvdNsZA2O6JKbqKXIceTmx7tESZGsQHwvhfyw', '2021-04-16 16:17:00.731325');

-- --------------------------------------------------------

--
-- Table structure for table `home_page_imageartefact`
--

CREATE TABLE `home_page_imageartefact` (
  `id` int(11) NOT NULL,
  `Image_Name` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  `Image_Description` longtext COLLATE utf8_swedish_ci NOT NULL,
  `image` varchar(100) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Project_Owner_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `home_page_imageartefact`
--

INSERT INTO `home_page_imageartefact` (`id`, `Image_Name`, `Image_Description`, `image`, `Project_Owner_id`) VALUES
(1, 'Artefact 1', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_1.jpg', 1),
(2, 'Artefact 2', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_2.gif', 1),
(3, 'Artefact 3', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_3.jpg', 2),
(4, 'Artefact 4', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_4.gif', 4),
(5, 'Artefact 5', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_5.gif', 6),
(6, 'Artefact 6', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_6.jpg', 7),
(7, 'Artefact 7', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_7.jpg', 7),
(8, 'Artefact 8', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_8.gif', 7),
(9, 'Artefact 9', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_9.jpg', 5),
(10, 'Artefact 10', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_10.jpg', 6),
(11, 'Artefact 17', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_17.jpg', 2),
(12, 'Artefact 18', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_18.jpg', 2),
(13, 'Artefact 19', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_19.jpg', 5),
(14, 'Artefact 20', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_20.jpg', 5),
(15, 'Artefact 21', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_21.jpg', 4),
(16, 'Artefact 22', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_22.jpg', 4),
(17, 'Artefact 23', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/Artefact_23.jpg', 8),
(18, 'Artefact 24', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/260743.jpg', 9);

-- --------------------------------------------------------

--
-- Table structure for table `home_page_project`
--

CREATE TABLE `home_page_project` (
  `id` int(11) NOT NULL,
  `Project_Name` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  `Project_Description` longtext COLLATE utf8_swedish_ci NOT NULL,
  `Project_Tag` varchar(32) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Module_Name` varchar(32) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Date_of_Completion` date NOT NULL,
  `Author_Comment` longtext COLLATE utf8_swedish_ci DEFAULT NULL,
  `Upload_Date` date NOT NULL,
  `Approval_Date` date DEFAULT NULL,
  `Account_ExpiryDate` date DEFAULT NULL,
  `Last_Updated` date DEFAULT NULL,
  `Project_Approval_Status` varchar(32) COLLATE utf8_swedish_ci NOT NULL,
  `Authors` varchar(100) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Admin_Comment` longtext COLLATE utf8_swedish_ci DEFAULT NULL,
  `User_Owner_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `home_page_project`
--

INSERT INTO `home_page_project` (`id`, `Project_Name`, `Project_Description`, `Project_Tag`, `Module_Name`, `Date_of_Completion`, `Author_Comment`, `Upload_Date`, `Approval_Date`, `Account_ExpiryDate`, `Last_Updated`, `Project_Approval_Status`, `Authors`, `Admin_Comment`, `User_Owner_id`) VALUES
(1, 'MyProject 1', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.', 'Data Scholarship', 'Data Scholarship', '2021-04-01', 'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', '2021-03-03', '2021-03-09', '2021-03-11', '2021-03-04', 'Approved', 'Michael Smith', '', 3),
(2, 'MyProject 2', 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English.', 'Digital Media Production', 'Digital Media Production', '2021-04-09', 'Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident.', '2021-04-02', '2021-04-02', '2021-04-30', '2021-04-02', 'Approved', 'Michael Smith', '', 3),
(3, 'MyProject 3', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don\'t look even slightly believable.', 'Technologies for Learning', 'Technologies for Learning', '2021-04-02', 'If you are going to use a passage of Lorem Ipsum, you need to be sure there isn\'t anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.', '2021-03-17', NULL, '2021-03-24', '2021-03-17', 'Rejected', 'Michael Smith', '', 3),
(4, 'MyProject 4', 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia,', 'Technologies for Learning', 'Technologies for Learning', '2021-04-08', ', looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.', '2021-04-02', NULL, '2021-04-09', '2021-04-02', 'Approved', 'Natsu Bread', NULL, 5),
(5, 'MyProject 5', '\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"', 'Digital Media Production', 'Digital Media Production', '2021-04-03', '\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet', '2021-04-02', NULL, '2021-04-09', '2021-04-02', 'Approved', 'Natsu Bread', '', 5),
(6, 'MyProject 6', 'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure,', 'Technologies for Learning', 'Technologies for Learning', '2021-04-02', 'But because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?', '2021-04-02', NULL, '2021-04-09', '2021-04-02', 'Pending', 'Natsu Bread', '', 5),
(7, 'MyProject 7', '\"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.', 'Data Scholarship', 'Data Scholarship', '2021-04-02', 'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.', '2021-04-02', '2021-04-02', '2021-04-09', '2021-04-02', 'Approved', 'John Doe and Mary Jane', '', 2),
(8, 'MyProject 8', 'Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.\"', 'Data Scholarship', 'Data Scholarship', '2021-04-02', '\"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will,', '2021-03-25', NULL, '2021-04-02', '2021-03-25', 'Pending', 'John Doe', '', 2),
(9, 'MyProject 9', 'which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided.', 'Digital Media Production', 'Digital Media Production', '2021-04-02', 'But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.\"', '2021-04-02', '2021-04-02', '2021-04-02', '2021-04-02', 'Approved', 'John Doe', '', 2),
(10, 'MyProject 10', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,', 'Data Scholarship', 'Data Scholarship', '2021-04-02', 'Adipiscing at in tellus integer feugiat. Enim tortor at auctor urna nunc id cursus metus aliquam. Tellus orci ac auctor augue mauris augue neque gravida in. Nec tincidunt praesent semper feugiat nibh sed pulvinar proin. Quis viverra nibh cras pulvinar mattis nunc sed blandit', '2021-04-02', NULL, '2021-07-08', '2021-04-02', 'Rejected', 'John Doe and Bob Ross', '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `home_page_userprofileinfo`
--

CREATE TABLE `home_page_userprofileinfo` (
  `id` int(11) NOT NULL,
  `StudentID` int(10) UNSIGNED NOT NULL CHECK (`StudentID` >= 0),
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `home_page_userprofileinfo`
--

INSERT INTO `home_page_userprofileinfo` (`id`, `StudentID`, `user_id`) VALUES
(1, 1, 1),
(2, 20120000, 2),
(3, 20121111, 3),
(4, 20122222, 4),
(5, 20123333, 5);

-- --------------------------------------------------------

--
-- Table structure for table `home_page_videoartefact`
--

CREATE TABLE `home_page_videoartefact` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  `Video_Description` longtext COLLATE utf8_swedish_ci DEFAULT NULL,
  `videofile` varchar(100) COLLATE utf8_swedish_ci DEFAULT NULL,
  `thumbnail` varchar(100) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Project_Owner_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `home_page_videoartefact`
--

INSERT INTO `home_page_videoartefact` (`id`, `name`, `Video_Description`, `videofile`, `thumbnail`, `Project_Owner_id`) VALUES
(1, 'Video Artefact 1', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/V_Artefact_1.mp4', 'artefacts/Artefact_16.jpg', 4),
(2, 'Video Artefact 2', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/V_Artefact_2.mp4', 'artefacts/Artefact_15.jpg', 5),
(3, 'Video Artefact 3', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/V_Artefact_3.mp4', 'artefacts/Artefact_14.jpg', 6),
(4, 'Video Artefact 4', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/V_Artefact_4.mp4', 'artefacts/Artefact_13.jpg', 7),
(5, 'Video Artefact 5', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/V_Artefact_5.mp4', 'artefacts/Artefact_12.jpg', 9),
(6, 'Video Artefact 6', 'This is the description of my artefact that is oftenly used in this dummy picture description , as it will enable to easily see which one is the description', 'artefacts/V_Artefact_6.mp4', 'artefacts/Artefact_11.jpg', 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `home_page_imageartefact`
--
ALTER TABLE `home_page_imageartefact`
  ADD PRIMARY KEY (`id`),
  ADD KEY `home_page_imageartef_Project_Owner_id_28c31366_fk_home_page` (`Project_Owner_id`);

--
-- Indexes for table `home_page_project`
--
ALTER TABLE `home_page_project`
  ADD PRIMARY KEY (`id`),
  ADD KEY `home_page_project_User_Owner_id_4a6721f9_fk_home_page` (`User_Owner_id`);

--
-- Indexes for table `home_page_userprofileinfo`
--
ALTER TABLE `home_page_userprofileinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `StudentID` (`StudentID`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `home_page_videoartefact`
--
ALTER TABLE `home_page_videoartefact`
  ADD PRIMARY KEY (`id`),
  ADD KEY `home_page_videoartef_Project_Owner_id_2a53c745_fk_home_page` (`Project_Owner_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `home_page_imageartefact`
--
ALTER TABLE `home_page_imageartefact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `home_page_project`
--
ALTER TABLE `home_page_project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `home_page_userprofileinfo`
--
ALTER TABLE `home_page_userprofileinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `home_page_videoartefact`
--
ALTER TABLE `home_page_videoartefact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `home_page_imageartefact`
--
ALTER TABLE `home_page_imageartefact`
  ADD CONSTRAINT `home_page_imageartef_Project_Owner_id_28c31366_fk_home_page` FOREIGN KEY (`Project_Owner_id`) REFERENCES `home_page_project` (`id`);

--
-- Constraints for table `home_page_project`
--
ALTER TABLE `home_page_project`
  ADD CONSTRAINT `home_page_project_User_Owner_id_4a6721f9_fk_home_page` FOREIGN KEY (`User_Owner_id`) REFERENCES `home_page_userprofileinfo` (`id`);

--
-- Constraints for table `home_page_userprofileinfo`
--
ALTER TABLE `home_page_userprofileinfo`
  ADD CONSTRAINT `home_page_userprofileinfo_user_id_48f8474c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `home_page_videoartefact`
--
ALTER TABLE `home_page_videoartefact`
  ADD CONSTRAINT `home_page_videoartef_Project_Owner_id_2a53c745_fk_home_page` FOREIGN KEY (`Project_Owner_id`) REFERENCES `home_page_project` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
