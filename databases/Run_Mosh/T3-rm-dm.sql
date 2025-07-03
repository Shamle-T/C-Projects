--****PLEASE ENTER YOUR DETAILS BELOW****
--T3-rm-dm.sql

--Student ID: 35512075
--Student Name: W.A.S.I.Thilaksiri

/* Comments for your marker:




*/

--(a)
DROP SEQUENCE competitor_seq;
DROP SEQUENCE team_seq;


CREATE SEQUENCE competitor_seq START WITH 100 INCREMENT BY 5;
CREATE SEQUENCE team_seq START WITH 100 INCREMENT BY 5 ;

   
COMMIT;


--(b)

-- Insert Keith Rose data into the competitor table
INSERT INTO COMPETITOR (
    comp_no,
    comp_fname,
    comp_lname,
    comp_gender,
    comp_dob,
    comp_email,
    comp_unistatus,
    comp_phone
) VALUES(competitor_seq.nextval,'Keith','Rose','M',TO_DATE('20/05/1994', 'DD/MM/YYYY'),'keith.rose@monash.com','Y','0422141112');

-- Insert Jackson Bull data into the competitor table
INSERT INTO COMPETITOR (
    comp_no,
    comp_fname,
    comp_lname,
    comp_gender,
    comp_dob,
    comp_email,
    comp_unistatus,
    comp_phone
) VALUES (competitor_seq.NEXTVAL, 'Jackson', 'Bull', 'M',TO_DATE('11/11/1996', 'DD/MM/YYYY'),'jackson.bull@monash.edu', 'Y', '0422412524');


-- Create an entry for Keith such that he can crete a team and join the event, for the moment keep the team as null
INSERT INTO ENTRY(
    event_id, 
    entry_no, 
    entry_starttime, 
    entry_finishtime, 
    entry_elapsedtime, 
    comp_no, 
    team_id, 
    char_id
    ) 
    VALUES (13,(SELECT NVL(MAX(entry_no), 0)+1 FROM entry WHERE event_id = 13),
        TO_DATE('08:30:00', 'HH24:MI:SS'),
        TO_DATE('09:15:00', 'HH24:MI:SS'),
        TO_DATE('00:45:00', 'HH24:MI:SS'),
        (SELECT comp_no FROM competitor WHERE comp_fname = 'Keith' AND comp_lname = 'Rose'),
        NULL,
        3   
    );


-- Create an entry for Jackson such that he can create a team and join the event, for the moment keep the event as null
INSERT INTO entry VALUES (    
    13,
    (SELECT NVL(MAX(entry_no), 0)+1 FROM entry WHERE event_id = 13),
    TO_DATE('08:30:00', 'HH24:MI:SS'),
    TO_DATE('09:20:00', 'HH24:MI:SS'),
    TO_DATE('00:50:00', 'HH24:MI:SS'),
    (SELECT comp_no FROM competitor WHERE comp_fname = 'Jackson' AND comp_lname = 'Bull'),
    NULL,
    1
);

-- Create a new team called Supper Runners, and set Keith as the team leader
INSERT INTO team VALUES (
    team_seq.NEXTVAL, 'Super Runners',
    TO_DATE('29/JUN/2025', 'DD/MON/YYYY'),
    13,
        (SELECT entry_no FROM entry e
        JOIN competitor c ON e.comp_no = c.comp_no
        WHERE c.comp_fname = 'Keith' AND c.comp_lname = 'Rose'
        AND e.event_id = 13)
);

-- Update the entry for both Keith and Rose such that the entry table is inked to team table
UPDATE entry
    SET team_id = team_seq.CURRVAL
    WHERE comp_no = (
        SELECT comp_no FROM competitor 
        WHERE comp_fname = 'Keith' AND comp_lname = 'Rose'
    )
    AND event_id = 13;



UPDATE entry
    SET team_id = team_seq.CURRVAL
    WHERE comp_no = (
        SELECT comp_no FROM competitor 
        WHERE comp_fname = 'Jackson' AND comp_lname = 'Bull'
    )
    AND event_id = 13;

COMMIT;
--(c)
--Task 3c

-- Update the entry table with 5Km run, where the event_id = 12, Use subquery to find the comp_no of Jackson Bull
UPDATE entry
    SET event_id = 12,  
    char_id = 2     
    WHERE comp_no = (
        SELECT comp_no FROM competitor 
        WHERE comp_fname = 'Jackson' AND comp_lname = 'Bull')
    AND event_id = 13;

COMMIT;

--(d)

-- Set the entry table team_id as null where the team 'Super Runner' is defined
UPDATE entry 
SET team_id = NULL 
WHERE team_id = (
    SELECT team_id FROM team 
    WHERE team_name = 'Super Runners' AND carn_date = TO_DATE('29/JUN/2025', 'DD/MON/YYYY'));

-- Delete team 'Super Runners'
DELETE FROM team
    WHERE team_name = 'Super Runners' AND carn_date = TO_DATE('29/JUN/2025', 'DD/MON/YYYY');

-- Delete the entry of Keith Rose from the entry table
DELETE FROM entry
    WHERE comp_no = (
        SELECT comp_no FROM competitor 
        WHERE comp_fname = 'Keith' AND comp_lname = 'Rose')
    AND event_id = 13;

-- Ensure Jackson Bull participates as an individual member
UPDATE entry
    SET team_id = NULL
    WHERE comp_no = (
        SELECT comp_no FROM competitor WHERE comp_fname = 'Jackson' AND comp_lname = 'Bull')
    AND event_id = 12;



COMMIT;