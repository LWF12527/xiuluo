create database if not exists sancks;
use sancks;
CREATE TABLE IF NOT EXISTS `��Ʒ����` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `����` VARCHAR(255) NOT NULL,
  `����` VARCHAR(255) NOT NULL,
  `����` VARCHAR(255) NOT NULL,
  `���` VARCHAR(255) NOT NULL,
  `����λ` VARCHAR(255) NOT NULL,
  `�����` INT NOT NULL,
  `�ɱ�` FLOAT NOT NULL,
  `�ۼ�` FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS `��Ʒ������ˮ` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `��ˮ��` VARCHAR(255) NOT NULL,
  `����ʱ��` DATETIME NOT NULL,
  `��Ա��������` VARCHAR(255) NOT NULL,
  `��Ʒ����` VARCHAR(255) NOT NULL,
  `��Ʒ����` VARCHAR(255) NOT NULL,
  `���` VARCHAR(255) NOT NULL,
  `��λ` VARCHAR(255) NOT NULL,
  `��Ʒ����` VARCHAR(255) NOT NULL,
  `��������` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `�ɹ���¼` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `�ɹ�����` VARCHAR(255) NOT NULL,
  `�ɹ�ʱ��` DATETIME NOT NULL,
  `��Ӧ��` VARCHAR(255) NOT NULL,
  `��Ʒ����` VARCHAR(255) NOT NULL,
  `��Ʒ����` VARCHAR(255) NOT NULL,
  `��λ` VARCHAR(255) NOT NULL,
  `���` VARCHAR(255) NOT NULL,
  `�ɹ���` INT NOT NULL,
  `�ɹ�����` FLOAT NOT NULL
);

