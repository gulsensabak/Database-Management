DROP DATABASE IF EXISTS VolleyballDataBase;
CREATE DATABASE volleyballdatabase;
USE volleyballdatabase;

CREATE TABLE manager(
	username VARCHAR(255),
    password VARCHAR(255)  NOT NULL,
	PRIMARY KEY (username)
);

# done
CREATE TABLE user(
	username VARCHAR(255),
    password VARCHAR(255)  NOT NULL,
    name VARCHAR(255),
	surname VARCHAR(255),
	PRIMARY KEY (username)
);

# done
CREATE TABLE coach(
	password VARCHAR(255),
	username VARCHAR(255),
    nationality VARCHAR(255) NOT NULL,
	FOREIGN KEY (username) REFERENCES user(username),
    PRIMARY KEY (username)
);

# done
CREATE TABLE jury(
	password VARCHAR(255),
	username VARCHAR(255),
    nationality VARCHAR(255) NOT NULL,
	FOREIGN KEY (username) REFERENCES user(username),
    PRIMARY KEY (username)
);

# done
CREATE TABLE player(
	password VARCHAR(255),
	username VARCHAR(255),
	team_list VARCHAR(255),
	position_list VARCHAR(255),
    height INT,
    weight INT,
    date_of_birth VARCHAR(255),
	FOREIGN KEY (username) REFERENCES user(username) ON UPDATE CASCADE,
    PRIMARY KEY (username)
);

# done
CREATE TABLE positions(
	position_ID INT,
    position_name VARCHAR(255),
    PRIMARY KEY (position_ID)
);

# done
CREATE TABLE team(
	team_ID INT, 
    channel_ID INT,
    team_name VARCHAR(255), 
    coach_username VARCHAR(255),
    contract_start VARCHAR(255) NOT NULL,
    contract_finish VARCHAR(255) NOT NULL,
    PRIMARY KEY (team_ID)
);

# done
CREATE TABLE tv_channel(
	channel_name VARCHAR(255) NOT NULL,
    channel_ID INT,
    UNIQUE (channel_name),
    PRIMARY KEY (channel_ID)
);

# done
CREATE TABLE stadium(
	stadium_ID INT, 
    stadium_name VARCHAR(255) NOT NULL, 
    stadium_country VARCHAR(255),
    UNIQUE (stadium_name),
	PRIMARY KEY (stadium_ID)
);

# done
CREATE TABLE match_session(
	session_ID INT,
    stadium_ID INT, 
	assigned_jury_username VARCHAR(255) NOT NULL,
	played_player_username_list JSON,
	team_id INT,
    date VARCHAR(255),
    time_slot INT,
    rating VARCHAR(5),
    PRIMARY KEY (session_ID),
    CHECK ((time_slot = 1) OR (time_slot = 2) OR (time_slot = 3))
);

# done
CREATE TABLE rate(
	username VARCHAR(255),
    session_ID INT,
    PRIMARY KEY (username, session_ID),
	FOREIGN KEY (username) REFERENCES jury(username),
    FOREIGN KEY (session_ID) REFERENCES match_session(session_ID) ON DELETE CASCADE
);

# done
CREATE TABLE being_in_an_aggreement(
	username VARCHAR(255),
    team_ID INT,
    FOREIGN KEY (username) REFERENCES coach(username),
    FOREIGN KEY (team_ID) REFERENCES team(team_ID),
    PRIMARY KEY (username, team_ID));
   
# done
CREATE TABLE has_aggreement(
	team_ID INT,
    channel_ID INT,
    UNIQUE (team_ID),
    PRIMARY KEY (channel_ID, team_ID),
    FOREIGN KEY (team_ID) REFERENCES team(team_ID),
    FOREIGN KEY (channel_ID) REFERENCES tv_channel(channel_ID));    
 
# done
CREATE TABLE register(
	username VARCHAR(255),
    team_ID INT,
    FOREIGN KEY (team_ID) REFERENCES team(team_ID),
	FOREIGN KEY (username) REFERENCES player(username),
    PRIMARY KEY (username, team_ID)
);
   
