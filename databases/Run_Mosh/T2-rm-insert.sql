/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T2-rm-insert.sql

--Student ID: 35512075
--Student Name: W.A.S.I.Thilaksiri

/* Comments for your marker:




*/
-- Task 2 Load the COMPETITOR, ENTRY and TEAM tables with your own
-- test data following the data requirements expressed in the brief

-- =======================================
-- COMPETITOR
-- =======================================
INSERT INTO COMPETITOR (
    comp_no,
    comp_fname,
    comp_lname,
    comp_gender,
    comp_dob,
    comp_email,
    comp_unistatus,
    comp_phone
) VALUES (1, 'Megan', 'Chang', 'F', TO_DATE('23/09/1988', 'DD/MM/YYYY'), 'megan.chang@monash.com', 'Y', '0466448162');
INSERT INTO COMPETITOR VALUES (2, 'Billy', 'Sheppard', 'M', TO_DATE('14/12/1990', 'DD/MM/YYYY'), 'billy.sheppard@monash.com', 'Y', '0444751217');
INSERT INTO COMPETITOR VALUES (3, 'Richard', 'Bowers', 'U', TO_DATE('27/09/1984', 'DD/MM/YYYY'), 'richard.bowers@monash.com', 'Y', '0475220111');
INSERT INTO COMPETITOR VALUES (4, 'Tammy', 'Howard', 'F', TO_DATE('04/10/2004', 'DD/MM/YYYY'), 'tammy.howard@monash.com', 'Y', '0450709944');
INSERT INTO COMPETITOR VALUES (5, 'Rebecca', 'Wagner', 'F', TO_DATE('04/01/1984', 'DD/MM/YYYY'), 'rebecca.wagner@monash.com', 'Y', '0458056573');
INSERT INTO COMPETITOR VALUES (6, 'Donald', 'Davis', 'U', TO_DATE('14/08/2001', 'DD/MM/YYYY'), 'donald.davis@monash.com', 'Y', '0439318886');
INSERT INTO COMPETITOR VALUES (7, 'John', 'Browning', 'U', TO_DATE('31/05/1998', 'DD/MM/YYYY'), 'john.browning@monash.com', 'Y', '0428693000');
INSERT INTO COMPETITOR VALUES (8, 'Lisa', 'Barrera', 'F', TO_DATE('21/12/1984', 'DD/MM/YYYY'), 'lisa.barrera@monash.com', 'Y', '0428756361');
INSERT INTO COMPETITOR VALUES (9, 'Corey', 'Jones', 'M', TO_DATE('11/05/2003', 'DD/MM/YYYY'), 'corey.jones@monash.com', 'N', '0492996081');
INSERT INTO COMPETITOR VALUES (10, 'Gabriella', 'Kennedy', 'F', TO_DATE('05/11/1977', 'DD/MM/YYYY'), 'gabriella.kennedy@monash.com', 'N', '0481479480');
INSERT INTO COMPETITOR VALUES (11, 'Michael', 'Stewart', 'U', TO_DATE('17/03/1996', 'DD/MM/YYYY'), 'michael.stewart@gmail.com', 'N', '0490785928');
INSERT INTO COMPETITOR VALUES (12, 'Robin', 'Levy', 'M', TO_DATE('26/08/1990', 'DD/MM/YYYY'), 'robin.levy@gmail.com', 'N', '0451627302');
INSERT INTO COMPETITOR VALUES (13, 'Scott', 'Boyd', 'M', TO_DATE('15/07/1976', 'DD/MM/YYYY'), 'scott.boyd@gmail.com', 'N', '0419897541');
INSERT INTO COMPETITOR VALUES (14, 'Linda', 'Dunn', 'U', TO_DATE('24/11/1974', 'DD/MM/YYYY'), 'linda.dunn@gmail.com', 'N', '0412519845');
INSERT INTO COMPETITOR VALUES (15, 'Edward', 'Griffin', 'M', TO_DATE('06/06/1982', 'DD/MM/YYYY'), 'edward.griffin@gmail.com', 'N', '0467885403');
INSERT INTO COMPETITOR VALUES (16, 'Tina', 'Morgan', 'F', TO_DATE('09/02/1993', 'DD/MM/YYYY'), 'tina.morgan@monash.com', 'Y', '0471234567');
INSERT INTO COMPETITOR VALUES (17, 'Alex', 'Nguyen', 'M', TO_DATE('22/11/1991', 'DD/MM/YYYY'), 'alex.nguyen@monash.com', 'N', '0438765432');




