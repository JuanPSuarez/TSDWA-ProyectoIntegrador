-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bdtienda
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bdtienda
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bdtienda` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
-- -----------------------------------------------------
-- Schema proyectofinal
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyectofinal
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyectofinal` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bdtienda` ;

-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_rol` (
  `id_rol` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_rol`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_documento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_documento` (
  `id_tipo_documento` INT NOT NULL AUTO_INCREMENT,
  `descripcion` CHAR(10) NULL DEFAULT NULL,
  PRIMARY KEY (`id_tipo_documento`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`usuario` (
  `email` VARCHAR(50) NOT NULL,
  `id_tipo_documento` INT NOT NULL,
  `nro_documento` VARCHAR(20) NOT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `nombre` VARCHAR(50) NULL DEFAULT NULL,
  `id_rol` INT NULL DEFAULT NULL,
  `nro_telefono` VARCHAR(45) NULL DEFAULT NULL,
  `contraseña` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`email`),
  INDEX `id_rol_idx` (`id_rol` ASC) VISIBLE,
  INDEX `id_tipo_documento_idx` (`id_tipo_documento` ASC) VISIBLE,
  CONSTRAINT `id_rol`
    FOREIGN KEY (`id_rol`)
    REFERENCES `bdtienda`.`tipo_rol` (`id_rol`),
  CONSTRAINT `id_tipo_documento`
    FOREIGN KEY (`id_tipo_documento`)
    REFERENCES `bdtienda`.`tipo_documento` (`id_tipo_documento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_modo_pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_modo_pago` (
  `id_modo_pago` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  `nro_de_tarjeta` INT NULL,
  `tipo_de_tarjeta` VARCHAR(45) NULL,
  PRIMARY KEY (`id_modo_pago`, `descripcion`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`compra` (
  `id_compra` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(50) NOT NULL,
  `fecha` DATE NOT NULL,
  `id_modo_pago` INT NOT NULL,
  `nro_cuenta` VARCHAR(25) NOT NULL,
  `total` FLOAT NOT NULL,
  PRIMARY KEY (`id_compra`),
  INDEX `email_idx` (`email` ASC) VISIBLE,
  INDEX `id_modo_pago_idx` (`id_modo_pago` ASC) VISIBLE,
  INDEX `nro_cuenta_idx` (`nro_cuenta` ASC) VISIBLE,
  CONSTRAINT `email`
    FOREIGN KEY (`email`)
    REFERENCES `bdtienda`.`usuario` (`email`),
  CONSTRAINT `id_modo_pago`
    FOREIGN KEY (`id_modo_pago`)
    REFERENCES `bdtienda`.`tipo_modo_pago` (`id_modo_pago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_editorial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_editorial` (
  `id_editorial` INT NOT NULL AUTO_INCREMENT,
  `sinopsis` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_editorial`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_libro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_libro` (
  `id_libro` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) GENERATED ALWAYS AS () VIRTUAL,
  `autor` VARCHAR(45) NULL,
  `editor_editora` VARCHAR(45) NULL,
  `sinopsis` LONGTEXT NULL,
  PRIMARY KEY (`id_libro`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_producto` (
  `id_producto` INT NOT NULL AUTO_INCREMENT,
  `sinopsis` LONGTEXT NULL DEFAULT NULL,
  `id_libros` VARCHAR(40) NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  `imagen` VARCHAR(200) NULL DEFAULT NULL,
  `tipo_editorial_id_editorial` INT NOT NULL,
  `tipo_libro_id_libro` INT NOT NULL,
  PRIMARY KEY (`id_producto`),
  INDEX `fk_tipo_producto_tipo_editorial1_idx` (`tipo_editorial_id_editorial` ASC) VISIBLE,
  INDEX `fk_tipo_producto_tipo_libro1_idx` (`tipo_libro_id_libro` ASC) VISIBLE,
  CONSTRAINT `fk_tipo_producto_tipo_editorial1`
    FOREIGN KEY (`tipo_editorial_id_editorial`)
    REFERENCES `bdtienda`.`tipo_editorial` (`id_editorial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tipo_producto_tipo_libro1`
    FOREIGN KEY (`tipo_libro_id_libro`)
    REFERENCES `bdtienda`.`tipo_libro` (`id_libro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`detalle_compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`detalle_compra` (
  `id_compra` INT NOT NULL,
  `id_detalle_compra` INT NOT NULL,
  `id_producto` INT NULL DEFAULT NULL,
  `cantidad` INT NULL DEFAULT NULL,
  `importe` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`id_compra`, `id_detalle_compra`),
  INDEX `id_producto_idx` (`id_producto` ASC) VISIBLE,
  CONSTRAINT `id_compra`
    FOREIGN KEY (`id_compra`)
    REFERENCES `bdtienda`.`compra` (`id_compra`),
  CONSTRAINT `id_producto`
    FOREIGN KEY (`id_producto`)
    REFERENCES `bdtienda`.`tipo_producto` (`id_producto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_estado_entrega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_estado_entrega` (
  `id_estado_entrega` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_estado_entrega`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_departamento` (
  `id_departamento` INT NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_departamento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`tipo_localidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`tipo_localidad` (
  `id_localidad` INT NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `id_departamento` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_localidad`),
  INDEX `id_departamento_idx` (`id_departamento` ASC) VISIBLE,
  CONSTRAINT `id_departamento`
    FOREIGN KEY (`id_departamento`)
    REFERENCES `bdtienda`.`tipo_departamento` (`id_departamento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdtienda`.`entrega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdtienda`.`entrega` (
  `id_entrega` INT NOT NULL AUTO_INCREMENT,
  `id_compra` INT NULL DEFAULT NULL,
  `fecha_entrega` DATE NULL DEFAULT NULL,
  `id_estado_entrega` INT NULL DEFAULT NULL,
  `nro_seguimiento` VARCHAR(45) NULL DEFAULT NULL,
  `domicilio_entrega` VARCHAR(45) NULL DEFAULT NULL,
  `id_localidad` INT NULL DEFAULT NULL,
  `codigo_postal` VARCHAR(10) NULL DEFAULT NULL,
  `fecha_entrega` DATE NULL DEFAULT NULL,
  `telefono` VARCHAR(45) NULL DEFAULT NULL,
  `apellido_receptor` VARCHAR(45) NULL DEFAULT NULL,
  `nombre_receptor` VARCHAR(45) NULL DEFAULT NULL,
  `dni_receptor` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_entrega`),
  INDEX `compra_idx` (`id_compra` ASC) VISIBLE,
  INDEX `id_localidad_idx` (`id_localidad` ASC) VISIBLE,
  INDEX `localidad_idx` (`id_localidad` ASC) VISIBLE,
  INDEX `estado_entrega_idx` (`id_estado_entrega` ASC) VISIBLE,
  CONSTRAINT `compra`
    FOREIGN KEY (`id_compra`)
    REFERENCES `bdtienda`.`compra` (`id_compra`),
  CONSTRAINT `estado_entrega`
    FOREIGN KEY (`id_estado_entrega`)
    REFERENCES `bdtienda`.`tipo_estado_entrega` (`id_estado_entrega`),
  CONSTRAINT `localidad`
    FOREIGN KEY (`id_localidad`)
    REFERENCES `bdtienda`.`tipo_localidad` (`id_localidad`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `proyectofinal` ;

-- -----------------------------------------------------
-- Table `proyectofinal`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyectofinal`.`categoria` (
  `id_Categoria` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `TipoCategoria` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_Categoria`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyectofinal`.`jurisdiccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyectofinal`.`jurisdiccion` (
  `id_Jurisdiccion` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Jurisdiccion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_Jurisdiccion`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyectofinal`.`normativa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyectofinal`.`normativa` (
  `id_Normativa` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `NroNormativa` INT NOT NULL,
  `id_TipoNormativa` INT NOT NULL,
  `Fecha` DATE NOT NULL,
  `Descripcion` VARCHAR(450) NOT NULL,
  `id_Categoria` INT NOT NULL,
  `id_Jurisdiccion` INT NOT NULL,
  `id_OrganoLegislativo` INT NOT NULL,
  `PalabrasClave` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_Normativa`))
ENGINE = InnoDB
AUTO_INCREMENT = 31
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyectofinal`.`organolegislativo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyectofinal`.`organolegislativo` (
  `id_OrganoLegislativo` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `OrganoLegislativo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_OrganoLegislativo`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proyectofinal`.`tiponormativa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyectofinal`.`tiponormativa` (
  `id_TipoNormativa` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `TipoNormativa` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_TipoNormativa`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
