--****PLEASE ENTER YOUR DETAILS BELOW****
--T4-rm-mods.sql

--Student ID: 35512075
--Student Name: W.A.S.I.Thilaksiri

/* Comments for your marker:




*/
--(a)


-- Alter competitor table to include a new attribute - completed_events of NUMBER(3)
ALTER TABLE competitor
ADD completed_events NUMBER(3); 

-- Comments on the newly added column
COMMENT ON COLUMN competitor.completed_events IS 
'Number of completed events';

-- Update the count of the compelted_events using a JOIN between the ENTRY table and the COMPETITOR table
UPDATE competitor c
SET completed_events = (
    SELECT COUNT(DISTINCT e.event_id)
    FROM entry e
    WHERE e.comp_no = c.comp_no
);

-- Displays the table strucutre
DESC competitor;

-- Testing to ensure the attribute has been added correctly to the table
SELECT comp_no, comp_fname, comp_lname, completed_events
FROM competitor
ORDER BY comp_no;

COMMIT;

--(b)

-- Create a table to resolve the many-to-many relationship
DROP TABLE entry_charity_split;

CREATE TABLE entry_charity_split (
    event_id        NUMBER(6),
    entry_no        NUMBER(5),
    char_id         NUMBER(3),
    percentage      NUMBER(3) CHECK (percentage BETWEEN 0 AND 100),

    CONSTRAINT entry_charity_split_pk PRIMARY KEY (event_id, entry_no, char_id),
    
    CONSTRAINT split_entry_fk FOREIGN KEY (event_id, entry_no)
        REFERENCES entry (event_id, entry_no),

    CONSTRAINT split_charity_fk FOREIGN KEY (char_id)
        REFERENCES charity (char_id)
);

COMMENT ON COLUMN entry_charity_split.percentage IS
'Percentage of total money funded to the charity (0-100)';

-- Remove the char_id from the entry table, since we are removing the link and creating the middle table

-- Insert into the entry_charity_split table the details of Jackson Bull
INSERT INTO entry_charity_split 
    VALUES (12, (SELECT entry_no FROM entry e
        JOIN competitor c ON e.comp_no = c.comp_no
        WHERE c.comp_fname = 'Jackson' AND c.comp_lname = 'Bull'
        AND e.event_id = 12),1,70);

INSERT INTO entry_charity_split 
    VALUES (12, (SELECT entry_no FROM entry e
        JOIN competitor c ON e.comp_no = c.comp_no
        WHERE c.comp_fname = 'Jackson' AND c.comp_lname = 'Bull'
        AND e.event_id = 12),2,30);

INSERT INTO entry_charity_split (event_id, entry_no, char_id, percentage)

SELECT event_id, entry_no, char_id, 100
FROM entry

WHERE char_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM competitor
    WHERE comp_fname = 'Jackson' AND comp_lname = 'Bull'
      AND comp_no = entry.comp_no
      AND event_id = 12
    );


DESC entry_charity_split;

SELECT * FROM entry_charity_split
ORDER BY event_id, entry_no;    

-- Remove the char_id from the entry table
ALTER TABLE entry DROP CONSTRAINT entry_char_id_fk;
ALTER TABLE entry DROP COLUMN char_id;

COMMIT;