-- =======================================
-- ENTRY
-- =======================================
INSERT INTO ENTRY (event_id, entry_no, entry_starttime, entry_finishtime, entry_elapsedtime, comp_no, team_id, char_id) VALUES (4, 1, TO_DATE('08:33:00', 'HH24:MI:SS'), TO_DATE('09:08:00', 'HH24:MI:SS'), TO_DATE('00:35:00', 'HH24:MI:SS'), 1, NULL, 4);
INSERT INTO ENTRY VALUES (4, 2, TO_DATE('08:42:00', 'HH24:MI:SS'), TO_DATE('10:07:00', 'HH24:MI:SS'), TO_DATE('01:25:00', 'HH24:MI:SS'), 2, NULL, 1);
INSERT INTO ENTRY VALUES (4, 3, TO_DATE('08:02:00', 'HH24:MI:SS'), TO_DATE('09:25:00', 'HH24:MI:SS'), TO_DATE('01:23:00', 'HH24:MI:SS'), 3, NULL, 4);
INSERT INTO ENTRY VALUES (3, 1, TO_DATE('08:40:00', 'HH24:MI:SS'), TO_DATE('09:48:00', 'HH24:MI:SS'), TO_DATE('01:08:00', 'HH24:MI:SS'), 4, NULL, 3);
INSERT INTO ENTRY VALUES (5, 1, TO_DATE('08:02:00', 'HH24:MI:SS'), TO_DATE('08:28:00', 'HH24:MI:SS'), TO_DATE('00:26:00', 'HH24:MI:SS'), 5, NULL, 1);
INSERT INTO ENTRY VALUES (2, 1, TO_DATE('08:12:00', 'HH24:MI:SS'), TO_DATE('08:50:00', 'HH24:MI:SS'), TO_DATE('00:38:00', 'HH24:MI:SS'), 6, NULL, 4);
INSERT INTO ENTRY VALUES (6, 1, TO_DATE('08:00:00', 'HH24:MI:SS'), TO_DATE('09:22:00', 'HH24:MI:SS'), TO_DATE('01:22:00', 'HH24:MI:SS'), 7, NULL, 2);
INSERT INTO ENTRY VALUES (2, 2, TO_DATE('08:03:00', 'HH24:MI:SS'), TO_DATE('08:49:00', 'HH24:MI:SS'), TO_DATE('00:46:00', 'HH24:MI:SS'), 8, NULL, 2);
INSERT INTO ENTRY VALUES (3, 2, TO_DATE('08:14:00', 'HH24:MI:SS'), TO_DATE('09:18:00', 'HH24:MI:SS'), TO_DATE('01:04:00', 'HH24:MI:SS'), 9, NULL, 4);
INSERT INTO ENTRY VALUES (6, 2, TO_DATE('08:52:00', 'HH24:MI:SS'), TO_DATE('09:50:00', 'HH24:MI:SS'), TO_DATE('00:58:00', 'HH24:MI:SS'), 10, NULL, 2);
INSERT INTO ENTRY VALUES (3, 3, TO_DATE('08:52:00', 'HH24:MI:SS'), TO_DATE('09:50:00', 'HH24:MI:SS'), TO_DATE('00:58:00', 'HH24:MI:SS'), 11, NULL, 4);
INSERT INTO ENTRY VALUES (5, 2, TO_DATE('08:48:00', 'HH24:MI:SS'), TO_DATE('10:13:00', 'HH24:MI:SS'), TO_DATE('01:25:00', 'HH24:MI:SS'), 12, NULL, 1);
INSERT INTO ENTRY VALUES (4, 4, TO_DATE('08:26:00', 'HH24:MI:SS'), TO_DATE('09:15:00', 'HH24:MI:SS'), TO_DATE('00:49:00', 'HH24:MI:SS'), 13, NULL, 1);
INSERT INTO ENTRY VALUES (3, 4, TO_DATE('08:09:00', 'HH24:MI:SS'), TO_DATE('09:31:00', 'HH24:MI:SS'), TO_DATE('01:22:00', 'HH24:MI:SS'), 14, NULL, 1);
INSERT INTO ENTRY VALUES (4, 5, TO_DATE('08:03:00', 'HH24:MI:SS'), TO_DATE('09:19:00', 'HH24:MI:SS'), TO_DATE('01:16:00', 'HH24:MI:SS'), 15, NULL, 4);
INSERT INTO ENTRY VALUES (2, 3, TO_DATE('08:26:00', 'HH24:MI:SS'), TO_DATE('09:49:00', 'HH24:MI:SS'), TO_DATE('01:23:00', 'HH24:MI:SS'), 1, NULL, 4);
INSERT INTO ENTRY VALUES (2, 4, TO_DATE('08:34:00', 'HH24:MI:SS'), TO_DATE('09:44:00', 'HH24:MI:SS'), TO_DATE('01:10:00', 'HH24:MI:SS'), 2, NULL, 1);
INSERT INTO ENTRY VALUES (3, 5, TO_DATE('08:03:00', 'HH24:MI:SS'), TO_DATE('08:35:00', 'HH24:MI:SS'), TO_DATE('00:32:00', 'HH24:MI:SS'), 3, NULL, 1);
INSERT INTO ENTRY VALUES (5, 3, TO_DATE('08:23:00', 'HH24:MI:SS'), TO_DATE('09:36:00', 'HH24:MI:SS'), TO_DATE('01:13:00', 'HH24:MI:SS'), 4, NULL, 4);
INSERT INTO ENTRY VALUES (4, 6, TO_DATE('08:32:00', 'HH24:MI:SS'), TO_DATE('09:46:00', 'HH24:MI:SS'), TO_DATE('01:14:00', 'HH24:MI:SS'), 5, NULL, 3);
INSERT INTO ENTRY VALUES (5, 4, TO_DATE('08:36:00', 'HH24:MI:SS'), TO_DATE('09:31:00', 'HH24:MI:SS'), TO_DATE('00:55:00', 'HH24:MI:SS'), 6, NULL, 2);
INSERT INTO ENTRY VALUES (4, 7, TO_DATE('08:51:00', 'HH24:MI:SS'), TO_DATE('10:00:00', 'HH24:MI:SS'), TO_DATE('01:09:00', 'HH24:MI:SS'), 7, NULL, 3);
INSERT INTO ENTRY VALUES (1, 1, TO_DATE('08:42:00', 'HH24:MI:SS'), TO_DATE('10:10:00', 'HH24:MI:SS'), TO_DATE('01:28:00', 'HH24:MI:SS'), 8, NULL, 2);
INSERT INTO ENTRY VALUES (4, 8, TO_DATE('08:17:00', 'HH24:MI:SS'), TO_DATE('08:46:00', 'HH24:MI:SS'), TO_DATE('00:29:00', 'HH24:MI:SS'), 9, NULL, 2);
INSERT INTO ENTRY VALUES (2, 5, TO_DATE('08:29:00', 'HH24:MI:SS'), TO_DATE('09:27:00', 'HH24:MI:SS'), TO_DATE('00:58:00', 'HH24:MI:SS'), 10, NULL, 4);
INSERT INTO ENTRY VALUES (2, 6, TO_DATE('08:21:00', 'HH24:MI:SS'), TO_DATE('09:40:00', 'HH24:MI:SS'), TO_DATE('01:19:00', 'HH24:MI:SS'), 11, NULL, 2);
INSERT INTO ENTRY VALUES (3, 6, TO_DATE('08:27:00', 'HH24:MI:SS'), TO_DATE('09:03:00', 'HH24:MI:SS'), TO_DATE('00:36:00', 'HH24:MI:SS'), 12, NULL, 1);
INSERT INTO ENTRY VALUES (1, 2, TO_DATE('08:59:00', 'HH24:MI:SS'), TO_DATE('09:32:00', 'HH24:MI:SS'), TO_DATE('00:33:00', 'HH24:MI:SS'), 13, NULL, 4);
INSERT INTO ENTRY VALUES (6, 3, TO_DATE('08:21:00', 'HH24:MI:SS'), TO_DATE('09:20:00', 'HH24:MI:SS'), TO_DATE('00:59:00', 'HH24:MI:SS'), 14, NULL, 1);
INSERT INTO ENTRY VALUES (3, 7, TO_DATE('08:48:00', 'HH24:MI:SS'), TO_DATE('09:40:00', 'HH24:MI:SS'), TO_DATE('00:52:00', 'HH24:MI:SS'), 15, NULL, 2);
INSERT INTO ENTRY VALUES (4, 9, TO_DATE('08:29:00', 'HH24:MI:SS'), TO_DATE('09:10:00', 'HH24:MI:SS'), TO_DATE('00:41:00', 'HH24:MI:SS'), 16, NULL, 2);
INSERT INTO ENTRY VALUES (4, 10, TO_DATE('08:45:00', 'HH24:MI:SS'), TO_DATE('09:25:00', 'HH24:MI:SS'), TO_DATE('00:40:00', 'HH24:MI:SS'), 17, NULL, 3);





