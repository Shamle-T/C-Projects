/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T5-rm-select.sql

--Student ID: 35512075
--Student Name: W.A.S.I.Thilaksiri


/* Comments for your marker:



/* 

(a) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer
SELECT 
    t.team_name AS "TEAM_NAME", TO_CHAR(t.carn_date, 'DD-MON-YYYY') AS "CARNIVAL_DATE", c.comp_fname || ' ' || c.comp_lname AS "TEAMLEADER",  m.team_member_count AS "TEAM_NO_MEMBERS" 
    FROM team t JOIN entry e ON t.event_id = e.event_id AND t.entry_no = e.entry_no
    JOIN competitor c ON e.comp_no = c.comp_no
    JOIN (
        SELECT team_id, COUNT(*) AS team_member_count
        FROM entry
        WHERE team_id IS NOT NULL
        GROUP BY team_id
    ) m ON t.team_id = m.team_id
    WHERE t.carn_date < SYSDATE
    AND t.team_name IN ( SELECT team_name
            FROM team
            WHERE carn_date < SYSDATE
            GROUP BY team_name
            HAVING COUNT(*) = ( SELECT MAX(team_count)
                    FROM ( SELECT COUNT(*) AS team_count
                        FROM team
                        WHERE carn_date < SYSDATE
                        GROUP BY team_name
                )
            )
        )
ORDER BY t.team_name, t.carn_date;



/* (b) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer


SELECT
    TRIM(t.eventtype_desc) AS "Event", c.carn_name || ' held ' || TRIM(TO_CHAR(c.carn_date, 'DY DD-Mon-YYYY')) AS "Carnival", TO_CHAR(e.entry_elapsedtime, 'HH24:MI:SS') AS "Current Record",
    TRIM(LPAD(co.comp_no,5,'0')) || ' ' || TRIM(co.comp_fname || ' ' || co.comp_lname) AS "Competitor No and Name", FLOOR(MONTHS_BETWEEN(e.entry_starttime, co.comp_dob) / 12) AS "Age at Carnival"
FROM
    entry e
    JOIN competitor co ON e.comp_no = co.comp_no
    JOIN event ev ON e.event_id = ev.event_id
    JOIN eventtype t ON ev.eventtype_code = t.eventtype_code
    JOIN carnival c ON ev.carn_date = c.carn_date
WHERE
    (ev.eventtype_code, e.entry_elapsedtime) IN (
        SELECT ev2.eventtype_code, MIN(e2.entry_elapsedtime)
        FROM entry e2
        JOIN event ev2 ON e2.event_id = ev2.event_id
        GROUP BY ev2.eventtype_code
    )
ORDER BY t.eventtype_desc, co.comp_no;




/* (c) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT
    c.carn_name AS "Carnival Name", TO_CHAR(c.carn_date, 'DD Mon YYYY') AS "Carnival Date", et.eventtype_desc AS "Event Description", 
    CASE 
        WHEN COUNT(e.entry_no) = 0 THEN 'Not offered'
        ELSE LPAD(COUNT(e.entry_no), 18)
    END AS "Number of Entries",

    CASE 
        WHEN COUNT(e.entry_no) = 0 THEN ''
        ELSE LPAD(TO_CHAR(ROUND(COUNT(e.entry_no) * 100 / total.total_entries)), 25)
    END AS "% of Carnival Entries"
    
    FROM carnival c
    
    JOIN event v ON c.carn_date = v.carn_date
    
    JOIN eventtype et ON v.eventtype_code = et.eventtype_code
    
    LEFT JOIN entry e ON v.event_id = e.event_id
    
    JOIN (
        SELECT v.carn_date, COUNT(e.entry_no) AS total_entries
        FROM event v
        JOIN entry e ON v.event_id = e.event_id
        GROUP BY v.carn_date
    ) total ON c.carn_date = total.carn_date

    GROUP BY
        c.carn_name, c.carn_date, et.eventtype_desc, total.total_entries
    ORDER BY
        c.carn_date,
        COUNT(e.entry_no) DESC,
        et.eventtype_desc;

