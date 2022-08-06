# The 5 W's

## **What:**
The Scheduler is system that is responsible for keeping track of requests and timing events under a unified system.

## **When:**


## **Where:**
This will be part of the base system of HA.
All data will be stored in the ledger

## **Why:**
- Will make tracking requests much easier
- Handling reminders and reoccurring events much easier to handle
- More resource efficient than using individual systems for each module
- Unifies handling time related events

## **How:**
The scheduling will be saved in a json file. The actually triggers will be triggered with cron