-- =======================================
-- TEAM
-- =======================================
INSERT INTO TEAM (team_id, team_name, carn_date, event_id, entry_no) 
VALUES (1, 'Cheetahs', TO_DATE('22/SEP/2024','DD/MON/YYYY'), 4, 1);
INSERT INTO TEAM VALUES (2, 'Tigers', TO_DATE('22/SEP/2024','DD/MON/YYYY'), 4, 2);
INSERT INTO TEAM VALUES (3, 'Cheetahs', TO_DATE('05/OCT/2024','DD/MON/YYYY'), 4, 5); 
INSERT INTO TEAM VALUES (4, 'Cheetahs', TO_DATE('02/FEB/2025','DD/MON/YYYY'), 4, 3); 
INSERT INTO TEAM VALUES (5, 'Falcons', TO_DATE('15/MAR/2025','DD/MON/YYYY'), 3, 1);
INSERT INTO TEAM VALUES (6, 'Panthers', TO_DATE('29/JUN/2025','DD/MON/YYYY'), 5, 1);

UPDATE entry SET team_id = 1 WHERE event_id = 4 AND entry_no = 1;

UPDATE entry SET team_id = 2 WHERE event_id = 4 AND entry_no = 2;

UPDATE entry SET team_id = 3 WHERE event_id = 4 AND entry_no = 5;

UPDATE entry SET team_id = 4 WHERE event_id = 4 AND entry_no = 3;

UPDATE entry SET team_id = 5 WHERE event_id = 3 AND entry_no = 1;

UPDATE entry SET team_id = 6 WHERE event_id = 5 AND entry_no = 1;

UPDATE entry SET team_id = 1 WHERE comp_no = 7 AND event_id = 4;

UPDATE entry SET team_id = 1 WHERE comp_no = 9 AND event_id = 4;

COMMIT;