# done
CREATE TABLE at_where(
	session_ID INT,
    stadium_ID INT,
    FOREIGN KEY (session_ID) REFERENCES match_session(session_ID) ON DELETE CASCADE,
    FOREIGN KEY (stadium_ID) REFERENCES stadium(stadium_ID),
    PRIMARY KEY (session_ID, stadium_ID));
    
# done
CREATE TABLE play_in(
	username VARCHAR(255),
    position_ID INT,
    FOREIGN KEY (position_ID) REFERENCES positions(position_ID),
    FOREIGN KEY (username) REFERENCES player(username),
    PRIMARY KEY (position_ID, username));
    
# done  
CREATE TABLE t_matchs(
	team_ID INT NOT NULL,
    session_ID INT,
    PRIMARY KEY(session_ID),
    FOREIGN KEY(team_ID) REFERENCES team(team_ID));

# done
CREATE TABLE played_in_m(
	username VARCHAR(255),
    position_ID INT,
	session_ID INT,
    UNIQUE (session_ID, username),
    FOREIGN KEY (position_ID) REFERENCES positions(position_ID),
    FOREIGN KEY (username) REFERENCES player(username),
    PRIMARY KEY(session_ID, username)
);
-- DBManager
INSERT INTO manager (username, password) VALUES
('Kevin', 'Kevin'),
('Bob', 'Bob'),
('sorunlubirarkadas', 'muvaffakiyetsizleştiricileştiriveremeyebileceklerimizdenmişsinizcesine');

-- User table
INSERT INTO user (username, password, name, surname) VALUES
('g_orge', 'Go.1993', 'Gizem', 'Örge'),
('c_ozbay', 'Co.1996', 'Cansu', 'Özbay'),
('m_vargas', 'Mv.1999', 'Melissa', 'Vargas'),
('h_baladin', 'Hb.2007', 'Hande', 'Baladın'),
('a_kalac', 'Ak.1995', 'Aslı', 'Kalaç'),
('ee_dundar', 'Eed.2008', 'Eda Erdem', 'Dündar'),
('z_gunes', 'Zg.2008', 'Zehra', 'Güneş'),
('i_aydin', 'Ia.2007', 'İlkin', 'Aydın'),
('e_sahin', 'Es.2001', 'Elif', 'Şahin'),
('e_karakurt', 'Ek.2006', 'Ebrar', 'Karakurt'),
('s_akoz', 'Sa.1991', 'Simge', 'Aköz'),
('k_akman', 'Ka.2006', 'Kübra', 'Akman'),
('d_cebecioglu', 'Dc.2007', 'Derya', 'Cebecioğlu'),
('a_aykac', 'Aa.1996', 'Ayşe', 'Aykaç'),
('user_2826', 'P.45825', 'Brenda', 'Schulz'),
('user_9501', 'P.99695', 'Erika', 'Foley'),
('user_3556', 'P.49595', 'Andrea', 'Campbell'),
('user_7934', 'P.24374', 'Beatrice', 'Bradley'),
('user_4163', 'P.31812', 'Betsey', 'Lenoir'),
('user_2835', 'P.51875', 'Martha', 'Lazo'),
('user_8142', 'P.58665', 'Wanda', 'Ramirez'),
('user_2092', 'P.16070', 'Eileen', 'Ryen'),
('user_3000', 'P.73005', 'Stephanie', 'White'),
('user_8323', 'P.33562', 'Daenerys', 'Targaryen'),
('d_santarelli', 'santa.really1', 'Daniele', 'Santarelli'),
('g_guidetti', 'guidgio.90', 'Giovanni', 'Guidetti'),
('f_akbas', 'a.fatih55', 'Ferhat', 'Akbaş'),
('m_hebert', 'm.hebert45', 'Mike', 'Hebert'),
('o_deriviere', 'oliviere_147', 'Oliviere', 'Deriviere'),
('a_derune', 'aderune_147', 'Amicia', 'Derune'),
('o_ozcelik', 'ozlem.0347', 'Özlem', 'Özçelik'),
('m_sevinc', 'mehmet.0457', 'Mehmet', 'Sevinç'),
('e_sener', 'ertem.4587', 'Ertem', 'Şener'),
('s_engin', 'sinan.6893', 'Sinan', 'Engin');


