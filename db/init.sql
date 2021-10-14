-- Create database
CREATE DATABASE IF NOT EXISTS tutti;
use tutti;

-- Create syntax for TABLE 'queries'
CREATE TABLE IF NOT EXISTS `queries` (
  `Id` int(11) unsigned NOT NULL,
  `Query` char(63) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Create syntax for TABLE 'items'
CREATE TABLE IF NOT EXISTS `items` (
  `Id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `TuttiId` bigint(31) NOT NULL,
  `QueryId` int(11) DEFAULT NULL,
  `Title` char(63) DEFAULT NULL,
  `Description` char(255) DEFAULT NULL,
  `Price` char(15) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8;

-- Create syntax for TABLE 'subscriptions'
CREATE TABLE IF NOT EXISTS `subscriptions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `UserId` int(11) DEFAULT NULL,
  `QueryId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- Create syntax for TABLE 'users'
CREATE TABLE IF NOT EXISTS `users` (
  `Id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ChatId` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- OWN CODE
INSERT INTO queries (Id, Query)
VALUES
    (1, 'sonos'),
    (2, 'philips%20hue'),
    (3, '70%20200%20ef');