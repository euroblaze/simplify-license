# Specification

## What does this module do?

It allows for the proper handling of licensing of Odoo modules and Odoo based vertical solutions. 
The primary use case is a base Community or Enterprise Odoo installation, loaded with a number of modules.

The "Solution" based on Community or Enterprise has a license key.
In case Enterprise is used, there is an Odoo license key.
Each module could have a license key.

## Host Odoo

The instance on which the licensed modules are installed is called a "Host".

The Host is identified by a database-ID.

## License Server (LS)

A relational database carries all the licensing data.

- structure this database schema
- decide on MySQL or PostgreSQL
- this could possibly be built as an Odoo module, integrating into the Contact database, as well as other business processes of the Publisher (and/or Reseller).

## Licensing Overview

General Settings -> Licensing shows an overview of 

- all modules insalled in the system
- their authors
- reseller, the company that is possibly reselling the module (ex. another company could be reseller of Simplify modules)
- respective license-key
- license type, "renewable" or "perpectual"
- version of Odoo with which the module is compatible

## manifest.py

Licensing Overview is build from the manifest files of all modules

## Heartbeat

The Host sends a ping to the LS using a Scheduled Action. 