-- Coach
INSERT INTO coach (username, nationality, password) VALUES
('d_santarelli', 'ITA', 'santa.really1'),
('g_guidetti', 'ITA', 'guidgio.90'),
('f_akbas', 'TR', 'a.fatih55'),
('m_hebert', 'US', 'm.hebert45'),
('o_deriviere', 'FR', 'oliviere_147'),
('a_derune', 'FR', 'aderune_147');

-- Jury
INSERT INTO jury (username, nationality, password) VALUES
('o_ozcelik', 'TR', 'ozlem.0347'),
('m_sevinc', 'TR', 'mehmet.0457'),
('e_sener', 'TR', 'ertem.4587'),
('s_engin', 'TR', 'sinan.6893');


-- Player
INSERT INTO player (username, date_of_birth, height, weight, password) VALUES
('g_orge', '1993-04-26', 170, 59, 'Go.1993'),
('c_ozbay', '1996-10-17', 182, 78, 'Co.1996'),
('m_vargas', '1999-10-16', 194, 76, 'Mv.1999'),
('h_baladin', '2007-09-01', 190, 81, 'Hb.2007'),
('a_kalac', '1995-12-13', 185, 73, 'Ak.1995'),
('ee_dundar', '2008-06-22', 188, 74, 'Eed.2008'),
('z_gunes', '2008-07-07', 197, 88, 'Zg.2008'),
('i_aydin', '2007-01-05', 183, 67, 'Ia.2007'),
('e_sahin', '2001-01-19', 190, 68, 'Es.2001'),
('e_karakurt', '2006-01-17', 196, 73, 'Ek.2006'),
('s_akoz', '1991-04-23', 168, 55, 'Sa.1991'),
('k_akman', '2006-10-13', 200, 88, 'Ka.2006'),
('d_cebecioglu', '2007-10-24', 187, 68, 'Dc.2007'),
('a_aykac', '1996-02-27', 176, 57, 'Aa.1996'),
('user_2826', '2002-12-13', 193, 80, 'P.45825'),
('user_9501', '1995-12-21', 164, 62, 'P.99695'),
('user_3556', '1996-04-26', 185, 100, 'P.49595'),
('user_7934', '1997-05-28', 150, 57, 'P.24374'),
('user_4163', '1993-05-07', 156, 48, 'P.31812'),
('user_2835', '2001-05-20', 173, 71, 'P.51875'),
('user_8142', '1994-01-03', 183, 94, 'P.58665'),
('user_2092', '2004-06-21', 188, 60, 'P.16070'),
('user_3000', '2002-05-19', 193, 74, 'P.73005'),
('user_8323', '2006-09-16', 222, 74, 'P.33562');


-- Channel
INSERT INTO tv_channel (channel_ID, channel_name) VALUES
(0, 'BeIN Sports'),
(1, 'Digiturk'),
(2, 'TRT');

-- Team
INSERT INTO team (team_ID, team_name, coach_username, contract_start, contract_finish, channel_ID) VALUES
(0, 'Women A', 'd_santarelli', '2021-12-25', '2025-12-12', 0),
(1, 'Women B', 'g_guidetti', '2021-09-11', '2026-09-11', 1),
(2, 'U19', 'f_akbas', '2021-08-10', '2026-08-10', 0),
(3, 'Women B', 'f_akbas', '2000-08-10', '2015-08-10', 1),
(4, 'Women C', 'm_hebert', '2024-04-01', '2026-07-21', 1),
(5, 'U19', 'o_deriviere', '2015-08-10', '2020-08-09', 2),
(6, 'U19', 'a_derune', '2005-08-10', '2010-08-10', 2);


-- Position
INSERT INTO positions (position_ID, position_name) VALUES
(0, 'Libero'),
(1, 'Setter'),
(2, 'Opposite hitter'),
(3, 'Outside hitter'),
(4, 'Middle blocker');

