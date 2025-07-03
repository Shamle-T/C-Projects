/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T6-rm-json.sql

--Student ID: 35512075
--Student Name: W.A.S.I.Thilaksiri


/* Comments for your marker:




*/


-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer
SELECT JSON_OBJECT(
  '_id' VALUE t.team_id,
  'carn_name' VALUE c.carn_name,
  'carn_date' VALUE TO_CHAR(c.carn_date, 'DD-Mon-YYYY'),
  'team_name' VALUE t.team_name,
  'team_leader' VALUE JSON_OBJECT(
    'name' VALUE comp.comp_fname || ' ' || comp.comp_lname,
    'phone' VALUE comp.comp_phone,
    'email' VALUE comp.comp_email
  ),

  'team_no_of_members' VALUE COUNT(*),
  'team_members' VALUE JSON_ARRAYAGG(
    JSON_OBJECT(

      'competitor_name' VALUE r.comp_fname || ' ' || r.comp_lname,
      'competitor_phone' VALUE r.comp_phone,
      'event_type' VALUE et.eventtype_desc,
      'entry_no' VALUE e.entry_no,
      'starttime' VALUE TO_CHAR(e.entry_starttime, 'HH24:MI:SS'),
      'finishtime' VALUE TO_CHAR(e.entry_finishtime, 'HH24:MI:SS'),
      'elapsedtime' VALUE TO_CHAR(e.entry_elapsedtime, 'HH24:MI:SS')
    )
  )

) AS team_json
FROM team t

JOIN carnival c ON t.carn_date = c.carn_date
JOIN entry e ON t.team_id = e.team_id
JOIN competitor r ON e.comp_no = r.comp_no
JOIN event ev ON e.event_id = ev.event_id
JOIN eventtype et ON ev.eventtype_code = et.eventtype_code
JOIN competitor comp ON comp.comp_no = (

    SELECT comp_no FROM entry 
    WHERE event_id = t.event_id AND entry_no = t.entry_no
)

GROUP BY t.team_id, t.team_name, c.carn_name, c.carn_date, comp.comp_fname, comp.comp_lname, comp.comp_phone, comp.comp_email;





