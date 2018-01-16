# Python_With_MariaDB
This is a modifyed class project using Python 3 and a Sql DB (Maria DB).

##To Create the database entet the commands below.

### Creating the Table
create database alertDB;
grant all on alertDB.* to 'user' identified by 'password';
quit

### Accessing the db, in the mariadb cmd (Password = password)
mysql -u user -p alertDB

### Creating the table
create table alerts (
id int not null auto_increment primary key,
ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
alert_id varchar(64) not null,
alert_text text not null );

### Display the table
select * from alerts;
