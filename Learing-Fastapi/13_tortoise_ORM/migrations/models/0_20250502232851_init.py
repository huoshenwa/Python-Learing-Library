from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL COMMENT '课程名称',
    `code` VARCHAR(20) NOT NULL UNIQUE COMMENT '课程代码',
    `credit` INT NOT NULL COMMENT '学分',
    `description` LONGTEXT COMMENT '课程描述'
) CHARACTER SET utf8mb4 COMMENT='课程模型';
CREATE TABLE IF NOT EXISTS `department` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL UNIQUE COMMENT '院系名称',
    `code` VARCHAR(20) NOT NULL UNIQUE COMMENT '院系代码',
    `established_date` DATE NOT NULL COMMENT '成立日期'
) CHARACTER SET utf8mb4 COMMENT='院系模型';
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL COMMENT '学生姓名',
    `student_id` VARCHAR(20) NOT NULL UNIQUE COMMENT '学号',
    `enrollment_date` DATE NOT NULL COMMENT '入学日期',
    `department_id` INT NOT NULL COMMENT '所属院系',
    CONSTRAINT `fk_student_departme_d624840b` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='学生模型';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4 COMMENT='所选课程';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