-- Stadium
INSERT INTO stadium (stadium_ID, stadium_name, stadium_country) VALUES
(0, 'Burhan Felek Voleybol Salonu', 'TR'),
(1, 'GD Voleybol Arena', 'TR'),
(2, 'Copper Box Arena', 'UK');

-- MatchSession !!!!!
INSERT INTO match_session (session_ID, team_id, stadium_ID, time_slot, date, assigned_jury_username, rating, played_player_username_list) VALUES
(0, 0, 0, 1, '2024-03-10', 'o_ozcelik', 4.5, '["g_orge", "c_ozbay", "m_vargas", "h_baladin", "a_kalac", "ee_dundar"]'),
(1, 1, 1, 1, '2024-04-03', 'o_ozcelik', 4.9, '["c_ozbay", "m_vargas", "i_aydin", "a_kalac", "s_akoz", "d_cebecioglu"]'),
(2, 0, 1, 3, '2024-04-03', 'o_ozcelik', 4.4, '["g_orge", "m_vargas", "c_ozbay", "a_kalac", "s_akoz", "a_aykac"]'),
(3, 2, 2, 2, '2024-04-03', 'm_sevinc', 4.9, '["ee_dundar", "h_baladin", "z_gunes", "i_aydin", "e_karakurt", "k_akman"]'),
(4, 3, 2, 2, '2023-04-03', 'e_sener', 4.5, '["user_2826", "user_9501", "user_3556", "user_7934", "user_4163", "user_2835"]'),
(5, 3, 1, 1, '2023-05-27', 's_engin', 4.4, '["user_2826", "user_9501", "user_3556", "user_7934", "user_4163", "user_2835"]'),
(6, 0, 1, 1, '2022-09-01', 'm_sevinc', 4.6, '["g_orge", "m_vargas", "c_ozbay", "a_kalac", "e_karakurt", "a_aykac"]'),
(7, 0, 2, 3, '2023-05-02', 'o_ozcelik', 4.7, '["g_orge", "m_vargas", "c_ozbay", "a_kalac", "e_karakurt", "a_aykac"]'),
(8, 1, 0, 1, '2024-02-10', 'o_ozcelik', 4.5, '["g_orge", "m_vargas", "c_ozbay", "a_kalac", "e_karakurt", "a_aykac"]');


INSERT INTO rate (session_ID, username) VALUES
(0, 'o_ozcelik'),
(1, 'o_ozcelik'),
(2, 'o_ozcelik'),
(3, 'm_sevinc'),
(4, 'e_sener'),
(5, 's_engin'),
(6, 'm_sevinc'),
(7, 'o_ozcelik'),
(8, 'o_ozcelik');



INSERT INTO register (username, team_ID) VALUES
('g_orge', 0),
('c_ozbay', 0),
('c_ozbay', 1),
('m_vargas', 0),
('m_vargas', 1),
('h_baladin', 0),
('h_baladin', 2),
('a_kalac', 0),
('a_kalac', 1),
('ee_dundar', 0),
('ee_dundar', 2),
('z_gunes', 0),
('z_gunes', 2),
('i_aydin', 1),
('i_aydin', 2),
('e_sahin', 0),
('e_karakurt', 0),
('e_karakurt', 2),
('s_akoz', 0),
('s_akoz', 1),
('k_akman', 0),
('k_akman', 2),
('d_cebecioglu', 0),
('d_cebecioglu', 1),
('a_aykac', 0),
('user_2826', 2),
('user_2826', 3),
('user_9501', 0),
('user_9501', 3),
('user_3556', 2),
('user_3556', 3),
('user_7934', 0),
('user_7934', 3),
('user_4163', 1),
('user_4163', 3),
('user_2835', 2),
('user_2835', 3),
('user_8142', 0),
('user_8142', 3),
('user_2092', 2),
('user_2092', 3),
('user_3000', 2),
('user_3000', 3),
('user_8323', 0),
('user_8323', 3);


