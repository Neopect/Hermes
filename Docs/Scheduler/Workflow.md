# Scheduler Workflow

# Sample for generating a job
1. A request is made
2. The request is sent to desired function
   - *name, command, time/frequency*
3. Clock generates a cron job
4. Clock passes the job's description to the ledger
   - *[name, command, time, enabled, job]*

## Workflow for creating and running a job
*Creating a job*
1. The scheduler creates a RPC server thread
2. A job request is made
3. Clock creates cron job from parameters
4. Clock saves task with a security key to ledger
5. 
*Running a job*
1. Cron executes python file from data folder
2. A RPC client thread is made
3. Client fetches data
4. Job runs script
5. Connection is closed and exits process