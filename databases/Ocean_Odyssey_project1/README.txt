📚 Database Design – Ocean Odyssey (Portfolio Version)
This project demonstrates the end-to-end design and implementation of a relational database system, built for a hypothetical global cruise management company. The design process follows best-practice industry methodology, transitioning from conceptual modelling to logical modelling and database deployment.

🧩 Project Overview
Ocean Odyssey is a simulated cruise booking system. It manages data on ships, operators, cruises, cabins, passengers (including minors and guardians), bookings, manifests, and cabin allocations.

✅ Deliverables
Conceptual Model
Created a comprehensive Entity-Relationship Diagram (ERD) using crow’s foot notation to represent key business entities, attributes, and relationships. The model includes cardinalities and business rules, with no use of surrogate keys.

Data Normalisation
Applied step-by-step normalization to 3NF from unstructured cruise itinerary data. Carefully identified functional dependencies, candidate keys, and eliminated redundancy through a series of normalized relations (UNF → 1NF → 2NF → 3NF).

Logical Model & Schema Implementation
Developed a 3NF logical model using Oracle Data Modeler.
Integrated surrogate keys where appropriate (e.g. composite key simplification).
Enforced integrity through primary and foreign key constraints, check constraints, and lookup enforcement.
Annotated all attributes and exported an SQL schema file.

Deployed the schema in Oracle and verified creation using a generated spool output.

Version Control
Maintained full development history via Git, with atomic commits and staged progress logs for conceptual modelling, normalization, and schema generation.

📂 Key Technologies & Skills
Tools Used: Oracle SQL Developer Data Modeler, Oracle SQL, Lucidchart, Git

Core Skills: ER Modelling, 3NF Normalization, Logical Schema Design, Relational Modelling, SQL Schema Scripting, Data Integrity Enforcement