-- PlayerPositions
INSERT INTO play_in (username, position_ID) VALUES
('g_orge', 0),
('g_orge', 3),
('c_ozbay', 1),
('m_vargas', 2),
('h_baladin', 3),
('a_kalac', 4),
('ee_dundar', 4),
('z_gunes', 4),
('i_aydin', 1),
('i_aydin', 3),
('e_sahin', 1),
('e_sahin', 3),
('e_karakurt', 2),
('e_karakurt', 3),
('s_akoz', 0),
('k_akman', 0),
('k_akman', 4),
('d_cebecioglu', 3),
('d_cebecioglu', 4),
('a_aykac', 0),
('user_2826', 2),
('user_2826', 1),
('user_9501', 0),
('user_9501', 4),
('user_3556', 1),
('user_3556', 0),
('user_7934', 4),
('user_7934', 2),
('user_4163', 3),
('user_4163', 0),
('user_2835', 2),
('user_2835', 3),
('user_8142', 1),
('user_8142', 3),
('user_2092', 4),
('user_2092', 2),
('user_3000', 1),
('user_3000', 4),
('user_8323', 3),
('user_8323', 2);


-- SessionSquads
INSERT INTO played_in_m (session_ID, username, position_ID) VALUES
(0, 'g_orge', 0),
(0, 'c_ozbay', 1),
(0, 'm_vargas', 2),
(0, 'h_baladin', 3),
(0, 'a_kalac', 4),
(0, 'ee_dundar', 4),
(1, 'c_ozbay', 1),
(1, 'm_vargas', 2),
(1, 'i_aydin', 1),
(1, 'a_kalac', 4),
(1, 's_akoz', 0),
(1, 'd_cebecioglu', 3),
(2, 'g_orge', 3),
(2, 'm_vargas', 2),
(2, 'c_ozbay', 1),
(2, 'a_kalac', 4),
(2, 's_akoz', 0),
(2, 'a_aykac', 0),
(3, 'ee_dundar', 4),
(3, 'h_baladin', 3),
(3, 'z_gunes', 4),
(3, 'i_aydin', 3),
(3, 'e_karakurt', 2),
(3, 'k_akman', 0),
(4, 'user_2826', 2),
(4, 'user_9501', 0),
(4, 'user_3556', 1),
(4, 'user_7934', 4),
(4, 'user_4163', 3),
(4, 'user_2835', 2),
(5, 'user_2826', 1),
(5, 'user_9501', 4),
(5, 'user_3556', 0),
(5, 'user_7934', 2),
(5, 'user_4163', 0),
(5, 'user_2835', 3),
(6, 'g_orge', 0),
(6, 'm_vargas', 2),
(6, 'c_ozbay', 1),
(6, 'a_kalac', 4),
(6, 'e_karakurt', 3),
(6, 'a_aykac', 0),
(7, 'g_orge', 3),
(7, 'm_vargas', 2),
(7, 'c_ozbay', 1),
(7, 'a_kalac', 4),
(7, 'e_karakurt', 2),
(7, 'a_aykac', 0);


INSERT INTO has_aggreement (channel_ID, team_ID) VALUES
(0, 0),
(1, 1),
(0, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 6);


INSERT INTO being_in_an_aggreement (username, team_ID) VALUES
('d_santarelli', 0),
('g_guidetti', 1),
('f_akbas', 2),
('f_akbas', 3),
('m_hebert', 4),
('o_deriviere', 5),
('a_derune', 6);


-- Mock data for t_match
INSERT INTO t_matchs (session_ID, team_id) VALUES
(0, 0),
(1, 1),
(2, 0),
(3, 2),
(4, 3),
(5, 3),
(6, 0),
(7, 0),
(8, 1);


-- Mock data for at_where
INSERT INTO at_where (session_ID, stadium_ID) VALUES
(0, 0),
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 1),
(6, 1),
(7, 2),
(8, 0);



DELIMITER //
CREATE TRIGGER israted BEFORE UPDATE ON match_session
    IF (NEW.rating IS NOT NULL) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You have already rated.';
    END IF;
DELIMITER ;

DELIMITER //
CREATE TRIGGER person_bi BEFORE INSERT ON match_session
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM match_session
        WHERE date = NEW.date
        AND time_slot = NEW.time_slot
        AND stadium_ID = NEW.stadium_ID
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot insert due to data conflict.';
    END IF;
END //
DELIMITER ;






