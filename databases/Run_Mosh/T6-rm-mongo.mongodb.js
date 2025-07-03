// *****PLEASE ENTER YOUR DETAILS BELOW*****
// T6-rm-mongo.mongodb.js

// Student ID: 35512075
// Student Name: W.A.S.I.Thilaksiri

// Comments for your marker:

// ===================================================================================
// DO NOT modify or remove any of the comments below (items marked with //)
// ===================================================================================

// Use (connect to) your database - you MUST update xyz001
// with your authcate username

use("wthi0003");



// (b)
// PLEASE PLACE REQUIRED MONGODB COMMAND TO CREATE THE COLLECTION HERE
// YOU MAY PICK ANY COLLECTION NAME
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer

// Drop collection
db.runmonashteams.drop()


// Create collection and insert documents

db.runmonashteams.insertOne({
    _id: 1,
    carn_name: "RM Spring Series Clayton 2024",
    carn_date: "22-Sep-2024",
    team_name: "Cheetahs",
    team_leader: {
      name: "Megan Chang",
      phone: "0466448162",
      email: "megan.chang@monash.com",
    },
    team_no_of_members: 3,
    team_members: [
      {
        competitor_name: "Megan Chang",
        competitor_phone: "0466448162",
        event_type: "10 Km Run",
        entry_no: 1,
        starttime: "08:33:00",
        finishtime: "09:08:00",
        elapsedtime: "00:35:00",
      },
      {
        competitor_name: "Corey Jones",
        competitor_phone: "0492996081",
        event_type: "10 Km Run",
        entry_no: 8,
        starttime: "08:17:00",
        finishtime: "08:46:00",
        elapsedtime: "00:29:00",
      },
      {
        competitor_name: "John Browning",
        competitor_phone: "0428693000",
        event_type: "10 Km Run",
        entry_no: 7,
        starttime: "08:51:00",
        finishtime: "10:00:00",
        elapsedtime: "01:09:00",
      },
    ],
  });

  db.runmonashteams.insertMany([
{
    _id: 2,
    carn_name: "RM Spring Series Clayton 2024",
    carn_date: "22-Sep-2024",
    team_name: "Tigers",
    team_leader: {
      name: "Billy Sheppard",
      phone: "0444751217",
      email: "billy.sheppard@monash.com",
    },
    team_no_of_members: 1,
    team_members: [
      {
        competitor_name: "Billy Sheppard",
        competitor_phone: "0444751217",
        event_type: "10 Km Run",
        entry_no: 2,
        starttime: "08:42:00",
        finishtime: "10:07:00",
        elapsedtime: "01:25:00",
      },
    ],
  },
  {
    _id: 3,
    carn_name: "RM Spring Series Caulfield 2024",
    carn_date: "05-Oct-2024",
    team_name: "Cheetahs",
    team_leader: {
      name: "Edward Griffin",
      phone: "0467885403",
      email: "edward.griffin@gmail.com",
    },
    team_no_of_members: 1,
    team_members: [
      {
        competitor_name: "Edward Griffin",
        competitor_phone: "0467885403",
        event_type: "10 Km Run",
        entry_no: 5,
        starttime: "08:03:00",
        finishtime: "09:19:00",
        elapsedtime: "01:16:00",
      },
    ],
  },
  {
    _id: 4,
    carn_name: "RM Summer Series Caulfield 2025",
    carn_date: "02-Feb-2025",
    team_name: "Cheetahs",
    team_leader: {
      name: "Richard Bowers",
      phone: "0475220111",
      email: "richard.bowers@monash.com",
    },
    team_no_of_members: 1,
    team_members: [
      {
        competitor_name: "Richard Bowers",
        competitor_phone: "0475220111",
        event_type: "10 Km Run",
        entry_no: 3,
        starttime: "08:02:00",
        finishtime: "09:25:00",
        elapsedtime: "01:23:00",
      },
    ],
  },
  {
    _id: 5,
    carn_name: "RM Autumn Series Clayton 2025",
    carn_date: "15-Mar-2025",
    team_name: "Falcons",
    team_leader: {
      name: "Tammy Howard",
      phone: "0450709944",
      email: "tammy.howard@monash.com",
    },
    team_no_of_members: 1,
    team_members: [
      {
        competitor_name: "Tammy Howard",
        competitor_phone: "0450709944",
        event_type: "5 Km Run",
        entry_no: 1,
        starttime: "08:40:00",
        finishtime: "09:48:00",
        elapsedtime: "01:08:00",
      },
    ],
  },
  {
    _id: 6,
    carn_name: "RM Winter Series Caulfield 2025",
    carn_date: "29-Jun-2025",
    team_name: "Panthers",
    team_leader: {
      name: "Rebecca Wagner",
      phone: "0458056573",
      email: "rebecca.wagner@monash.com",
    },
    team_no_of_members: 1,
    team_members: [
      {
        competitor_name: "Rebecca Wagner",
        competitor_phone: "0458056573",
        event_type: "21.1 Km Half Marathon",
        entry_no: 1,
        starttime: "08:40:00",
        finishtime: "09:00:00",
        elapsedtime: "00:20:00",
      }
    ]
  }
  ]);





// List all documents you added
db.runmonashteams.find({}).pretty();


// (c)
// PLEASE PLACE REQUIRED MONGODB COMMAND/S FOR THIS PART HERE
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer

db.runmonashteams.find({"team_members.event_type":{"$in": ["5 Km Run", "10 Km Run"]}},
  {"_id": 0,"carn_date": 1,"carn_name": 1,"team_members.competitor_name": 1,"team_members.competitor_phone": 1}
);



// (d)
// PLEASE PLACE REQUIRED MONGODB COMMAND/S FOR THIS PART HERE
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer


// (i) Add new team
db.runmonashteams.insertOne(
    {
    _id: 7,
    carn_name: "RM Winter Series Caulfield 2025",
    carn_date: "29-Jun-2025",
    team_name: "The Great Runners",
    team_leader: {
      name: "Jackson Bull",
      phone: "0422412524",
      email: "jackson.bull@monash.edu"},
    team_no_of_members:1,
    team_members: [
      {
        competitor_name: "Jackson Bull",
        competitor_phone: "0422412524",
        event_type: "5 Km Run",
        entry_no: 11,
         starttime: "08:30:00",
        finishtime: "09:00:00",
        elapsedtime: "00:30:00"
      },
    ]})


// Illustrate/confirm changes made
db.runmonashteams.find({team_name:"The Great Runners"}).pretty();




// (ii) Add new team member
db.runmonashteams.updateOne(
  { team_name: {$eq: "The Great Runners" }},
  {$push: {
      team_members: {
        competitor_name: "Steve Bull",
        competitor_phone: "0422251427",
        event_type: "10 Km Run",
        entry_no: 2,
        starttime: "08:45:00",
        finishtime: "09:40:00",
        elapsedtime: "00:55:00"
      }
    },
   
    $inc: { team_no_of_members: 1 }
  });





// Illustrate/confirm changes made
db.runmonashteams.find({ team_name: "The Great Runners" }).pretty();


